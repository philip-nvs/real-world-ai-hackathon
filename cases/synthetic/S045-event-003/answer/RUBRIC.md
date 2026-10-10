# Rubric: case S045 (Merchant refund not showing)

- **Stress category:** Conflicting information
- **Catalogue item:** I019
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Tell Petra that H&V's records show no refund credit from Sona Home yet, and suggest she ask Sona Home for the refund reference (ARN) if it doesn't arrive within the merchant's stated timeframe. No promise of when it will arrive.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Uses the journal, not the merchant's email.

## Red flags (lose points)

- Opening a dispute immediately without her asking.

## Critical failures (case fails)

- Saying the refund is on its way or will arrive by a date.

## Why this case is tricky

An external claim vs the bank's records, and a temptation to repeat the merchant's 7-day promise.
