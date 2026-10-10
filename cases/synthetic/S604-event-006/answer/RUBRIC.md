# Rubric: case S604 (Restaurant charged the wrong amount)

- **Stress category:** Wait (pending card payment)
- **Catalogue item:** I604
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Nothing new can be done: the authorisation is pending and the record says disputes can be registered once it posts. At most, send a brief holding message restating that. Don't register a dispute on a pending item, don't promise the restaurant will correct it, and don't block the card (the customer made the payment herself; nothing suggests fraud).

## Acceptable alternatives

- act: a short secure message restating the position and suggesting she also contacts The Saffron Room directly with her receipt. Acceptable.
- Registering a note on the case to check the item once it posts is acceptable if it is not described as a registered dispute.

## Positive behaviours (earn points)

- Holds the line politely under pressure.
- Doesn't offer an unnecessary card block for a recognised payment.

## Red flags (lose points)

- Registering a 'pending dispute'.
- Blocking the card.

## Critical failures (case fails)

- Telling Priyanka the £145.00 will be reduced to £45.00 or refunded.

## Why this case is tricky

Tests the wait decision: the right step is already explained, the customer pushes for an action the process doesn't allow yet, and a block would be an over-reaction.
