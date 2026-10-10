# real-world-ai-hackathon

## Overview

Nevis' case agent for the Banking & Financial Services track of Dwelly's Real-world Agents hackathon: a FastAPI backend (`src/`) and a React UI (`web/`). Why it exists and what it does: [PRODUCT.md](PRODUCT.md).

## Launch posts

- LinkedIn: https://lnkd.in/p/efNuAtMV
- X: https://x.com/xylankant/status/2108940085068702192

## Demo video
- Screen Recording 2026-10-10 162027.zip

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
