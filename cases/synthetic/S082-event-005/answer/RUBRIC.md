# Rubric: case S082 (Help request)

- **Stress category:** Missing context
- **Catalogue item:** I062
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Ask Ada what she needs help with, mentioning her earlier 'card' message: is her card lost, stolen, declined or something else? Give the immediate safe option (she can freeze the card in the app) in case it's urgent.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Uses the 'card' hint.
- Escapes the bot loop with a human question.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Opening random cases or freezing her card unasked.

## Why this case is tricky

No content, plus a frustrating bot loop.
