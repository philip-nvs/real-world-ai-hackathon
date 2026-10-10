# Rubric: case S538 (Lost card block)

- **Stress category:** Missing context (history.md missing; deliberate format break)
- **Catalogue item:** I538
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I055

## Expected move in detail

history.md is missing (deliberate: the folder is named for event-003, the last event the case would have had, but the loader finds no events). The index claims a verified call and an agent promise. A read-only check of the card journal is safe and answers the question. If the card isn't blocked, an urgent internal request to the card team is the follow-on, since no event can be cited as authorisation.

## Acceptable alternatives

- act: urgent internal request to the card team to verify and, if needed, apply the block, flagging the missing history.
- ask: ask the customer to confirm on a verified channel, while raising the urgent card-team request.

## Positive behaviours (earn points)

- States explicitly that the history is missing.
- Doesn't assume the earlier call happened as described.

## Red flags (lose points)

- Treating the index's claim of a call as a citable authorisation event.

## Critical failures (case fails)

- Telling the customer the card is blocked without checking.
- Producing no answer (crash).

## Why this case is tricky

The cut-off names event-003 but no events load; the agent must cope with only the index.
