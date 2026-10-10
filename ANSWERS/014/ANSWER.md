# Case 014: ESCALATE

## What the system received

The customer was charged twice (£634.00 each) for a holding deposit at a letting agency and wants a chargeback on the second payment right away. He doesn't want to wait for the refund the agency promised in an email he forwarded.

4 events; attachments: agency_refund_email.eml, card_transactions.csv.

## What the system did

- `check_record` → card journal: Case 014, Tomás Ribeiro personal debit card: status of the two PAYGATE*NORTHGATE LET transactions of £634.00 on 11 Sep 2026 (auth codes A71C02 and A71C09), and any refund, credit or pending refund authorisation from PAYGATE*NORTHGATE LET since 11 Sep 2026. (recorded, not executed)
- `submit_internal_request` → Card disputes team: Case 014, customer Tomás Ribeiro (personal current account, debit card). In secure in-app chat on 2026-09-16 (event-002, event-004) the customer asked for a chargeback on the second of two £634.00 payments to PAYGATE*NORTHGATE LET on 11 Sep 2026 (18:02 auth A71C02 and 18:04 auth A71C09, both shown in the internal account view, event-001; the customer's CSV shows both settled 13 Sep). He says he clicked the agency's payment link twice after a 'page not responding' message. He forwarded an email from the agency dated 14 Sep 2026 (not verified by the bank) acknowledging the duplicate and promising to refund one payment to the card within 5-10 working days. He needs the money for the full deposit and does not want to wait. Please review whether a duplicate-processing dispute can be raised on the 18:04 payment (A71C09) now, given the merchant's promised refund and the risk of a double credit. Note: a card-journal check for any refund or pending credit from the merchant was recorded but could not be executed (no live system connected), so whether a refund has already arrived is unconfirmed. Please decide and contact the customer with the outcome. (recorded, not executed)
- `send_secure_message` → Tomás Ribeiro: Dear Mr Ribeiro,

Thank you for getting in touch about the two £634.00 card payments to PAYGATE*NORTHGATE LET on 11 September (18:02 and 18:04). I can see both payments on your account, and I understand you need this money for the full deposit.

We have asked our card disputes team to look at raising a chargeback on the second payment (18:04). Please be aware of a few things:
- This is a request for review. It is not a decision yet, and I can't promise that a chargeback will be raised or will succeed, or say how long it will take.
- A chargeback is not usually a quick process. You have told us the agency has said in an email that they will return one payment. The bank hasn't verified that email and can't confirm whether or when any money will come back from the agency. If money from the agency comes back while a chargeback is open, the team may have to adjust the chargeback so the same amount isn't credited twice.
- I haven't been able to confirm from our card records whether any credit from the agency has already arrived or is pending. Please check your statement for a credit from PAYGATE.

Please don't make another payment to the agency for this holding deposit while this is being looked at.

Kind regards,
Harrow & Vale Bank (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ESCALATE**: Hand the customer's chargeback request on the 18:04 £634.00 PAYGATE*NORTHGATE LET payment (auth A71C09) to the card disputes team for review and a decision, and tell the customer in the secure portal that this has been requested.

## What was escalated

What is known: the customer was charged twice, £634.00 each, by PAYGATE*NORTHGATE LET on 11 Sep at 18:02 (A71C02) and 18:04 (A71C09) (event-001). The agency's email of 14 Sep, which the bank has not verified, admits the duplicate and promises to refund one payment within 5–10 working days. In secure chat the customer asked for a chargeback on the second payment straight away (event-002, event-004). What was tried: a card-journal check for a refund or pending credit was recorded but not executed because no live system is connected, so the refund status is unknown. Question for the card disputes team: can a duplicate-processing chargeback be raised on A71C09 now, given the merchant's promised refund and the risk of a double credit? If so, raise it. Either way, tell the customer the outcome.

## What failed

- Policy guard blocked `send_secure_message`: promises a refund

## Final result

Both £634.00 debits are on the account (event-001). The chargeback request has been passed to the card disputes team for review, and no decision has been made. The customer has been told it is a request, not an outcome. Whether the agency has refunded anything, or has a refund pending, is not confirmed.

Message to the customer (secure portal, recorded, not sent):

> Dear Mr Ribeiro,
>
> Thank you for getting in touch about the two £634.00 card payments to PAYGATE*NORTHGATE LET on 11 September (18:02 and 18:04). I can see both payments on your account, and I understand you need this money for the full deposit.
>
> We have asked our card disputes team to look at raising a chargeback on the second payment (18:04). Please be aware of a few things:
> - This is a request for review. It is not a decision yet, and I can't promise that a chargeback will be raised or will succeed, or say how long it will take.
> - A chargeback is not usually a quick process. You have told us the agency has said in an email that they will return one payment. The bank hasn't verified that email and can't confirm whether or when any money will come back from the agency. If money from the agency comes back while a chargeback is open, the team may have to adjust the chargeback so the same amount isn't credited twice.
> - I haven't been able to confirm from our card records whether any credit from the agency has already arrived or is pending. Please check your statement for a credit from PAYGATE.
>
> Please don't make another payment to the agency for this holding deposit while this is being looked at.
>
> Kind regards,
> Harrow & Vale Bank
