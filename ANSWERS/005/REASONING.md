# Case 005: reasoning

## Evidence relied on

- event-001: Mandate H&V COLLECT / OAKFIELD PM active since Feb 2025. £875.00 was collected on 24 Aug and on 23 Sep. The 23 Sep collection took the account £412 overdrawn and a £6.50 fee was applied on 24 Sep. £2,525.00 is scheduled for 28 Sep (instruction received 24 Sep). Available balance is £600.00. The bank can't see whether advance notices were sent.
- event-002: Customer passed ID&V on the phone and says she moved out at the end of August. She says the agency told her it can't cancel the collection on its side.
- event-004: On the verified call, the customer explicitly asked for Monday's collection to be stopped, for the August and September collections to be refunded and for the overdraft fee to be refunded.

## Conflicts between events

- The customer wants the 24 Aug collection refunded, but it was taken before the tenancy end date she gave (31 Aug).
- The tenancy end date comes only from a forwarded agency email (a claim, not a bank record). The originator labels the £2,525 collection as the final account for the property, which suggests the agency may say a balance is owed.
- The bank can't see whether advance notice was given for the September collections.

## Options rejected

- Submit the stop of the 28 Sep collection directly as an instruction: Tried, and rejected by the policy guard because the phone channel isn't a secure confirmation. It was passed to the Direct Debit team as an urgent protective request instead.
- Cancel the whole mandate: The customer asked only for Monday's collection to be stopped, not for the mandate to be cancelled. Keeping the step narrow.
- Promise refunds of the August and September collections and the fee: Refunds are decided by the Direct Debit team after review. The bank can't promise the outcome, and the August collection predates the stated tenancy end.
- Refer to the financial support team now: This would share her details, which needs her consent first. She has been offered support instead.
- Wait for the records check result: No live system is connected, so no result will come back.

## Policy guard

- Blocked `submit_instruction`: event-004 came by 'Phone (personal banking)', which is not a secure confirmation (an email is never authorisation)
- Blocked `send_secure_message`: gives a guarantee
