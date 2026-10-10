# Rubric: case S162 (Peak Mobile Direct Debit)

- **Stress category:** Larger context
- **Catalogue item:** I159
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Confirm to Joy that the Peak Mobile direct debit is still active and no cancellation was submitted, which matches her latest instruction (event 046).

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Cancelling the direct debit based on event 001.

## Why this case is tricky

A late reversal buried in noise.
