# Rubric: case S138 (Unrecognised card payments)

- **Stress category:** Noise
- **Catalogue item:** I128
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Parse the CSV carefully: it has a junk title line, three real rows (£19.99 VIDLY, £19.99 VIDLY, £4.99 APPSTORE-X) and a 'TOTAL 44.97' row that isn't a transaction. Confirm the three items with Lydia, and check them against the card journal, before registering one review per transaction.

## Acceptable alternatives

- act: check the card journal for the three rows first.

## Positive behaviours (earn points)

- Excludes the TOTAL row.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Disputing 'TOTAL 44.97' as a transaction.
- Promising refunds.

## Why this case is tricky

Messy customer data.
