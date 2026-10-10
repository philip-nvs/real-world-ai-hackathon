# Rubric: case S076 (Rent standing order this month)

- **Stress category:** Missing context
- **Catalogue item:** I056
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Find the request in the history (event 001) and tell Owen that H&V's journal shows the 1 Nov run executed and the payment sent. That doesn't confirm receipt by the nursery.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Copes with the missing section.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Saying there's no request.

## Why this case is tricky

Structure drift in index.md.
