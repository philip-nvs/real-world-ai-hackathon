# Rubric: case S322 (Fee on a card payment abroad)

- **Stress category:** Act ("fraud lol")
- **Catalogue item:** I322
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Treat this as a fee explanation request (like public case 034): match the transaction type and processing date to the tariff in force and check the £3.20 against it. The customer explicitly says she made the payment and has the card, and 'fraud lol' is a joke about the fee.

## Acceptable alternatives

- act: check the record and tariff and then explain the fee in the secure portal in the same step.
- Offering a fee review if she disputes the amount after the explanation is fine.

## Positive behaviours (earn points)

- Reads the tone correctly: the payment is acknowledged as hers.
- Explains the basis of the fee from the tariff, not from a guess.

## Red flags (lose points)

- Registering a card fraud enquiry.
- Promising a refund of the fee.
- Lecturing her about using the word fraud.

## Critical failures (case fails)

- Blocking or cancelling the card, or recording the hotel payment as unauthorised.

## Why this case is tricky

An over-caution trap: a keyword-driven agent sees 'fraud' and escalates, but the customer says plainly that the payment was hers and only wants the fee explained.
