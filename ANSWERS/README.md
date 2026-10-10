# Reality Test answers: Banking & Financial Services

Track: **Banking & Financial Services**. One folder per case, named after the case number (`001/` to `030/`), from [DwellyOrg/HackatonChallenges](https://github.com/DwellyOrg/HackatonChallenges) `Banking & Financial Services/`.

## How these were produced

Unedited system output, generated once at 16:40 BST with the code frozen at 16:30 (last change to `src/`: `fdb6e4e`):

```bash
uv run -m src.run "HackatonChallenges/Banking & Financial Services" --out ANSWERS/ --workers 10
```

Model: Claude Opus 5.5 (`claude-opus-5-5`), adaptive thinking, effort `high`. No live bank systems were connected, so every tool call is **recorded as the bank's next step and not executed**; each `ANSWER.md` marks such actions "(recorded, not executed)".

Run summary: 30 cases, act 12, ask 2, wait 0, escalate 16, crashed 0, policy-guard blocks 22.

## Each folder

- `ANSWER.md`: what the system received (its own summary), what it did, the decision and next action, what was escalated with the handover, what failed (including policy-guard blocks), the final result, and the message to the customer.
- `REASONING.md`: evidence with event IDs, conflicts between events, options rejected and policy-guard blocks.
- `trace.jsonl`: every model turn, tool call, tool result, guard block and the final decision.

## Known issues in this run

Found when the cases arrived, after the code freeze, and left unfixed so the answers come from the submitted system:

- **Cases 021–030 load with 0 events.** Their event headers read `event 001 (E01)`, and the loader's event pattern doesn't allow the `(E01)` suffix. The agent still read the full history, but the policy guard saw no events. It rejected each first decision that cited event IDs (10 blocks, one per case) and any instruction citing an event (2 blocks). The agent re-planned and finished every case; these answers cite events less and execute no instructions.
- **New channel names** ("Phone (personal banking)", "In-app chat", "Authenticated customer chat"…) aren't in the guard's list of channels that can carry a confirmation (verified call, secure portal, business portal). Two instructions confirmed by phone were blocked (cases with a "came by 'Phone (personal banking)'" block), so the agent asked or escalated instead.

The other 10 guard blocks were the guard working as intended: 3 guarantees, 3 suggestions to pay again and 2 refund promises were stopped before reaching the customer, and 2 instructions cited events that don't exist.
