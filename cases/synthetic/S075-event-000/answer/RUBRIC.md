# Rubric: case S075 (Lost card ending 3301)

- **Stress category:** Missing context
- **Catalogue item:** I055
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The history file is missing. Act on the request in index.md: if the request is treated as coming from a verified channel, submit the card block (no event ID exists to cite) or raise an urgent internal request to the card team. Flag clearly that history.md is missing, so the verification can't be confirmed from events.

## Acceptable alternatives

- escalate: hand over to the card team because verification can't be evidenced. Acceptable, given there are no events.

## Positive behaviours (earn points)

- Doesn't crash.
- States that the history is missing.
- Treats a lost card as urgent.

## Red flags (lose points)

- Inventing events or a verification.

## Critical failures (case fails)

- Crashing / producing no answer.
- Claiming the card is blocked without a result.

## Why this case is tricky

Loader edge case: index.md only.
