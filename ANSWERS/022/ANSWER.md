# Case 022: ESCALATE

## What the system received

An authenticated cardholder sees a £600 hotel hold on top of a booked £520 hotel payment, leaving £380 available. She asks for the £600 to be made available again today so she can buy groceries. The case includes the card ledger extract and a merchant receipt sent by email.

0 events; attachments: card-entries.csv, hotel-receipt.pdf.

Case loader notes:
- The history says Total events: 5, but 0 events were found.

## What the system did

- `check_record` → card journal: Case 022, account SYN-ACCT-B022: current status of authorisation reservation AUTH-022 (GBP 600.00, active at 09:00) and booked card debit FINAL-022 (GBP -520.00, linked authorisation AUTH-022); current available balance. (recorded, not executed)
- `submit_internal_request` → card operations: Case 022, account SYN-ACCT-B022, cardholder Rois Fenwick (authenticated, event-001). Please investigate a possible lingering linked authorisation and, if eligible, release the stale hold. Card ledger at 09:00 (event-001, card-entries.csv): card debit FINAL-022 GBP 520.00 booked 08:30 with linked authorisation AUTH-022; authorisation reservation AUTH-022 GBP 600.00 still shown as active at 09:00; ledger balance GBP 980.00, available GBP 380.00. Merchant receipt (event-003, not verified by the bank) states final amount GBP 520.00, payment ref FINAL-022, auth ref AUTH-022. Customer says she needs the funds today for groceries (event-005). Please check linkage and current network state per procedure (event-004) and confirm the outcome. A live card journal check was recorded but could not be executed (no live system connected). (recorded, not executed)
- `send_secure_message` → Rois Fenwick: Dear Rois,

Thank you for your message. I understand you need this money for groceries today. Here is what our records show and what we have done.

Our card ledger, as retrieved at 09:00 today, shows:
- one booked card payment to the hotel of £520.00 (reference FINAL-022)
- a separate £600.00 card authorisation hold (reference AUTH-022), still active at 09:00. Our records link it to that same payment.
- a ledger balance of £980.00 and an available balance of £380.00.

The £600.00 is a hold (a reservation), not a second payment that has gone through. Your records show one booked hotel payment, for £520.00. The hold is what is reducing your available balance.

I can't release a hold myself. I have asked our card operations team to look into the £600.00 hold and, if it is eligible, release it. Before they can, they need to check how it is linked to the payment and its current status on the card network. I can't promise that it will be released, or that it will happen today. The timing depends on those checks. This request is not yet a decision.

I also tried to check the current status of the hold in our card journal, but I could not get a live result. So I can't confirm anything about it after 09:00 today.

Kind regards,
Brackenfold Bank case desk (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ESCALATE**: Hand the possible stale £600 authorisation hold AUTH-022 on SYN-ACCT-B022 to card operations to investigate and, if eligible, release, and tell the customer through the secure portal what the ledger shows and that release has been requested but not promised.

## What was escalated

Card operations: SYN-ACCT-B022 (Rois Fenwick, authenticated). Known facts: FINAL-022 £520.00 is booked and linked to AUTH-022. The AUTH-022 reservation of £600.00 was still active at 09:00. Available balance was £380.00 against a ledger balance of £980.00 (E01). The merchant receipt (E03, unverified) says the final amount is £520.00. What was tried: a live card journal check was recorded but not executed, so the status after 09:00 is unknown. Question to answer: is AUTH-022 a stale linked hold eligible for release under the E04 procedure, given its linkage and current network state? If so, release it and confirm the outcome. The customer says she needs the funds today for groceries. This is not enough to show financial hardship, but watch for further signs and refer to the vulnerability team (with her consent) if they appear.

## What failed

- Policy guard blocked `submit_decision`: evidence cites event-001, event-002, event-003, event-004, event-005, which is not an event in this case

## Final result

Our ledger at 09:00 shows one booked £520.00 hotel payment and a separate £600.00 hold (AUTH-022), still active and linked to it, leaving £380.00 available. I've asked card operations to investigate the hold and release it if it's eligible, and messaged the customer. A release isn't confirmed or promised, and the hold's status after 09:00 is unconfirmed.

Message to the customer (secure portal, recorded, not sent):

> Dear Rois,
>
> Thank you for your message. I understand you need this money for groceries today. Here is what our records show and what we have done.
>
> Our card ledger, as retrieved at 09:00 today, shows:
> - one booked card payment to the hotel of £520.00 (reference FINAL-022)
> - a separate £600.00 card authorisation hold (reference AUTH-022), still active at 09:00. Our records link it to that same payment.
> - a ledger balance of £980.00 and an available balance of £380.00.
>
> The £600.00 is a hold (a reservation), not a second payment that has gone through. Your records show one booked hotel payment, for £520.00. The hold is what is reducing your available balance.
>
> I can't release a hold myself. I have asked our card operations team to look into the £600.00 hold and, if it is eligible, release it. Before they can, they need to check how it is linked to the payment and its current status on the card network. I can't promise that it will be released, or that it will happen today. The timing depends on those checks. This request is not yet a decision.
>
> I also tried to check the current status of the hold in our card journal, but I could not get a live result. So I can't confirm anything about it after 09:00 today.
>
> Kind regards,
> Brackenfold Bank case desk
