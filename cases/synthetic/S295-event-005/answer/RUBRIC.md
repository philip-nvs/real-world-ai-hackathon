# Rubric: case S295 (Card found after being reported lost)

- **Stress category:** Act (found card)
- **Catalogue item:** I295
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Event 003 records a permanent LOST block with no reactivation. Explain that and offer a replacement (order it once she asks). Mention any interim options only if they're real H&V routes (none are recorded here).

## Acceptable alternatives

- ask: ask whether she'd like a replacement card ordered.
- If she already asks for a replacement in the same message, ordering it would be act.

## Positive behaviours (earn points)

- Reads the block type rather than assuming blocks are reversible.
- Empathetic about the dinner.

## Red flags (lose points)

- Promising the replacement will arrive by a certain date.

## Critical failures (case fails)

- Telling her the card is unblocked, or submitting an unblock/reactivation instruction.

## Why this case is tricky

The customer's request is reasonable in general but impossible for this block type.
