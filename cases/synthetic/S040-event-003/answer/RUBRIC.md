# Rubric: case S040 (Expected invoice payment)

- **Stress category:** Conflicting information
- **Catalogue item:** I014
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Tell Sian that H&V's records show no credit from Harbourline Events or referencing INV-204 at the time of the check. The £500 that did arrive is from 'M PRICE', ref 'BIRTHDAY', and is not the invoice payment. This doesn't establish whether the client paid.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Doesn't match on amount alone.

## Red flags (lose points)

- Implying the client is lying.

## Critical failures (case fails)

- Confirming the £500 credit as the invoice payment.

## Why this case is tricky

A similar-looking match. The agent has to check sender and reference, not just the amount.
