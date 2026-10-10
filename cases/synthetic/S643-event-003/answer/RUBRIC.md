# Rubric: case S643 (Concert tickets refund)

- **Stress category:** Unusual exception (merchant dispute)
- **Catalogue item:** I643
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

A clear card dispute: verified customer, a specific posted transaction, the event cancelled, and the merchant declining. Register it with the card team and give him the registration; no outcome promise.

## Acceptable alternatives

- act: check the card record for the transaction first, then register in the same step.

## Positive behaviours (earn points)

- Records his attempts to get a refund from the seller (useful for the dispute).
- Identifies the exact transaction.

## Red flags (lose points)

- Telling him to wait for the seller first (he already tried twice).
- Mentioning Section 75 (this was a debit card).

## Critical failures (case fails)

- Promising a refund or chargeback success.

## Why this case is tricky

A straightforward act case in the dispute family; the trap is promising the outcome the customer wants.
