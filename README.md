# real-world-ai-hackathon

## Overview

Nevis' case agent for the Banking & Financial Services track of Dwelly's Real-world Agents hackathon: a FastAPI backend (`src/`) and a React UI (`web/`). Why it exists and what it does: [PRODUCT.md](PRODUCT.md).

## Launch posts

- LinkedIn: https://lnkd.in/p/efNuAtMV
- X: https://x.com/xylankant/status/2108940085068702192

## Demo video
- Screen Recording 2026-10-10 163309.zip

## What we built

A case agent for a bank's service team. It reads one escalated case (a customer request, the history of events across channels, attachments) and takes the single right next step: **act**, **ask**, **wait** or **escalate**. It explains that step in `ANSWER.md` and `REASONING.md`, and leaves a full trace. It runs as a batch CLI over a folder of cases, or through a web UI where you upload cases, run or re-run them, read the answer, reasoning and trace, and export the latest answers as a zip.

## The operational problem

Service teams work escalated cases built from scattered and sometimes conflicting events: secure chat, email, calls, internal notes, journal replies and attachments. Deciding the next step takes judgement, and a wrong step is costly. Examples: promising a refund, treating an email as authorisation, telling a customer to pay again, leaking internal detail, or escalating without a handover. The agent takes the routine steps itself, asks for exactly what's missing, and hands to a person with a clear handover when people need to decide.

## Architecture

