#!/usr/bin/env python3
"""Batch case agent for the Banking track.

    uv run -m src.run CASES_DIR --out ANSWERS/

Every case folder (one holding index.md) under CASES_DIR gets ANSWERS/<case>/ with
ANSWER.md, REASONING.md and trace.jsonl. A case that crashes still gets an Escalate answer.
The agent itself lives in src/agent/core.py; the API runs the same agent.
"""

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic

from src.agent.core import MODEL, load_env, run_case


def find_cases(root):
    root = Path(root)
    if (root / "index.md").is_file():
        return [(root, Path(root.name))]
    return sorted((p.parent, p.parent.relative_to(root)) for p in root.rglob("index.md"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cases", help="folder of case folders (or a single case folder)")
    ap.add_argument("--out", default="ANSWERS", help="output folder (default ANSWERS/)")
    ap.add_argument("--workers", type=int, default=4, help="cases run in parallel (default 4)")
    args = ap.parse_args()

    load_env()
    cases = find_cases(args.cases)
    if not cases:
        sys.exit(f"No case folders (with index.md) under {args.cases}")
    client = anthropic.Anthropic(timeout=600, max_retries=3)
    print(f"Running {len(cases)} cases with {MODEL} -> {args.out}/", file=sys.stderr)

    def one(item):
        src, rel = item
        r = run_case(src, Path(args.out) / rel, client)
        print(f"  {rel}: {r['decision']}{' (CRASHED → fallback)' if r['crashed'] else ''}", file=sys.stderr)
        return r

    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(one, cases))
    counts = {k: sum(r["decision"] == k for r in results) for k in ("act", "ask", "wait", "escalate")}
    crashed = sum(r["crashed"] for r in results)
    print(f"Done: {len(results)} cases · " + " · ".join(f"{k} {v}" for k, v in counts.items())
          + f" · crashed {crashed} · guard blocks {sum(r['blocked'] for r in results)}", file=sys.stderr)
    if crashed == len(results):
        print("Every case crashed. Check credentials (ANTHROPIC_API_KEY) and a trace.jsonl.", file=sys.stderr)


if __name__ == "__main__":
    main()
