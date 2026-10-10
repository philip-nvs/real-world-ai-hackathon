# Case 013: reasoning

## Evidence relied on

- event-001: 18 Sep: £750 collection presented and returned unpaid ('refer to payer'), available balance £710.40.
- event-001: 19 Sep: automated unpaid-DD letter sent. 21 Sep: originator re-presented the £750 collection and it was paid after salary was credited on 20 Sep.
- event-001: No unpaid-item fee charged by H&V. No further collection scheduled before 18 Oct.
- event-002: Customer asks what is going on and says she does not want to pay twice. The agency texted her (dated 22 Sep) asking for a manual £750 payment.
- event-003: Servicing agent said they would check both dates on the mandate.

## Conflicts between events

- The agency's text of 22 Sep says the September Direct Debit failed and asks for a manual payment. The bank's records (event-001) show the 21 Sep re-presentation was paid. The text probably reflects only the 18 Sep return, but the bank cannot see Northgate's records.
- The bank letter of 19 Sep (unpaid) and the statement debit of 21 Sep (paid) only look contradictory. They are two separate presentations of the same collection.

## Options rejected

- Tell the customer to make the manual £750 payment the agency asked for: The bank's records show the 21 Sep re-presentation was paid. Telling her to pay would risk a duplicate payment, and the rules forbid telling a customer to pay again.
- Tell the customer the agency has received the money and she is not in arrears: The bank's records show only the debit to H&V Collect. They don't confirm the recipient's records or her arrears position.
- Escalate to the Direct Debit team or fraud team: The bank's records explain the sequence and show no bank error. Nothing confirms the text is fraudulent, so advising her to use known contact details is enough without a referral.
- Wait for the Direct Debit journal check result: No live system is connected and no result will come back. The case record (event-001) already shows the collection history.

## Policy guard

- Blocked `send_secure_message`: advises paying again
