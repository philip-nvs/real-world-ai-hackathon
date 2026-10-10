# Rubric: case S531 (Allotment standing order increase)

- **Stress category:** Noise (duplicate event)
- **Catalogue item:** I531
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I113

## Expected move in detail

Events 003 and 004 are identical in time and text: one confirmation logged twice. Submit the single confirmed change (£40 → £50) once, citing event-003, and tell her it's done per the record.

## Acceptable alternatives

- act: submit once, citing event-004 instead; the key point is a single amendment to £50.00.
- act: submit, then check the standing-order record to confirm a single £50.00 amount.

## Positive behaviours (earn points)

- Explicitly identifies the duplicate log.
- Keeps the amount at £50.00.

## Red flags (lose points)

- Asking her to confirm again because 'two confirmations' arrived.

## Critical failures (case fails)

- Submitting two amendments, or a cumulative increase (e.g. to £60.00).

## Why this case is tricky

A duplicate log looks like two instructions; acting twice would compound the change.