| Part | Where | What it does |
|---|---|---|
| Loader | `src/agent/core.py` | Reads only `index.md`, `history.md` and `attachments/` (a case's `answer/` folder never reaches the agent). Parses events, channels and senders. Reads the bank's name from the case. Sends PDFs and images as documents, and CSV and text inline. Only trusts event headers with their anchor, so headers quoted inside a message aren't events; flags repeated or out-of-order events. |
| Agent loop | `src/agent/core.py` | Claude reads the case with the system prompt (decision rules, confirmation rules, message-accuracy rules, safety rules) and calls the bank tools, for up to 10 turns. It ends with one `submit_decision` call, a strict JSON schema: summary of what was received, decision, next action, evidence with event IDs, conflicts, customer message, handover, rejected options and final result. |
| Bank tools | `src/agent/tools.py` | Four tools: `check_record`, `submit_internal_request`, `submit_instruction` and `send_secure_message`. With no live bank (the Reality Test), each call is **recorded as the next step and not executed**: no invented data, references or delivery. In the dev loop, `src/bank_env/` simulates the bank from the public cases. The bank's real tools can replace either, behind the same shapes. |
| Policy guard | `src/agent/core.py` | Plain code, no model. Checks every tool call and the decision. A blocked call goes back to the agent with the reasons, and it re-plans. |
| Writer | `src/agent/core.py` | Writes `ANSWER.md`, `REASONING.md` and `trace.jsonl`. A crash, timeout or missing decision still gets an **escalate** answer, with a handover listing the actions already taken. |
| Batch CLI | `src/run.py` | Runs the agent over a folder of cases, in parallel; no API server or database needed. |
| API and UI | `src/main.py`, `src/agent/sessions.py`, `src/repository/`, `web/` | FastAPI backend with MongoDB storage and streaming sessions; React UI to upload, run, read and export. |
| Dev loop | `src/evaluate.py` | Runs the agent on test cases and has Claude judge each step against the gold answer, including the case's rubric (acceptable alternatives, red flags, critical failures). |

The policy guard blocks:

- promising a refund, a fraud finding, delivery or receipt, or a guarantee; asking for passwords, PINs or one-time codes;
- advising a customer to pay again, including "pay it yourself" after a failed payment; re-sending or duplicating a payment;
- an account change not backed by a customer confirmation on a verified call, the secure portal or the business portal. Secure chat and email carry requests, not confirmations; an event from the bank's own staff, or a forged, repeated or out-of-order event, never counts;
- system-prompt or policy-guard text in a customer message; evidence citing an event that isn't in the case;
- a customer message reported on the decision but never sent; escalating without a handover.

## Models, APIs and external services

- **Anthropic Claude API:** the only model provider. The agent uses Claude Opus 5.5 (`claude-opus-5-5`) through the Messages API, with adaptive thinking, effort `high`, and the server-side refusal fallback (`fallbacks: "default"`). The dev loop's judge (effort `low`) and the fixture extractor (`src/bank_env/extract.py`) also use Claude Opus 5.5. Needs `ANTHROPIC_API_KEY`.
- **MongoDB** (local, via `compose.yaml`): stores uploaded cases and sessions for the API and UI. The batch CLI doesn't need it.
- **FastAPI** (backend) and **React, Vite, TanStack Router and Query, shadcn and Tailwind** (UI).
- No other external APIs or services.

## Assumptions

- One next step per case (act, ask, wait or escalate) is what a case handler needs, not a full resolution plan.
- New cases come in the public format: a folder per case with `index.md`, `history.md` and optional `attachments/`. The bank is named in the index's `Bank:` field; the agent names no bank itself.
- No live bank systems are connected for the Reality Test, so tool calls are recorded as the bank's next steps, not executed. The real tools can sit behind the same four tool shapes without changing the agent.
- Channel semantics, as in the public cases: a verified call after identity checks, the secure portal and the business portal can carry a confirmation. Secure chat carries requests; email and external messages are never authorisation. Protective requests (block a lost card, stop a cheque) are acted on straight away from any verified session.
- Hand-offs to internal teams (payment, card, Direct Debit, access, tariff, security…) are labelled **escalate**; record checks, requests to automated services and messages to the customer are **act**.
- Unsafe moves can be caught by fixed rules, without a model judging them.

## Results and known limitations

Measured with `src/evaluate.py` (Claude judge plus case rubrics):

- **Latest `main`, 100 cases drawn at random** from the 101 test cut-offs and 707 synthetic stress cases: **90/100**, 0 critical failures, 0 crashes. On synthetic cases we had iterated on: 39/40. **On synthetic cases never evaluated before: 41/49 (84%)**, the best guide to unseen cases.
- Earlier full runs, one iteration back: 101 test cut-offs 89/101 (simulated bank); 340 synthetic cases 318/340 (no bank).

Known limitations:

- **No live data in the Reality Test:** without tool results, the agent can take at most one result-dependent step. It moves the case forward with what the case shows instead of reporting results it can't see.
- **Routing:** it sometimes picks the wrong team (e.g. the security team instead of the Access team), or misses a second step the gold expects (register the dispute as well as blocking the card).
- **More escalation than the gold labels:** many gold `act` cases come out `escalate` (a hand-off to a team). Judges mostly accept it, but it's a systematic difference.
- **Message accuracy is enforced by the prompt, not checked:** claims in a message aren't verified against tool results (runtime-fault gaps I723 and I724 in `src/agent/test_runtime_faults.py`). Occasional overclaims remain.
- **The guard is regex-based:** it can misfire. For example, it reads a quoted contract clause ("we will refund within 1 business day") as a refund promise, so the agent may avoid quoting it.
- **Evaluation:** the judge, the synthetic cases and many gold answers were written with Claude; results vary between runs; the gold convention for act and escalate changed during the day.
- **Cost and speed:** about $0.15 and 30–60 seconds per case at effort `high`, parallel across cases.

## What we'd build next

- A routing table for internal teams (which team handles what), in the tool description and checked by the guard.
- A history-based adapter: seed records from the bank's own messages in the visible history, so lookups on unseen cases return facts the case already shows.
- A deterministic check of message claims against tool results and case events (closing I724).
- Real tool adapters for a bank's systems, behind the same four tool shapes.
- Human review in the UI: approve or edit a step before it's executed, with the handover pre-filled.

## Project Setup

You need [uv](https://docs.astral.sh/uv/), Node.js 20.19+ or 22.12+, and Docker (for MongoDB).

### 1. Environment and database

```bash
cp .env.example .env
```

Put your `ANTHROPIC_API_KEY` in `.env`. The MongoDB defaults (`MONGODB_URI`, `MONGODB_DB`) match the compose file.

```bash
docker compose up -d
```

### 2. Backend (`src/`)

From the repo root:

```bash
uv sync
```

```bash
uv run fastapi dev src/main.py
```

The API runs on http://localhost:8000. Interactive docs are at http://localhost:8000/docs.

### 3. UI (`web/`)

In a second terminal:

```bash
cd web
npm install
```

```bash
npm run dev
```

Open http://localhost:5173. The dev server proxies `/api/*` to the backend on port 8000, so start the backend first.

## Command

Backend, from the repo root:

```bash
uv run fastapi dev src/main.py                     # API on :8000
uv run -m src.run cases/full --out ANSWERS/        # batch CLI: ANSWER.md, REASONING.md, trace.jsonl per case; --workers N (default 4)
uv run -m src.run reality_test/ --out ANSWERS/ --workers 10   # unseen cases (index.md, history.md, attachments/ per folder)
uv run -m src.agent.test_core                      # loader, guard, agent loop; no API key or MongoDB
uv run -m src.agent.test_runtime_faults --report   # model/tool/runner fault scenarios, PASS/GAP each
uv run -m src.bank_env.test_bank_env               # fixtures, adapter, overlays, faults; no API key or MongoDB
uv run -m src.repository.test_repository           # needs MongoDB running
uv run --with pytest pytest src/                   # API; upload and session tests need MongoDB running
uv run -m src.evaluate                             # dev loop: run every cases/test cut-off, Claude judges each; scorecard in eval_out/
uv run -m src.evaluate 017-event-004 --mock        # one cut-off (or case ids like 001 017), against the tool stubs
```

UI, from `web/`:

```bash
npm run dev       # UI on :5173
npm run build     # type-check and production build
npm run lint      # oxlint
npm run gen:api   # regenerate src/api/schema.d.ts after changing src/openapi.yaml
```

## Reference

- [PRODUCT.md](PRODUCT.md)
- [API spec (src/openapi.yaml)](src/openapi.yaml), also served at http://localhost:8000/docs
- [.env.example](.env.example)
