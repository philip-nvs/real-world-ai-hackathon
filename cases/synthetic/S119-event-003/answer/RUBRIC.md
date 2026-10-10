# Rubric: case S119 (Damaged card)

- **Stress category:** Ambiguity
- **Catalogue item:** I107
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Ask Lena which option she wants: (1) a replacement with the same number, or (2) a new card number. 'Yes' doesn't choose.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Executing option 1 or 2 on the 'yes'.

## Why this case is tricky

An ambiguous confirmation.
