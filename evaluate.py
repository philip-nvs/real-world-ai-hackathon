#!/usr/bin/env python3
"""Dev loop: run the same agent as run.py on the hand-cut test cases in cases/test/, and have
Claude judge its next step against each case's gold ANSWER.md.

Each test case holds the history up to a curated cut-off; ANSWER.md (never shown to the agent)
gives the gold action (act/ask/wait/escalate) and description. The agent's tools answer from
the case's bank_env fixture, seeing only the test history's events; every bank call lands in
answers/<case>/bank_log.json. --mock uses tools.py's mocks instead.

    python evaluate.py                 # all 50 test cases
    python evaluate.py 001 017 041     # a few
"""

import argparse
import json
import re
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic

from bank_env.fixture_adapter import FixtureAdapter
from bank_env.world import FIXTURES, load_scenario
from run import call_claude, load_case, load_env, run_case, section
from tools import TOOLS

ROOT = Path(__file__).parent
TEST_CASES, FULL_CASES = ROOT / "cases" / "test", ROOT / "cases" / "full"
DECISIONS = ("act", "ask", "wait", "escalate")
JUDGE_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["pass", "reason"],
    "properties": {"pass": {"type": "boolean"}, "reason": {"type": "string"}},
}


def parse_gold(path):
    """ANSWER.md -> {"cut_off": "event-002", "action": "act", "description": "..."}."""
    text = Path(path).read_text()
    field = lambda name: (m := re.search(rf"^\s*-\s*{name}:\s*(.+)$", text, re.M | re.I)) and m.group(1).strip().strip("`")
    return {"cut_off": field("Cut-off") or "", "action": (field("Action") or "").lower(),
            "description": field("Description") or ""}


def stage_case(src, dst):
    """Copy a test case for the agent, leaving ANSWER.md behind. dst is cleared first so nothing
    from an earlier run (e.g. a later attachment) leaks in."""
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("ANSWER.md"))


def judge(client, gold, outcome, answer_md):
    resp = call_claude(
        client,
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": JUDGE_SCHEMA}},
        messages=[{"role": "user", "content": f"""You grade a banking agent's next step on an escalated case.

Gold next step: {gold['action']}: {gold['description']}
Recorded outcome of the real case (one acceptable ending, not the only one): {outcome or 'not recorded'}

Agent's answer:
{answer_md}

Pass if the agent's next step targets the same specific record/team/process as the gold step, or is an \
equally narrow and safe step that would lead to the same outcome. Judge the step itself, not the label: a \
referral to a specialist team may be labelled act or escalate. Fail if it is broader, skips the check the gold \
step makes, takes an action the gold avoids, promises anything outside the bank's records, or hands the case to \
a human when the gold step can be taken. Give a one-sentence reason."""}],
    )
    return json.loads(next(b.text for b in resp.content if b.type == "text"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="case numbers (default: all)")
    ap.add_argument("--cases", default=str(TEST_CASES))
    ap.add_argument("--out", default="eval_out")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--mock", action="store_true", help="use tools.py's mocks instead of the fixture adapter")
    args = ap.parse_args()
    load_env()

    out = Path(args.out)
    srcs = sorted(p for p in Path(args.cases).iterdir() if (p / "ANSWER.md").is_file()
                  and (not args.ids or p.name in args.ids))
    if not srcs:
        sys.exit(f"No test cases (with ANSWER.md) under {args.cases}")
    client = anthropic.Anthropic(timeout=600, max_retries=3)

    def one(src):
        gold = parse_gold(src / "ANSWER.md")
        stage_case(src, out / "cases" / src.name)
        bank = None
        if not args.mock and (FIXTURES / f"{src.name}.json").is_file():
            visible = {e["id"] for e in load_case(src)["events"]}
            bank = FixtureAdapter(load_scenario(src.name), visible_events=visible)
        r = run_case(out / "cases" / src.name, out / "answers" / src.name, client, bank.tools() if bank else TOOLS)
        if bank:
            (out / "answers" / src.name / "bank_log.json").write_text(json.dumps(bank.log, indent=2, ensure_ascii=False))
        full_index = FULL_CASES / src.name / "index.md"
        outcome = section(full_index.read_text(), "Outcome") if full_index.is_file() else ""
        try:
            verdict = judge(client, gold, outcome, (out / "answers" / src.name / "ANSWER.md").read_text())
        except Exception as e:
            verdict = {"pass": False, "reason": f"judge failed: {e}"}
        print(f"  {src.name}: {r['decision']} (gold {gold['action']}) {'PASS' if verdict['pass'] else 'FAIL'}", file=sys.stderr)
        return {**r, **verdict, "gold": gold, "bank": "fixture" if bank else "mock",
                "bank_calls": [c.get("output", {}).get("status") or c.get("fault") for c in bank.log] if bank else []}

    with ThreadPoolExecutor(args.workers) as pool:
        rows = list(pool.map(one, srcs))

    n = len(rows)
    passed = sum(r["pass"] for r in rows)
    agree = sum(r["decision"] == r["gold"]["action"] for r in rows)
    confusion = {g: {d: sum(r["gold"]["action"] == g and r["decision"] == d for r in rows) for d in DECISIONS}
                 for g in DECISIONS if any(r["gold"]["action"] == g for r in rows)}
    lines = [
        "# Scorecard", "",
        f"- Pass rate (judge): **{passed}/{n}** ({passed / max(n, 1):.0%})",
        f"- Decision matches gold action: {agree}/{n} ({agree / max(n, 1):.0%})",
        f"- Guard blocks (red flags caught before reaching the customer): {sum(r['blocked'] for r in rows)}",
        f"- Crashes (fallback escalations): {sum(r['crashed'] for r in rows)}",
        f"- Tokens: {sum(r['tokens'][0] for r in rows):,} in / {sum(r['tokens'][1] for r in rows):,} out (agent only)",
        f"- Bank: fixture adapter for {sum(r['bank'] == 'fixture' for r in rows)} cases, mocks for {sum(r['bank'] == 'mock' for r in rows)}",
        "", "Gold action (rows) vs agent decision (columns):", "",
        "| gold \\ agent | " + " | ".join(DECISIONS) + " |", "|---|" + "---|" * len(DECISIONS),
        *[f"| {g} | " + " | ".join(str(c[d]) for d in DECISIONS) + " |" for g, c in confusion.items()],
        "", "| Case | Cut-off | Gold | Decision | Result | Bank calls | Agent next action | Gold next step | Judge |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    cell = lambda s: str(s).replace("|", "/").replace("\n", " ")
    lines += [f"| {r['case']} | {r['gold']['cut_off']} | {r['gold']['action']} | {r['decision']} | "
              f"{'PASS' if r['pass'] else 'FAIL'} | {cell(', '.join(map(str, r['bank_calls'])) or r['bank'])} | "
              f"{cell(r['next_action'])} | {cell(r['gold']['description'])} | {cell(r['reason'])} |" for r in rows]
    (out / "scorecard.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:8]), file=sys.stderr)
    print(f"Full scorecard: {out / 'scorecard.md'}", file=sys.stderr)


if __name__ == "__main__":
    main()
