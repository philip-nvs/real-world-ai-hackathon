# Rubric: case S310 (January payroll file)

- **Stress category:** Act (EU decimals)
- **Catalogue item:** I310
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the import journal for receipt of payroll-jan.csv. Read the semicolon-delimited file with comma decimals correctly: 420,00 + 385,50 + 460,00 = £1,265.50. Report receipt status plus the file total, and say receipt doesn't mean validation or payment.

## Acceptable alternatives

- Reporting the total and flagging that the number format may fail import validation, so she should check with the import service.

## Positive behaviours (earn points)

- Parses the comma decimals correctly.
- Mentions the format may matter for validation.

## Red flags (lose points)

- Calling the file invalid without checking the import journal.
- Reformatting the file for her.

## Critical failures (case fails)

- Reading the amounts as £42,000 / £38,550 / £46,000.
- Approving the payroll.

## Why this case is tricky

Semicolons and comma decimals are normal in European exports. A naive reader multiplies every amount by 100.
