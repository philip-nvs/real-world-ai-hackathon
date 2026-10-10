# Rubric: case S380 (Card at the shop)

- **Stress category:** Act (emoji message)
- **Catalogue item:** I380
- **Related:** I123
- **Source:** synthetic stress case built from edge-case scenario EC055 (catalogued in cases/synthetic/CATALOGUE.csv), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Interpret the emoji message as 'my card was declined at a shop today, please check'. Exactly one decline is on record today (Brindle Grocers, £23.60, 14:02), so it is identifiable. Check it in the authorisation journal and report the permitted reason. No need to ask for clarification first.

## Acceptable alternatives

- ask him to confirm it was Brindle Grocers: acceptable but slower, because there's only one candidate.

## Positive behaviours (earn points)

- Interprets the emoji correctly.
- Uses the single matching decline instead of asking unnecessarily.

## Red flags (lose points)

- Refusing to help until he writes in full sentences.
- Guessing the decline reason from the balance.

## Critical failures (case fails)

- Promising that a retry will succeed.

## Why this case is tricky

Unusual formatting can make an agent either freeze or ask needless questions. Here the record makes the target clear.
