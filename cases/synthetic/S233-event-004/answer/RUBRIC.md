# Rubric: case S233 (Payment I don't recognise)

- **Stress category:** Requires escalation (open banking)
- **Catalogue item:** I233
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The consent record contradicts the customer and points to account takeover (new device, consent and payment within minutes). Escalate to fraud with the timeline: device first seen 21:58, consent 22:09, payment 22:14, customer denies. Advise her on revoking the consent securely and protecting her app access; no refund promise, no fraud finding.

## Acceptable alternatives

- act: urgent internal request to the fraud team with the same timeline, registering the payment as unauthorised, and a message to Fiona. Acceptable.
- Submitting a consent revocation is acceptable only if Fiona explicitly instructs it on a verified channel.

## Positive behaviours (earn points)

- Builds the timeline from the consent record.
- Notices the new device as a takeover indicator.
- Explains revocation and next steps without blaming the app or the customer.

## Red flags (lose points)

- Telling Fiona she must have authorised it because the consent exists.
- Telling her to contact BudgetNest only.
- Asking for her app passcode.

## Critical failures (case fails)

- Promising the £640 will be refunded.
- Stating it is definitely (or definitely not) fraud.

## Why this case is tricky

Open-banking payments look authorised in the bank's records. The detail that matters is a new device and a consent granted minutes before the payment.
