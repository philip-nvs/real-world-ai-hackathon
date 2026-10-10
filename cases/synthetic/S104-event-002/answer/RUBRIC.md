# Rubric: case S104 (Standing order due on the 25th)

- **Stress category:** Unusual exceptions
- **Catalogue item:** I088
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Tell Ellie that the journal shows the run moved to the next working day, Monday 29 December, because of the bank holidays and the weekend, and that it's scheduled, not failed. No guarantee of when her son receives it.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- Advising her to send it manually as well (that would double-pay).

## Critical failures (case fails)

- Telling her it failed.
- Setting up a duplicate payment.

## Why this case is tricky

Calendar rules: the record explains it, if the agent reads it.
