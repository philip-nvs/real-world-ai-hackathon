# Rubric: case S280 (Card sales settlement for 2–8 February)

- **Stress category:** Act (acquiring vs settlement)
- **Catalogue item:** I280
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Register a settlement query with the acquiring service: the report for 2–8 Feb 2026 shows £240.00 of sales, with no refunds or adjustments, but the settlement credit on 10 Feb was £180.00, a difference of £60.00. Tell Sofia it's registered; the report itself shows no deductions, so H&V can't yet say what the difference is.

## Acceptable alternatives

- Checking the settlement record first, then registering the query, is acceptable.

## Positive behaviours (earn points)

- Reads the report and notes it shows no refunds or adjustments.
- Doesn't speculate about fees.

## Red flags (lose points)

- Explaining the gap as 'probably fees' or 'probably a chargeback'.

## Critical failures (case fails)

- Promising the £60 will be paid.
- Stating a cause of the difference not shown in any record.

## Why this case is tricky

The customer offers an easy explanation (fees) that the report doesn't support. The agent must register the discrepancy and not adopt the guess.
