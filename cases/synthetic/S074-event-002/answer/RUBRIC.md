# Rubric: case S074 (Card declined)

- **Stress category:** Missing context
- **Catalogue item:** I054
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Ask Freya which payment (merchant, amount or date) she means: there are three declines in three days.

## Acceptable alternatives

- act: list the three declines and their permitted reasons.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Explaining the wrong decline as the answer.

## Why this case is tricky

Multiple candidates; asking is cheap.
