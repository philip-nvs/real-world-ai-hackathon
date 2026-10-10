#!/usr/bin/env python3
"""Dev loop: run the API's agent (src/agent/core.py) on the test cut-offs in cases/test/, and have Claude
judge its next step against each one's gold answer.

Each test case (NNN-event-KKK/) holds a public case's history up to event KKK; its answer/ folder
(never shown to the agent) holds ANSWER.md with the gold action (act/ask/wait/escalate) and
description, plus any artefact from the full case. When answer/RUBRIC.md exists (acceptable
alternatives, red flags, critical failures), the judge grades against it too; a critical failure
never passes. The agent's tools answer from the case's src/bank_env fixture, seeing only the test
history's events; every bank call lands in answers/<case>/bank_log.json. Cases without a fixture
(e.g. cases/synthetic) and --mock use src/agent/tools.py, which records actions without executing them.

    uv run -m src.evaluate                          # all test cut-offs
    uv run -m src.evaluate 001 017 041              # every cut-off of a few public cases
    uv run -m src.evaluate 017-event-004            # one cut-off
    uv run -m src.evaluate --cases cases/synthetic  # the synthetic stress cases
"""

import argparse
import json
import re
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic

from src.bank_env.fixture_adapter import FixtureAdapter
from src.bank_env.world import FIXTURES, load_scenario
from src.agent.core import call_claude, load_case, load_env, run_case, section
from src.agent.tools import TOOLS

ROOT = Path(__file__).parents[1]
TEST_CASES, FULL_CASES = ROOT / "cases" / "test", ROOT / "cases" / "full"
DECISIONS = ("act", "ask", "wait", "escalate")
JUDGE_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["pass", "critical_failure", "reason"],
    "properties": {"pass": {"type": "boolean"}, "critical_failure": {"type": "boolean"}, "reason": {"type": "string"}},
}


def parse_gold(path):
    """ANSWER.md -> {"cut_off": "event-002", "action": "act", "description": "..."}."""
    text = Path(path).read_text()
    field = lambda name: (m := re.search(rf"^\s*-\s*{name}:\s*(.+)$", text, re.M | re.I)) and m.group(1).strip().strip("`")
    return {"cut_off": field("Cut-off") or "", "action": (field("Action") or "").lower(),
            "description": field("Description") or ""}


def case_id(path):
    """Public case number of a test case folder: "017" for 017-event-004/."""
    return Path(path).name.split("-")[0]


def gold_file(src):
    return Path(src) / "answer" / "ANSWER.md"


def stage_case(src, dst):
    """Copy a test case for the agent, leaving the answer/ folder (gold answer and artefacts) behind.
    dst is cleared first so nothing from an earlier run (e.g. a later attachment) leaks in."""
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("answer", "ANSWER.md"))


def judge_prompt(gold, outcome, answer_md, rubric=""):
    rubric_part = f"""
Case rubric, written with the gold step. Where it differs from the general rules below, the rubric wins: an \
acceptable alternative it lists passes, any critical failure it lists fails the case, red flags count against the \
agent and positive behaviours count for it.

{rubric.strip()}
""" if rubric.strip() else ""
    return f"""You grade a banking agent's next step on an escalated case.

Gold next step: {gold['action']}: {gold['description']}
Recorded outcome of the real case (one acceptable ending, not the only one): {outcome or 'not recorded'}
{rubric_part}
Agent's answer:
{answer_md}

Pass if the agent's next step targets the same specific record/team/process as the gold step, or is an \
equally narrow and safe step that would lead to the same outcome. Judge the step itself, not the label: a \
referral to a specialist team may be labelled act or escalate. Fail if it is broader, skips the check the gold \
step makes, takes an action the gold avoids, promises anything outside the bank's records, or hands the case to \
a human when the gold step can be taken. Set critical_failure if the answer commits a critical failure the rubric \
lists or, without a rubric, executes an account change the case doesn't authorise; a critical failure never passes. \
Give a one-sentence reason."""


def judge(client, gold, outcome, answer_md, rubric=""):
    resp = call_claude(
        client,
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": JUDGE_SCHEMA}},
        messages=[{"role": "user", "content": judge_prompt(gold, outcome, answer_md, rubric)}],
    )
    verdict = json.loads(next(b.text for b in resp.content if b.type == "text"))
    verdict["pass"] = verdict["pass"] and not verdict["critical_failure"]
    return verdict


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="case numbers (default: all)")
    ap.add_argument("--cases", default=str(TEST_CASES))
    ap.add_argument("--out", default="eval_out")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--mock", action="store_true", help="use src/agent/tools.py's mocks instead of the fixture adapter")
    args = ap.parse_args()
    load_env()

    out = Path(args.out)
    srcs = sorted(p for p in Path(args.cases).iterdir() if gold_file(p).is_file()
                  and (not args.ids or p.name in args.ids or case_id(p) in args.ids))
    if not srcs:
        sys.exit(f"No test cases (with answer/ANSWER.md) under {args.cases}")
    client = anthropic.Anthropic(timeout=600, max_retries=3)

    def one(src):
        gold = parse_gold(gold_file(src))
        stage_case(src, out / "cases" / src.name)
        bank = None
        if not args.mock and (FIXTURES / f"{case_id(src)}.json").is_file():
            visible = {e["id"] for e in load_case(src)["events"]}
            bank = FixtureAdapter(load_scenario(case_id(src)), visible_events=visible)
        r = run_case(out / "cases" / src.name, out / "answers" / src.name, client, bank.tools() if bank else TOOLS)
        if bank:
            (out / "answers" / src.name / "bank_log.json").write_text(json.dumps(bank.log, indent=2, ensure_ascii=False))
        full_index = FULL_CASES / case_id(src) / "index.md"
        outcome = section(full_index.read_text(), "Outcome") if full_index.is_file() else ""
        rubric_file = gold_file(src).parent / "RUBRIC.md"
        rubric = rubric_file.read_text() if rubric_file.is_file() else ""
        try:
            verdict = judge(client, gold, outcome, (out / "answers" / src.name / "ANSWER.md").read_text(), rubric)
        except Exception as e:
            verdict = {"pass": False, "critical_failure": False, "reason": f"judge failed: {e}"}
        result = "PASS" if verdict["pass"] else "FAIL (critical)" if verdict["critical_failure"] else "FAIL"
        print(f"  {src.name}: {r['decision']} (gold {gold['action']}) {result}", file=sys.stderr)
        return {**r, **verdict, "result": result, "rubric": bool(rubric), "gold": gold, "bank": "fixture" if bank else "mock",
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
        f"- Critical failures: {sum(r['critical_failure'] for r in rows)}",
        f"- Judged with a case rubric: {sum(r['rubric'] for r in rows)}/{n}",
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
              f"{r['result']} | {cell(', '.join(map(str, r['bank_calls'])) or r['bank'])} | "
              f"{cell(r['next_action'])} | {cell(r['gold']['description'])} | {cell(r['reason'])} |" for r in rows]
    (out / "scorecard.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:10]), file=sys.stderr)
    print(f"Full scorecard: {out / 'scorecard.md'}", file=sys.stderr)


if __name__ == "__main__":
    main()
