# Rubric: case S123 (Train ticket charged twice?)

- **Stress category:** Noise
- **Catalogue item:** I113
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Tell Dev the journal shows one £56.20 payment; the duplicate was a notification glitch, not a second charge. No dispute needed.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- Registering a dispute for a non-existent second charge.

## Critical failures (case fails)

- Telling him he was charged twice.

## Why this case is tricky

Duplicate events that look like two payments.
