# Case 015: reasoning

## Evidence relied on

- event-001: 28 Aug Faster Payment −£4,980.00 to HARROW & VALE RE LIME PROPERTY CA, ref MOVE IN 14 GROVE. Bank record doesn't show how the agency allocated it.
- event-001: DD mandate H&V COLLECT / LIME PROPERTY created 2 Sep via originator invite. DD collection −£4,980.00 paid on 14 Sep. Account now £3,100 overdrawn against a £1,000 arranged limit, with daily unarranged fees (statement shows £6.50 fee, balance −£3,084.20).
- event-002: ID&V passed on the phone. Customer asks for a refund under the Guarantee and for the DD to be cancelled.
- event-004: Customer says he never agreed to £4,980 by Direct Debit.

## Conflicts between events

- The originator's advance notice (attachment, unverified) describes £4,980 as the account balance at 8 Sep. The customer says he had already paid all the move-in money on 28 Aug (the bank record confirms a £4,980 transfer was sent). How the agency allocated that transfer isn't shown in bank records.
- The bank's payment confirmation PDF says the transfer was received by the beneficiary bank. That is a document claim and was not confirmed by a live journal check in this step.

## Options rejected

- Cancel the mandate now citing event-002: Blocked by the policy guard: a phone call is not a secure confirmation, so the customer must confirm in the secure portal. It isn't an urgent protective stop either, because the next collection isn't due for about a month.
- Promise an immediate refund today: The bank can't promise a refund or a timescale. The indemnity decision belongs to the Direct Debit team.
- Tell the customer the advance notice means the collection was valid: The notice is an unverified originator document, and the customer disputes the amount. Deciding that is for the DD team.
- Wait for the journal check results: No live system is connected, so no result will come back.

## Policy guard

- Blocked `submit_instruction`: event-002 came by 'Phone (personal banking)', which is not a secure confirmation (an email is never authorisation)
- Blocked `send_secure_message`: gives a guarantee
