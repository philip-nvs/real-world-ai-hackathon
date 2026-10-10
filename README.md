# real-world-ai-hackathon

Nevis' contribution to Dwelly's Real-world Agents hackathon: a batch case agent for the **Banking & Financial Services** track.

One command reads every case, works out the single next step with Claude and a small set of bank tools, runs it past a code-only policy guard, and writes one of four decisions (**act**, **ask**, **wait**, **escalate**) per case.

## Setup

```bash
uv sync
cp .env.example .env   # then put your ANTHROPIC_API_KEY in .env
```

## Run

```bash
uv run run.py HackatonChallendges/ --out ANSWERS/
```

`run.py` accepts a folder of case folders, nested track folders, or a single case folder (anything holding an `index.md`). `--workers N` sets parallelism (default 4).

Each case gets `ANSWERS/<case>/`:

| File | Contents |
|---|---|
| `ANSWER.md` | What the system received, what it did, the decision, what it escalated, what failed, the final result |
| `REASONING.md` | Evidence (with event IDs), conflicts between events, options rejected, policy-guard blocks |
| `trace.jsonl` | Every model turn, tool call, tool result, guard block and the final decision |

A case that crashes or times out still gets an **Escalate** answer with a handover note, so coverage is never partial.

## How it works

1. **Loader** (`run.py: load_case`) reads `index.md`, `history.md` and `attachments/` loosely: missing files or fields never crash it. PDFs and images go to Claude as documents and images; CSV/TXT go inline.
2. **Agent loop** (`run.py: run_agent`): Claude (`claude-opus-5-5`, adaptive thinking, effort high) calls bank tools and finishes with `submit_decision`, a strict JSON schema.
3. **Tool adapter** (`tools.py`): `check_record`, `submit_internal_request`, `submit_instruction`, `send_secure_message`. Mocks today; replace the function bodies with the real bank tools and nothing else changes. Tool errors go back to the agent and into the answer.
4. **Policy guard** (`run.py: guard_tool`, `guard_decision`): plain regex and lookup code, no LLM. It blocks:
   - promising a refund, a fraud finding, delivery or receipt by a recipient, or a guarantee
   - asking for passwords, PINs or one-time codes, and advising a customer to pay again
   - re-sending or duplicating a payment
   - an account-changing instruction not backed by a customer event on a secure channel (an email is never authorisation)
   - escalating without a handover

   A blocked call goes back to Claude to re-plan.
5. **Writer** (`run.py: write_answer`) produces the three files.

Server-side refusal fallback (`fallbacks: "default"`) is on for every Claude call.

## Dev loop

```bash
uv run evaluate.py              # all 50 test cases in cases/test/
uv run evaluate.py 001 017 041  # a few
uv run evaluate.py --mock       # against tools.py's mocks instead of the simulated bank
uv run evaluate.py --cases cases/cutoffs   # the generated extra cut-offs
```

Each case in `cases/test/` holds a public case's history up to a hand-picked cut-off, with the gold next step in `ANSWER.md` (action and description). The agent never sees `ANSWER.md`. The dev loop runs the same `run_case` with the agent's tools answering from the case's `bank_env` fixture. The adapter sees only the events in the test history, so a confirmation that comes later doesn't count yet. Claude then judges the agent's step against the gold one. `eval_out/scorecard.md` holds:
- the judge's pass rate;
- how often the agent's decision matches the gold action, plus a gold-vs-agent table;
- guard blocks, crashes and tokens;
- each case's bank calls (full log in `eval_out/answers/<case>/bank_log.json`).

### More cut-offs

`cases/test/` has one curated cut-off per case. `cases/cutoffs/NNN-eKKK/` adds the case's other decision points: a cut after event KKK where that event is new input (a customer or outside message, a system or team reply) and the bank moves next. Points right after the agent's own move are left out, because it's only waiting on itself.
- `make_cutoffs.py` builds each one from the curated test case (same neutralised title), with the full history cut after KKK and only the attachments the visible history names. Rebuilding the curated cut-offs this way reproduces `cases/test/` exactly.
- Claude writes the gold `ANSWER.md` from the full case and marks it as generated. `cases/cutoffs/MANIFEST.md` lists every point, including the skipped ones, with Claude's reason.

## Tests

```bash
uv run test_run.py
uv run test_bank_env.py
```

Neither needs an API key.
- `test_run.py` covers the loader, the guard rules, parsing the gold answers and staging test cases without them, the agent loop driven by a scripted fake Claude (including a guard block and re-plan), and the crash fallback.
- `test_bank_env.py` replays every lookup the public cases' own agent makes against the fixtures, and covers the adapter, overlays and faults.
