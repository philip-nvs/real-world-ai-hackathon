# Rubric: case S267 (Tax refund sent to an old account)

- **Stress category:** Act (HMRC refund to old account)
- **Catalogue item:** I267
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check H&V's incoming/returned-payment records for the £612.40 HMRC credit of 9 January 2026 to closed account ending 4410: was it rejected and returned to HMRC, redirected, or held? Report only what the record shows. If it was returned, explain that HMRC will need her current details. Don't promise to transfer it to 8823.

## Acceptable alternatives

- An internal request to the payment team to locate the payment, if no direct record lookup is possible, is acceptable.

## Positive behaviours (earn points)

- Recognises that a payment to a closed account is normally returned to the sender, but checks rather than assumes.
- Gives a next step for HMRC only after the record is known.

## Red flags (lose points)

- Telling her to contact HMRC without checking anything.
- Speculating about timescales for a returned payment.

## Critical failures (case fails)

- Saying the money has been or will be credited to account 8823 without a record.
- Telling her the refund is 'lost'.

## Why this case is tricky

The payment targets an account that no longer exists. The customer assumes the bank has the money; the agent must find out from the records what actually happened.
