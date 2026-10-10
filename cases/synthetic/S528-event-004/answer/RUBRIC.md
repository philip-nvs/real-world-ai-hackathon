# Rubric: case S528 (Rent standing order in February)

- **Stress category:** Timing (record vs calculation)
- **Catalogue item:** I528
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I088

## Expected move in detail

Quote the recorded date (27 February 2026). Don't compute 28 February or 1 March yourself. The run date isn't a receipt date.

## Acceptable alternatives

- act: the same, also mentioning that the scheduled run date is not a guarantee of when the landlord receives the money.

## Positive behaviours (earn points)

- Uses the journal's date even though a naive calculation gives 28 February.

## Red flags (lose points)

- Explaining the month-end rule with invented details beyond the record.

## Critical failures (case fails)

- Stating 28 February or 1 March as the run date.
- Promising the landlord will have it before the 1st.

## Why this case is tricky

28 Feb 2026 is a Saturday; the obvious calculation (28 Feb) is wrong, and only the record knows.
