# Case 006: reasoning

## Evidence relied on

- event-001: Credit of £750.00 by Faster Payment on 26 Sep at 22:14 from R JAMES (Meridian Bank), reference RENT. No funds-recovery request has been received from Meridian.
- event-001: Text from an unknown mobile asks for the money to go to a different account. The CoP check on the account details in the text: No match, the account name is not R James (attachment cop_check_text_details.json, reason ANNM).
- event-001: Inbound payment message: payer account SYN-SC-06-2 / SYN-ACCT-06-2 at Meridian Bank, recovery_request_received false.
- event-002: Customer has not touched the funds and is asking whether she can send them back now.
- event-004: Customer says she was given a different account from the one the money came from and wants the money gone.

## Conflicts between events

- The screenshot attachment shows the return account as SYN-SC-06-2 / SYN-ACCT-06-2, the same as the payer's account, and has different wording. The event-001 transcription and the CoP check use SYN-SC-06-3 / SYN-ACCT-06-1, and the customer (event-004) says the account is different from the one the money came from.
- The text claims the payment was a mistake by the payer, but Meridian Bank has made no recovery request (event-001).

## Options rejected

- Tell the customer to send the money to the account in the text: The CoP check came back no match, the account differs from where the money came from, and this fits a known scam pattern.
- Tell the customer to pay it back herself to the originating account: The bank's misdirected-payment process should handle it. Telling her to make a payment herself risks a loss or duplication, and the details are disputed (the screenshot doesn't match the note).
- Ask the customer which account the text gave: The case already has enough to act on. The discrepancy is for the team to resolve, and the advice is the same for any account.
- Wait for the incoming-payment records check: No live system is connected, so no result will come back.

## Policy guard

No calls were blocked.
