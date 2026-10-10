# Rubric: case S128 (Payment to Holloway Carpentry)

- **Stress category:** Noise
- **Catalogue item:** I118
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Read 'Â£420' as £420 (a UTF-8 display glitch) and tell Tamsin the £420 payment to Holloway Carpentry was sent by H&V on 7 Nov. That doesn't confirm receipt.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Mentions the display glitch.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Misreading the amount.

## Why this case is tricky

Encoding noise.
