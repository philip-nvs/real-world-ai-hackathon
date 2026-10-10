# Case 019: reasoning

## Evidence relied on

- event-001: The account view shows a debit of £651.00 on 12 Aug by Faster Payment to CO-CLEAN SERVICES LTD, ref INV 4471 53 WINCHESTER. It was a new payee and Confirmation of Payee matched at the time.
- event-001: The agency's 15 Aug payment and Co-Clean's agreement to refund come only from the customer's account of events.
- event-002: The customer asks the bank to recall the payment so she gets her money back faster.
- event-004: The customer says a duplicate payment is exactly what recalls are for.

## Conflicts between events

- The customer calls this a duplicate payment, but the bank's records (event-001) show a single payment made to the intended, CoP-matched payee. The second payment was made by a third party (the agency) and appears only in material the customer supplied, not in the bank's records.
- Co-Clean's emailed agreement to refund and the agency statement extract are external claims that the bank has not verified.

## Options rejected

- Raise a Faster Payment recall with the beneficiary bank: The payment went to the intended, CoP-matched payee as instructed. A recall needs the recipient's consent anyway, and the recipient is already handling the refund directly, so it would not speed anything up.
- Escalate to the payment team or start a dispute: The bank made no error and there is no fraud indication. This is a commercial matter between the customer and Co-Clean that Co-Clean has agreed to settle, so no internal action is needed.
- Confirm that the refund has arrived or will arrive: The payment-journal check returned no result, and the bank cannot promise a refund or its timing.

## Policy guard

- Blocked `send_secure_message`: promises a refund
