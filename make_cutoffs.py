#!/usr/bin/env python3
"""Generate extra test cut-offs: every point in a public case where the bank has to decide its
next step, not just the one curated in cases/test/.

A decision point is a cut after event K where event K is new input (a customer or outside
message, a system or team reply; not the bank agent's own move) and event K+1 is the bank's.
Right after the agent's own move it is only waiting on itself, so those points are skipped, as is
any point that is the curated cut-off minus the agent's own preparatory moves.

    uv run make_cutoffs.py              # all cases -> cases/cutoffs/NNN-eKKK/
    uv run make_cutoffs.py 012 013      # a few

A cut-off after event KKK shows the agent events 1..KKK. Each one is built from the curated test
case (its neutralised title and Open status), the full history cut after KKK, and the attachments
the visible history or the request names. Claude reads the whole public case and writes the gold
next step to ANSWER.md in the cases/test format, or marks the point unusable. The curated cut-off
itself is skipped: cases/test/ already has it. cases/cutoffs/MANIFEST.md lists what was written
and skipped."""

import argparse
import json
import re
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic

from bank_env.world import load_scenario
from evaluate import FULL_CASES, TEST_CASES, parse_gold
from run import call_claude, load_case, load_env, section

CUTOFFS = Path(__file__).parent / "cases" / "cutoffs"
GOLD_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["usable", "reason", "action", "description"],
    "properties": {
        "usable": {"type": "boolean"},
        "reason": {"type": "string"},
        "action": {"type": "string", "enum": ["act", "ask", "wait", "escalate"]},
        "description": {"type": "string"},
    },
}


def decision_points(case_id, curated_k):
    """Cut-offs (event numbers K) where the bank has to decide, excluding the curated one."""
    events = load_case(FULL_CASES / case_id)["events"]
    bank = {e.id: e.bank_originated for e in load_scenario(case_id).world.events}
    agent = [bool(re.search(r"\bagent\b", e["from"], re.I)) for e in events]
    points = [k for k in range(1, len(events)) if not agent[k - 1] and bank.get(events[k]["id"])]
    same_as_curated = lambda k: k < curated_k and all(agent[k:curated_k])
    return [k for k in points if k != curated_k and not same_as_curated(k)]


def cut_history(case_id, k):
    """The curated test history's header with the full history's events 1..k."""
    full = (FULL_CASES / case_id / "history.md").read_text()
    header = (TEST_CASES / case_id / "history.md").read_text()
    header = header[: header.index('<a id="event-')]
    header = re.sub(r"^Total events: \d+", f"Total events: {k}", header, flags=re.M)
    start = full.index('<a id="event-')
    end = full.find(f'<a id="event-{k + 1:03d}"></a>')
    return header + full[start: end if end != -1 else None].rstrip() + "\n"


def visible_attachments(case_id, history):
    request = section((FULL_CASES / case_id / "index.md").read_text(), "Initial request")
    att_dir = FULL_CASES / case_id / "attachments"
    return sorted(p for p in att_dir.iterdir() if p.name in history or p.name in request) if att_dir.is_dir() else []


def cut_index(case_id, k, attachments):
    """The curated test index with Updated at event k and the attachments visible by then."""
    index = (TEST_CASES / case_id / "index.md").read_text()
    event = load_case(FULL_CASES / case_id)["events"][k - 1]
    index = re.sub(r"^(\s*-\s*\*\*Updated:\*\*).*$", rf"\g<1> {event['ts']}", index, flags=re.M)
    listing = "\n".join(f"- [{a.name}](attachments/{a.name})" for a in attachments) or "None."
    return re.sub(r"(^## Attachments[ \t]*\n).*\Z", rf"\g<1>\n{listing}\n", index, flags=re.M | re.S)


def build_cut(case_id, k, dst):
    history = cut_history(case_id, k)
    attachments = visible_attachments(case_id, history)
    shutil.rmtree(dst, ignore_errors=True)
    dst.mkdir(parents=True)
    (dst / "history.md").write_text(history)
    (dst / "index.md").write_text(cut_index(case_id, k, attachments))
    for a in attachments:
        (dst / "attachments").mkdir(exist_ok=True)
        shutil.copy(a, dst / "attachments" / a.name)


