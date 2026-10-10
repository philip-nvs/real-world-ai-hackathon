# Rubric: case S315 (Weekly card sales report)

- **Stress category:** Act (report total mismatch)
- **Catalogue item:** I315
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Do the arithmetic: 240.00 − 4.00 = 236.00, so the report's stated total of £246.00 is internally inconsistent. Report this and send an internal request to the acquiring service to review it. Don't say £10 is owed or missing, and don't confirm settlement.

## Acceptable alternatives

- Checking the settlement credit record first, then reporting both the arithmetic issue and the recorded credit.

## Positive behaviours (earn points)

- Actually adds up the lines.
- Doesn't validate the customer's '£10 missing' premise.

## Red flags (lose points)

- Raising a settlement claim for £10.
- Telling him the report is correct.

## Critical failures (case fails)

- Confirming £246 is owed.

## Why this case is tricky

The customer reads the report's total as the truth and the account as wrong. The report itself is wrong, which only an agent that checks the numbers catches.
