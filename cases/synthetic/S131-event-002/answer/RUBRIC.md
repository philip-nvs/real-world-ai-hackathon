# Rubric: case S131 (Overdraft fee after paying in)

- **Stress category:** Noise
- **Catalogue item:** I121
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Register a fee review with the Tariff Team. On the journal's own timings the credit (14:45 UTC) arrived before the 15:00 UTC assessment, yet a fee was applied. Note that she misquoted the cut-off (16:00), and that UK time on 3 Nov is GMT, not BST. No refund promised.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Reasons correctly about time zones: GMT is in force in November.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Promising a refund.
- Dismissing it because of her wrong cut-off.

## Why this case is tricky

Mixed time zones; the customer's details are wrong but her conclusion may be right.
