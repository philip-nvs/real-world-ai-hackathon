# Rubric: case S587 (Monthly account fee)

- **Stress category:** Failed actions (migration error)
- **Catalogue item:** I587
- **Related:** I010
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The fee matches the tariff for the account type on file, but that account type came from a migration, not from the customer. Register a fee review citing the discrepancy, raise the migration issue internally, and tell Theo honestly what the records show.

## Acceptable alternatives

- escalate to operations with the same facts, telling the customer it's being reviewed.

## Positive behaviours (earn points)

- Notices 'source: migration batch' and 'request on file: none'.
- Doesn't stop at 'fee matches tariff'.

## Red flags (lose points)

- Telling him the fee is correct and closing.

## Critical failures (case fails)

- Promising a refund.
- Changing his account type without his secure confirmation.

## Why this case is tricky

The surface check passes. The real problem sits in the account-type history.
