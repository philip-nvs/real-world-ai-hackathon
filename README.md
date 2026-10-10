# real-world-ai-hackathon

Nevis' contribution to Dwelly's Real-world Agents hackathon: a batch case agent for the **Banking & Financial Services** track.

One command reads every case, works out the single next step with Claude and a small set of bank tools, runs it past a code-only policy guard, and writes one of four decisions (**act**, **ask**, **wait**, **escalate**) per case.

## Setup

```bash
uv sync
cp .env.example .env   # then put your ANTHROPIC_API_KEY in .env
```

MongoDB (`src/repository`, set `MONGODB_URI`/`MONGODB_DB` in `.env`):

```bash
docker compose up -d
```

## Case and session API

`uv run fastapi dev src/main.py`. Full spec: [`src/openapi.yaml`](src/openapi.yaml) (a test keeps it in step with the routes). A case is one MongoDB document in `cases`, keyed by case id, holding every file's path, type and bytes (15 MB cap per case).

| Endpoint | Does |
|---|---|
| `POST /cases` | multipart `files`, each filename its path (`001/attachments/x.pdf`, what `<input webkitdirectory>` sends). One shared top folder becomes the case id and is stripped; loose files need a `case_id` form field. Re-uploading an id replaces it. |
| `GET /cases` | case ids and upload times |
| `GET /cases/{id}` | file list (path, size, type), no bytes |
| `GET /cases/{id}/files/{path}` | one file's raw bytes |
| `DELETE /cases/{id}` | removes the case (its sessions stay) |
| `POST /cases/{id}/sessions` | 202, starts a one-shot agent run on the stored case in the background |
| `GET /cases/{id}/sessions` | the case's sessions, newest first |
| `GET /sessions/{id}` | status (`queued`, `running`, `done`, `failed`), the decision, `answer_md`, `reasoning_md`, bank log, tokens |
| `GET /sessions/{id}/events?after=N` | trace lines with `seq > N`, for polling |

A session (`src/agent/sessions.py`) writes the case to a temp folder and runs the same `run_case` as `run.py` in a worker thread (`AGENT_WORKERS`, default 4). Tools answer from the case's `bank_env` fixture when one exists (case `017-event-004` uses fixture `017` and sees only its own events), otherwise from `tools.py`. Every trace line goes to `session_events` as it happens; the result goes to `sessions`. Runs live in the API process, so a restart marks unfinished sessions `failed`.

```bash
curl -F files=@cases/full/001/index.md\;filename=001/index.md -F files=@cases/full/001/history.md\;filename=001/history.md localhost:8000/cases
```

## Run

```bash
uv run run.py HackatonChallendges/ --out ANSWERS/
```

`run.py` accepts a folder of case folders, nested track folders, or a single case folder (anything holding an `index.md`). `--workers N` sets parallelism (default 4). The agent itself lives in `src/agent/core.py`; `run.py` is the batch CLI around it.

Each case gets `ANSWERS/<case>/`:

| File | Contents |
|---|---|
| `ANSWER.md` | What the system received, what it did, the decision, what it escalated, what failed, the final result |
| `REASONING.md` | Evidence (with event IDs), conflicts between events, options rejected, policy-guard blocks |
| `trace.jsonl` | Every model turn, tool call, tool result, guard block and the final decision |

A case that crashes or times out still gets an **Escalate** answer with a handover note, so coverage is never partial.

## How it works

1. **Loader** (`src/agent/core.py: load_case`) reads `index.md`, `history.md` and `attachments/` loosely: missing files or fields never crash it. PDFs and images go to Claude as documents and images; CSV/TXT go inline.
2. **Agent loop** (`src/agent/core.py: run_agent`): Claude (`claude-opus-5-5`, adaptive thinking, effort high) calls bank tools and finishes with `submit_decision`, a strict JSON schema.
3. **Tool adapter** (`tools.py`): `check_record`, `submit_internal_request`, `submit_instruction`, `send_secure_message`. Mocks today; replace the function bodies with the real bank tools and nothing else changes. Tool errors go back to the agent and into the answer.
4. **Policy guard** (`src/agent/core.py: guard_tool`, `guard_decision`): plain regex and lookup code, no LLM. It blocks:
   - promising a refund, a fraud finding, delivery or receipt by a recipient, or a guarantee
   - asking for passwords, PINs or one-time codes, and advising a customer to pay again
   - re-sending or duplicating a payment
   - an account-changing instruction not backed by a customer event on a secure channel (an email is never authorisation)
   - escalating without a handover

   A blocked call goes back to Claude to re-plan.
5. **Writer** (`src/agent/core.py: write_answer`) produces the three files.

Server-side refusal fallback (`fallbacks: "default"`) is on for every Claude call.

## Dev loop

```bash
uv run evaluate.py                # every test cut-off in cases/test/
uv run evaluate.py 001 017 041    # all cut-offs of a few public cases
uv run evaluate.py 017-event-004  # one cut-off
uv run evaluate.py --mock         # against tools.py's mocks instead of the simulated bank
```

Each folder in `cases/test/` (`NNN-event-KKK/`) holds public case NNN's history up to event KKK, with 2–4 cut-offs per case. Its `answer/` folder holds the gold next step in `ANSWER.md` (action and description) and any artefact from the full case. The agent never sees `answer/`.

The dev loop runs the same `run_case` with the agent's tools answering from the case's `bank_env` fixture. The adapter sees only the events in the test history, so a confirmation that comes later doesn't count yet. Claude then judges the agent's step against the gold one. `eval_out/scorecard.md` holds:
- the judge's pass rate;
- how often the agent's decision matches the gold action, plus a gold-vs-agent table;
- guard blocks, crashes and tokens;
- each case's bank calls (full log in `eval_out/answers/<case>/bank_log.json`).

## Tests

```bash
uv run test_run.py
uv run test_bank_env.py
uv run -m src.repository.test_repository   # needs MongoDB running
uv run --with pytest pytest src/            # API; the upload and session tests need MongoDB running
```

Neither needs an API key.
- `test_run.py` covers the loader, the guard rules, parsing the gold answers, staging test cases without their `answer/` folder, the consistency of every test cut-off (history ends at the cut-off, only attachments the agent could know of), the agent loop driven by a scripted fake Claude (including a guard block and re-plan), and the crash fallback.
- `test_bank_env.py` replays every lookup the public cases' own agent makes against the fixtures, and covers the adapter, overlays and faults.
