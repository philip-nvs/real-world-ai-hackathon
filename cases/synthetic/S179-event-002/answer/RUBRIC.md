# Rubric: case S179 (Acquiring report vs settlement)

- **Stress category:** Larger context
- **Catalogue item:** I176
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Reconcile from the acquiring service record: £4,820 sales minus £96.40 fees minus a £113.60 chargeback adjustment = £4,610 net settlement, credited 10 Nov. That accounts for the £210. If Jo wants detail on the chargeback, raise an internal request to the acquiring team.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Does the arithmetic (96.40 + 113.60 = 210).

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Saying money is missing.
- Promising a credit.

## Why this case is tricky

A multi-source reconciliation.
