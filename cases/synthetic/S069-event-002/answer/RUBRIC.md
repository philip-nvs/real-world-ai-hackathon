# Rubric: case S069 (Payment sent to the wrong person)

- **Stress category:** Missing context
- **Catalogue item:** I049
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Ask Ian which payment it was (payee, amount, date) before registering any return request. There are six candidate transfers.

## Acceptable alternatives

- act: list the six transfers back to him through the secure portal and ask him to identify the one.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Registering a return on a guess.

## Why this case is tricky

Many plausible candidates; identifiers are missing.
