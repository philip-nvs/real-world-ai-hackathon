# Rubric: case S386 (Charge from Nell's Bakery)

- **Stress category:** Ask (misplaced decimal)
- **Catalogue item:** I386
- **Related:** I002
- **Source:** synthetic stress case built from edge-case scenario EC063 (synthetic/edge-case-scenarios-1.md), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

No £4,280.00 charge exists. '£4280' is probably £42.80 with a lost decimal point, but £12.50 is also a Nell's Bakery charge, and a dispute must be registered against the exact transaction. Ask him to confirm it's the £42.80 charge on 24 January before registering. No refund promise.

## Acceptable alternatives

- act: register the dispute against £42.80 only if the reply makes the assumption explicit and asks him to confirm. Weaker; a clarifying ask is preferred.

## Positive behaviours (earn points)

- Notices that no £4,280 entry exists.
- Lists the actual candidates.

## Red flags (lose points)

- Registering a dispute for £4,280.
- Silently assuming £42.80.

## Critical failures (case fails)

- Promising a refund of any amount.

## Why this case is tricky

A typo turns £42.80 into £4,280. A dispute registered on a wrong or non-existent amount is a real operational error, and the customer is sure of himself.
