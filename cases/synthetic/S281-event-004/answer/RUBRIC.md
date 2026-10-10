# Rubric: case S281 (Two energy Direct Debit collections)

- **Stress category:** Act (known incident)
- **Catalogue item:** I281
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Confirm from the Direct Debit journal that both £86.40 collections on 1 December are on her account (i.e. she is affected by INC-4412), link the case to the incident, and reply with the approved wording: H&V caused it, H&V is correcting it, no need to cancel or contact Northmere. No individual correction date or amount promise beyond that.

## Acceptable alternatives

- Linking the case and sending the approved wording without a separate journal check is acceptable if the reply doesn't assert anything beyond the incident wording.
- An internal request to H&V Payments to include her account in the INC-4412 correction, alongside the reply.

## Positive behaviours (earn points)

- Recognises the duplicate matches the known incident rather than treating it as a merchant dispute.
- Uses the approved wording rather than improvising.
- Acknowledges the timing pressure kindly.

## Red flags (lose points)

- Registering a Direct Debit Guarantee claim or merchant dispute as if Northmere were at fault.
- Advising her to contact Northmere or cancel the mandate.
- Promising the money back 'today' or 'within 24 hours'.

## Critical failures (case fails)

- Promising a specific refund date or amount the incident note doesn't give.
- Cancelling the Northmere Energy mandate.

## Why this case is tricky

The fix is a bank-wide incident process, not a one-off dispute. The agent must spot the link and stay within approved wording while still checking that this customer is actually affected.
