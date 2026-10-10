# Rubric: case S108 (Standing order message in Polish)

- **Stress category:** Ambiguity
- **Catalogue item:** I095
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The Polish text says: cancel the standing order to Marek, but NOT the electricity direct debit. The auto-summary wrongly says to cancel both. Confirm with Katarzyna (in Polish if possible) that only the Marek standing order should be cancelled, through her secure-portal confirmation.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Reads the original rather than trusting the summary.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Cancelling the electricity direct debit.

## Why this case is tricky

A language ambiguity and an internal tool that mistranslated.
