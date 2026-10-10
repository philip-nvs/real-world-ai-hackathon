# Case 006: ESCALATE

## What the system received

A student customer got an unexpected £750 Faster Payment. Someone texting from an unknown number, claiming to be the payer, has asked her to send it to a different account. She wants to know whether she can just send it, and whether it matters that the account differs from the one the money came from.

4 events; attachments: cop_check_text_details.json, inbound_payment_message.json, sms_screenshot.png.

## What the system did

- `check_record` → incoming-payment records: Case 006: Aisha Khan, payee SYN-SC-06-1 / SYN-ACCT-06-3. Inbound FPS credit £750.00 received 2026-09-26 22:14:31 from R JAMES (Meridian Bank, SYN-SC-06-2 / SYN-ACCT-06-2), ref RENT, end-to-end ID MER26092622143198. Confirm the credit is posted and whether any funds-recovery / misdirected-payment request has been received from Meridian Bank. (recorded, not executed)
- `submit_internal_request` → Payments team (misdirected payments) with Fraud team: Case 006 – Aisha Khan (20, student current account SYN-SC-06-1 / SYN-ACCT-06-3). Unexpected inbound FPS credit £750.00 on 2026-09-26 22:14:31 from R JAMES, Meridian Bank (SYN-SC-06-2 / SYN-ACCT-06-2), ref RENT, E2E ID MER26092622143198. Per case record no funds-recovery request received from Meridian. On 27 Sep the customer received a text from an unknown mobile claiming to be the payer and asking her to send the money to a different account. The case note transcription gives SYN-SC-06-3 / SYN-ACCT-06-1; CoP on those details returned No match (ANNM) – account name is not "R James". Note conflict: the customer's screenshot shows SYN-SC-06-2 / SYN-ACCT-06-2 (same as originating account) and differs in wording from the note's transcription; customer herself says she was given a different account from the one the payment came from. Pattern consistent with an overpayment/misdirected-payment scam or money-mule recruitment. Customer has not touched the funds and wants them returned. Please: (1) review the credit and the text for fraud risk; (2) decide how the funds are handled under the bank's misdirected-payment process (e.g. contact Meridian Bank to return to the originating account) – customer has been told not to send money herself; (3) record whether the credit/funds should be protected pending review. Live incoming-payment records check could not be completed (no live system connected). (recorded, not executed)
- `send_secure_message` → Aisha Khan: Hi Aisha, thank you for checking with us before sending anything. To answer your question: yes, being asked to pay the money into a different account from the one it came from is a problem. Please don't send the £750 anywhere yourself for now, including to the account in the text.

Here's what our records show. The £750 reached your account on 26 September at 22:14 by Faster Payment. It came from an account in the name R JAMES at Meridian Bank, with the reference "RENT". So far our records show no request from Meridian Bank to get the payment back.

We ran a Confirmation of Payee check on the account details in the text you received. The result was "no match", meaning the name on that account isn't "R James". On its own, this doesn't tell us who sent the text, but it does mean we can't confirm the account belongs to the person who paid you.

We've asked our payments and fraud teams to look at the payment and the text, and to decide how the money should be returned through the bank's own process. That's a request at this stage, not a decision, and we can't give you a timescale.

Until then, please:
- leave the money where it is and don't spend or move it
- don't reply to the text with any personal or banking details, and don't send money to any account it gives you
- never share your passwords, PINs or one-time codes with anyone. Harrow & Vale Bank will never ask you for them.

You've done exactly the right thing by not sending the money. (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ESCALATE**: Hand the case to the Payments (misdirected payments) and Fraud teams to review the credit and the text and decide how the funds are returned through the bank's process, and tell the customer by secure message not to send the money herself.

## What was escalated

Known: £750 FPS credit on 26 Sep at 22:14 from R JAMES, Meridian Bank (SYN-SC-06-2 / SYN-ACCT-06-2), ref RENT, E2E ID MER26092622143198, into Aisha Khan's student account (age 20). No recovery request from Meridian. On 27 Sep an unknown mobile texted asking for the money to go to a different account. The CoP check on SYN-SC-06-3 / SYN-ACCT-06-1 gave no match (ANNM). The customer hasn't touched the funds and has been told not to send them herself. Conflict: the screenshot shows SYN-SC-06-2 / SYN-ACCT-06-2 (the originating account) with different wording from the note's transcription. The live incoming-payment records check was requested, but no live system was connected, so it gave no result. The pattern fits a misdirected-payment or money-mule scam. Question for the team: is this credit genuinely misdirected, and how should the funds be returned under the bank's process (e.g. contacting Meridian to return them to the originating account)? Do the funds need protecting while you review?

## What failed

Nothing failed.

## Final result

The credit and the text have been passed to the Payments and Fraud teams to review. A secure message tells the customer not to send the money herself and gives her the CoP result. Neither a review result nor a return of the funds has been confirmed.

Message to the customer (secure portal, recorded, not sent):

> Hi Aisha, thank you for checking with us before sending anything. To answer your question: yes, being asked to pay the money into a different account from the one it came from is a problem. Please don't send the £750 anywhere yourself for now, including to the account in the text.
>
> Here's what our records show. The £750 reached your account on 26 September at 22:14 by Faster Payment. It came from an account in the name R JAMES at Meridian Bank, with the reference "RENT". So far our records show no request from Meridian Bank to get the payment back.
>
> We ran a Confirmation of Payee check on the account details in the text you received. The result was "no match", meaning the name on that account isn't "R James". On its own, this doesn't tell us who sent the text, but it does mean we can't confirm the account belongs to the person who paid you.
>
> We've asked our payments and fraud teams to look at the payment and the text, and to decide how the money should be returned through the bank's own process. That's a request at this stage, not a decision, and we can't give you a timescale.
>
> Until then, please:
> - leave the money where it is and don't spend or move it
> - don't reply to the text with any personal or banking details, and don't send money to any account it gives you
> - never share your passwords, PINs or one-time codes with anyone. Harrow & Vale Bank will never ask you for them.
>
> You've done exactly the right thing by not sending the money.