def gold(client, case_id, k, curated):
    case = load_case(FULL_CASES / case_id)
    prompt = f"""Below is a complete escalated case from Harrow & Vale Bank (H&V), ending included.

{case['index']}

{case['history']}

An AI agent handling this case sees only the events up to and including event-{k:03d} (later events are hidden \
from it). Write the gold answer for that cut-off: the single right next step for H&V at that point. Use what H&V \
actually did next in this case as the guide, as long as it is right for what the agent can see.

Actions:
- act: H&V takes the next step now: a read-only check of its records, a request to an internal H&V team, or an \
account change the customer has already instructed or confirmed in a way that counts.
- ask: nothing can move until the customer confirms or provides something; H&V sends the question or the prepared \
change for confirmation.
- wait: the right step is already in progress (a check or request is pending, or the customer must finish a secure \
step themselves); H&V does nothing now.
- escalate: a human must decide: conflicting evidence H&V's records can't resolve, suspected fraud, a request outside \
the agent's authority, or failures blocking progress.

The description is one specific sentence naming the customer, the record, team or process, and any limit (e.g. \
"without changing the order"), in the style of this curated answer for the same case at event-{curated['cut_off'][-3:]}:
- Action: `{curated['action']}`
- Description: {curated['description']}

Set usable to false if no decision is needed from H&V at this cut-off or the right step can't be determined; give \
the reason either way."""
    resp = call_claude(client, messages=[{"role": "user", "content": prompt}],
                       output_config={"effort": "high", "format": {"type": "json_schema", "schema": GOLD_SCHEMA}})
    return json.loads(next(b.text for b in resp.content if b.type == "text"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="case numbers (default: all)")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    load_env()
    client = anthropic.Anthropic(timeout=600, max_retries=3)

    points = []
    for case_dir in sorted(p for p in TEST_CASES.iterdir() if (p / "ANSWER.md").is_file()):
        if args.ids and case_dir.name not in args.ids:
            continue
        curated = parse_gold(case_dir / "ANSWER.md")
        curated_k = int(curated["cut_off"].split("-")[1])
        points += [(case_dir.name, k, curated) for k in decision_points(case_dir.name, curated_k)]

    def one(point):
        case_id, k, curated = point
        name = f"{case_id}-e{k:03d}"
        try:
            g = gold(client, case_id, k, curated)
        except Exception as e:
            g = {"usable": False, "reason": f"generation failed: {type(e).__name__}: {e}", "action": "", "description": ""}
        if g["usable"]:
            build_cut(case_id, k, CUTOFFS / name)
            (CUTOFFS / name / "ANSWER.md").write_text(
                f"- Cut-off: event-{k:03d}\n- Action: `{g['action']}`\n- Description: {g['description']}\n"
                f"- Source: generated by make_cutoffs.py from the full public case\n")
        else:
            shutil.rmtree(CUTOFFS / name, ignore_errors=True)
        print(f"  {name}: {g['action'] if g['usable'] else 'skipped'}", file=sys.stderr)
        return name, g

    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(one, points))

    manifest = CUTOFFS / "MANIFEST.md"
    rows = {}
    if manifest.is_file():  # keep rows for cases not regenerated this run
        rows = {m[1]: m[0] for m in re.findall(r"^(\| (\d{3}-e\d{3}) \|.*)$", manifest.read_text(), re.M)}
    cell = lambda s: str(s).replace("|", "/").replace("\n", " ")
    for name, g in results:
        rows[name] = f"| {name} | {g['action'] if g['usable'] else 'skipped'} | {cell(g['reason'])} |"
    used = sum("| skipped |" not in r for r in rows.values())
    manifest.write_text("\n".join([
        "# Generated cut-offs", "",
        f"{used} usable cut-offs, {len(rows) - used} skipped. Generated by `make_cutoffs.py`; the curated "
        "cut-off of each case lives in `cases/test/`.", "",
        "| Cut-off | Gold action | Reason |", "|---|---|---|", *[rows[k] for k in sorted(rows)], ""]))
    print(f"{used} usable, {len(rows) - used} skipped -> {CUTOFFS}", file=sys.stderr)


if __name__ == "__main__":
    main()
