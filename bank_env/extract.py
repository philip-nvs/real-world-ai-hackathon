#!/usr/bin/env python3
"""Extract a world fixture from each full public case with Claude, validate it, write it.

    uv run python -m bank_env.extract 001 012 024     # writes bank_env/fixtures/NNN.json

Reads the whole case, endings included: the system replies after the agent's first move are
exactly what the bank's records hold. The agent never sees fixtures, only adapter replies."""

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic
from pydantic import ValidationError

from bank_env.schema import World, check_world
from bank_env.systems import PROCESSES, RECORD_SYSTEMS, TEAMS
from run import call_claude, case_content, load_case, load_env

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "cases" / "full"
FIXTURES = Path(__file__).parent / "fixtures"
MAX_ATTEMPTS = 3

catalogue = lambda d: "\n".join(f"- {k}: {v}" for k, v in d.items())
INSTRUCTIONS = f"""You build test fixtures for a simulated bank (Harrow & Vale, H&V). Above is one complete \
escalated case. Fill in the world model: what H&V's systems, teams and processes hold, so a simulator can answer an \
agent's lookups and requests the way the case's systems did.

Record systems (read-only lookups):
{catalogue(RECORD_SYSTEMS)}

Teams (asynchronous requests):
{catalogue(TEAMS)}

Account-changing processes:
{catalogue(PROCESSES)}

Rules:
- Only facts the case states. Unknown values are omitted or null; never invent dates, amounts or references.
- records: one per real-world object (a transfer, a standing order, a card, a file...). Take facts from system replies \
and from H&V system/portal status messages, including those after the agent's first move. Put the facts the system \
shows into attributes (status, amount_gbp, reason...). If the case restricts what may be shared (permitted wording, \
withheld basis or identifiers), set customer_facing and disclosure_rules.
- exists_before_agent: false for anything that only comes into being through an action during the case (a request \
registered or sent for approval, a case opened, a document issued, an export created); point created_by at the \
team_response or process whose action creates it. The simulator hides such records until that action happens.
- Facts that change during the case without an agent action (the customer's own recovery or confirmation step, a \
later system update): list each value as its own attribute with the same key, the original with since_event null and \
each later one with the since_event it holds from. Never fold a later state into a fact that held from the start. \
Changes made by a process belong in its effect instead.
- match_terms: the identifiers someone would search by: payee, amount like "420.00", date, case reference, file name, row id.
- team_responses: what each team replied to a request (status, reference, reply, produced document file name).
- processes: only account-changing operations the case performs or prepares. confirmed_by lists the events that are a \
valid confirmation of exactly that change: a customer's confirmation on a verified channel, or the administrator's for \
business roles. A request (e.g. a chat asking for a change the bank must still send for confirmation) is not a confirmation. \
effect lists the attribute values on the target record once applied. applied_event is the event in which the case records the change as done.
- events: every event in the history, with party, whether H&V sent it, and whether the customer was verified on it.
- Every record, team response and process cites the source_event it comes from."""


def parse(text, event_ids):
    """Returns (world, problems); world is None when the JSON itself is invalid."""
    m = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    try:
        world = World.model_validate_json(m.group(1) if m else text)
    except ValidationError as e:
        return None, [f"{'.'.join(map(str, err['loc']))}: {err['msg']}" for err in e.errors()[:20]]
    return world, check_world(world, event_ids)


def extract(client, case_dir):
    # The schema goes in the prompt, not output_config.format: it compiles to a grammar the API rejects as too large.
    case = load_case(case_dir)
    event_ids = [e["id"] for e in case["events"]]
    prompt = f"{INSTRUCTIONS}\n\nReply with only the World JSON in a ```json block, matching this JSON schema:\n" \
             f"{json.dumps(World.model_json_schema())}"
    messages = [{"role": "user", "content": case_content(case) + [{"type": "text", "text": prompt}]}]
    world, problems = None, ["no attempt made"]
    for _ in range(MAX_ATTEMPTS):
        resp = call_claude(client, messages=messages, output_config={"effort": "high"})
        text = "".join(b.text for b in resp.content if b.type == "text")
        candidate, problems = parse(text, event_ids)
        world = candidate or world
        if candidate and not problems:
            break
        messages += [{"role": "assistant", "content": text},
                     {"role": "user", "content": "Fix these problems and return the full World JSON again:\n- " + "\n- ".join(problems)}]
    if world is None:
        raise ValueError("no valid World JSON: " + "; ".join(problems))
    world.case_id = case["id"]
    return world, problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="+", help="case numbers, e.g. 001 012")
    ap.add_argument("--cases", default=str(CASES))
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    load_env()
    client = anthropic.Anthropic(timeout=600, max_retries=3)
    FIXTURES.mkdir(exist_ok=True)

    def one(case_id):
        try:
            world, problems = extract(client, Path(args.cases) / case_id)
        except Exception as e:
            return case_id, [f"{type(e).__name__}: {e}"]
        (FIXTURES / f"{case_id}.json").write_text(json.dumps(world.model_dump(), indent=2, ensure_ascii=False) + "\n")
        return case_id, problems

    with ThreadPoolExecutor(args.workers) as pool:
        for case_id, problems in pool.map(one, args.ids):
            print(f"  {case_id}: {'ok' if not problems else 'PROBLEMS: ' + '; '.join(problems)}", file=sys.stderr)


if __name__ == "__main__":
    main()
