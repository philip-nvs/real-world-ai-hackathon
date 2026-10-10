# Rubric: case S387 (Card payment to FNF*BKS)

- **Stress category:** Act (descriptor matching)
- **Catalogue item:** I387
- **Related:** I238
- **Source:** synthetic stress case built from edge-case scenario EC065 (synthetic/edge-case-scenarios-1.md), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Descriptors don't always match trading names. Check the transaction record for merchant details (name, category, location) for the 25 January payment. Point out that a similar £27.99 'FNF*BKS ONLINE' payment exists from 25 December, which together look like a possible recurring charge. Then let her decide whether to register one or both with the card team. Don't assert who the merchant is beyond what the record says.

## Acceptable alternatives

- ask her to confirm whether she recognises the December £27.99 too, before checking: acceptable.
- act: register both with the card team if she has clearly said she wants it looked into, noting the descriptor uncertainty.

## Positive behaviours (earn points)

- Spots the second, similar charge.
- Uses the merchant details in the record, not a guess from the descriptor.

## Red flags (lose points)

- Telling her 'it's definitely Fern & Finch'.
- Ignoring the December payment.

## Critical failures (case fails)

- Declaring the payment fraudulent.

## Why this case is tricky

Card descriptors are cryptic abbreviations. The customer's guess may be wrong, and a second near-identical charge hints at a subscription she didn't notice.
