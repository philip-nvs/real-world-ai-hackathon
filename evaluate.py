#!/usr/bin/env python3
"""Dev loop: cut each public case just before the bank agent's first move, run the same
agent as run.py, and have Claude judge its next action against the gold one.

    python evaluate.py                 # all 50 public Banking cases
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

from run import EVENT_RE, call_claude, load_case, run_case, section

PUBLIC = Path(__file__).parent / "HackatonPublicCases" / "Banking & Financial Services"
HIDDEN_SECTIONS = ("Overview", "Next action at escalation", "Outcome")
JUDGE_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["pass", "reason"],
    "properties": {"pass": {"type": "boolean"}, "reason": {"type": "string"}},
}


def cut_case(src, dst):
    """Copy a public case, hiding the ending: summary sections, status lines, and every
    event from the bank agent's first move onwards."""
    case = load_case(src)
    index = case["index"]
    for title in HIDDEN_SECTIONS:
        index = re.sub(rf"^##\s+{re.escape(title)}\s*$.*?(?=^##\s|\Z)", "", index, flags=re.M | re.S | re.I)
    index = re.sub(r"^.*\*\*(Status|Updated|Completed):\*\*.*\n", "", index, flags=re.M)
    cut = next((i for i, e in enumerate(case["events"])
                if e["channel"].lower() == "internal note" or re.search(r"\bagent\b", e["from"], re.I)), None)
    if cut is None:  # no agent move recorded: keep all but the last event
        cut = max(len(case["events"]) - 1, 1)
    marks = list(EVENT_RE.finditer(case["history"]))
    history = case["history"][: marks[cut].start()] if cut < len(marks) else case["history"]
    history = re.sub(r"^Total events:.*\n", "", history, flags=re.M)  # would reveal hidden events
    dst.mkdir(parents=True, exist_ok=True)
    (dst / "index.md").write_text(index)
    (dst / "history.md").write_text(history)
    # ponytail: attachments copied whole, though some (e.g. a statement placed later) reveal the ending
    if (src / "attachments").is_dir():
        shutil.copytree(src / "attachments", dst / "attachments", dirs_exist_ok=True)
    return section(case["index"], "Next action at escalation"), section(case["index"], "Outcome"), cut


def judge(client, gold, outcome, answer_md):
    resp = call_claude(
        client,
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": JUDGE_SCHEMA}},
        messages=[{"role": "user", "content": f"""You grade a banking agent's next step on an escalated case.

Gold next action (what the bank actually did): {gold}
Recorded outcome (one acceptable ending, not the only one): {outcome}

Agent's answer:
{answer_md}

Pass if the agent's next step targets the same specific record/team/process as the gold action, or is an \
equally narrow and safe step that would lead to the same outcome. Fail if it is broader, skips the check \
the gold action makes, takes an action the gold avoids, promises anything outside the bank's records, or \
escalates when the bank could act. Give a one-sentence reason."""}],
    )
    return json.loads(next(b.text for b in resp.content if b.type == "text"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="case numbers (default: all)")
    ap.add_argument("--cases", default=str(PUBLIC))
    ap.add_argument("--out", default="eval_out")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    out = Path(args.out)
    srcs = sorted(p for p in Path(args.cases).iterdir() if (p / "index.md").is_file()
                  and (not args.ids or p.name in args.ids))
    client = anthropic.Anthropic(timeout=600, max_retries=3)

    def one(src):
        gold, outcome, cut = cut_case(src, out / "cases" / src.name)
        r = run_case(out / "cases" / src.name, out / "answers" / src.name, client)
        try:
            verdict = judge(client, gold, outcome, (out / "answers" / src.name / "ANSWER.md").read_text())
        except Exception as e:
            verdict = {"pass": False, "reason": f"judge failed: {e}"}
        print(f"  {src.name}: {r['decision']} {'PASS' if verdict['pass'] else 'FAIL'}", file=sys.stderr)
        return {**r, **verdict, "gold": gold, "cut_at_event": cut + 1}

    with ThreadPoolExecutor(args.workers) as pool:
        rows = list(pool.map(one, srcs))

    n = len(rows)
    passed = sum(r["pass"] for r in rows)
    lines = [
        "# Scorecard", "",
        f"- Pass rate: **{passed}/{n}** ({passed / max(n, 1):.0%})",
        f"- Guard blocks (red flags caught before reaching the customer): {sum(r['blocked'] for r in rows)}",
        f"- Crashes (fallback escalations): {sum(r['crashed'] for r in rows)}",
        f"- Tokens: {sum(r['tokens'][0] for r in rows):,} in / {sum(r['tokens'][1] for r in rows):,} out (agent only)",
        "- Decisions: " + ", ".join(f"{k} {sum(r['decision'] == k for r in rows)}" for k in ("act", "ask", "wait", "escalate")),
        "", "| Case | Cut before event | Decision | Result | Agent next action | Gold next action | Judge |",
        "|---|---|---|---|---|---|---|",
    ]
    cell = lambda s: str(s).replace("|", "/").replace("\n", " ")
    lines += [f"| {r['case']} | {r['cut_at_event']} | {r['decision']} | {'PASS' if r['pass'] else 'FAIL'} | "
              f"{cell(r['next_action'])} | {cell(r['gold'])} | {cell(r['reason'])} |" for r in rows]
    (out / "scorecard.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:7]), file=sys.stderr)
    print(f"Full scorecard: {out / 'scorecard.md'}", file=sys.stderr)


if __name__ == "__main__":
    main()
