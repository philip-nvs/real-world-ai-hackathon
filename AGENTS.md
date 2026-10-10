# Agents

## Structure

- `src/`: FastAPI backend. `main.py` is the app; run everything from the repo root.
- `src/agent/`: the case agent (loader, policy guard, agent loop, answer writer), API sessions, and the tool stubs used when a case has no fixture.
- `src/bank_env/`: simulated bank for public cases. `fixtures/NNN.json` serves cases `NNN` and `NNN-event-KKK`; `overlays/` add conflicts and faults; `extract.py` builds fixtures with Claude.
- `src/repository/`: MongoDB connection.
- `src/evaluate.py`: dev loop that runs the agent on `cases/test/` and has Claude judge each step against the gold one; writes `eval_out/`.
- `src/openapi.yaml`: hand-written API spec; the UI's types are generated from it.
- `web/`: React UI (Vite, TanStack Router and Query, shadcn on Base UI, Tailwind).
- `web/src/api/`: typed API client; `schema.d.ts` is generated.
- `cases/full/`: public cases. `cases/test/`: public cases cut off at an event, with the gold step in `answer/`. `cases/synthetic/`: stress cases.
- `test_*.py`: plain-`assert` scripts run as modules, except `src/test_main.py`, which is pytest.

## Rule

- Import Python as `src.…`; don't add modules at the repo root.
- When you change a route in `src/main.py`, update `src/openapi.yaml` to match (`src/test_main.py` fails otherwise), then run `npm run gen:api` in `web/`.
- Don't hand-edit `web/src/api/schema.d.ts` or `web/src/routeTree.gen.ts`; both are generated.
- Call the backend from the UI through `api` in `web/src/api/client.ts`; use raw `fetch` only for file downloads.
- Keep the policy guard in plain code; never call a model from it.
- Keep the tool names and arguments in `src/agent/tools.py` identical to `FixtureAdapter.tools()` in `src/bank_env/`.
- Tool stubs record a step and return no result; never make them invent data, references or delivery.
- Keep the loader reading only `index.md`, `history.md` and `attachments/`; a case's `answer/` holds the gold step and must never reach the agent.
- Add Python dependencies with `uv add` and JS ones with `npm install` in `web/`.

## Reference

- [README.md](README.md): setup and commands
- [PRODUCT.md](PRODUCT.md): what the product does and why
- [src/openapi.yaml](src/openapi.yaml): API spec
