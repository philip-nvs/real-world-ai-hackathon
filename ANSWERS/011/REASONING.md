# Case 011: reasoning

## Evidence relied on

- event-001: Two Faster Payment credits of £1,096.00 on 21 Sep 09:40 and 22 Sep 14:20, both from Meridian SYN-SC-11-2 / SYN-ACCT-11-2, payer name 'A KOWALCZYK', reference 'INV 2211 BOILER'.
- event-001: CoP on the refund details SYN-SC-11-2 / SYN-ACCT-11-2 with the name 'M Kowalczyk' returned Match – 'M KOWALCZYK' (personal account).
- event-002: The customer asks the bank to refund one of the payments to the account details in the client's text, which are the same account the credits came from.
- event-003: The agent pointed out that the payer name (A Kowalczyk) differs from the refund name (M Kowalczyk).
- event-004: The customer explains that Anna is the client and Marek her husband, and that the account is his but she uses it.

## Conflicts between events

- The payer name on both credits is 'A KOWALCZYK', but the refund name and CoP result are 'M KOWALCZYK'. The account number and sort code are the same as the originating account, and the customer's explanation (event-004) fits, but the bank can't verify who the account holder(s) are beyond the CoP match.
- The client's text is an external message forwarded by the customer and hasn't been verified. It is not authorisation for anything.

## Options rejected

- Send the refund from the customer's account on his behalf: The bank doesn't make outgoing payments for customers, and the customer hasn't given an instruction that counts. A chat message isn't an executable payment instruction, and the client's text is an external message.
- Tell the customer to go ahead and send the £1,096 refund now: We haven't been able to check for a recall/return request from Meridian or for any refund already set up, so advising a payment now could mean the money is returned twice.
- Escalate to the payment or fraud team over the A/M name difference: The refund details are the same account both credits came from, and CoP matched. The bank's records show nothing that points to fraud, so a referral isn't needed.
- Ask the customer to get further confirmation from his client: Nothing is actually missing. The refund account is the originating account shown in the bank's own records.

## Policy guard

- Blocked `send_secure_message`: advises paying again
