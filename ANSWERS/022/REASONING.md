# Case 022: reasoning

## Evidence relied on

- E01: Card ledger at 09:00: FINAL-022 	£520.00 booked 08:30 with linked authorisation AUTH-022; AUTH-022 reservation £600.00 active at 09:00; ledger £980.00, available £380.00; contact authentication passed.
- E02: Customer reports £600 and £520 taken and an available balance of £380, and expected the stay to cost £520.
- E03: Merchant email and receipt (an unverified external claim) state the final amount is £520.00, ref FINAL-022, auth AUTH-022, and that the stay ended that morning.
- E04: Procedure: card operations can investigate a lingering linked authorisation and release an eligible stale hold after checks. The case desk cannot release a hold, and timing depends on the checks.
- E05: Customer asks for the £600 back in her available balance today because she needs groceries.

## Conflicts between events

- The customer believes £1,120 was taken (E02), but the ledger shows only £520 booked; the £600 is an active authorisation hold, not a booked debit (E01).
- The case loader note says 0 events were found, although the history lists 5 events; the history shown was used.
- The live card journal check and the card operations request were recorded but not executed (no live system connected), so the hold's status after 09:00 is unconfirmed.

## Options rejected

- Release the hold or promise funds today: The case desk cannot release holds (E04), and timing depends on card operations' checks.
- Wait for the journal check: No live system is connected, so no result will come back; the customer needs an answer now.
- Treat the merchant receipt as proof: An external email is a claim; only the bank's ledger (E01) was relied on.
- Refer to vulnerability support now: Urgency about groceries alone doesn't establish hardship, and a referral that shares her details would need her consent.

## Policy guard

- Blocked `submit_decision`: evidence cites event-001, event-002, event-003, event-004, event-005, which is not an event in this case
