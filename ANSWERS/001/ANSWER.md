# Case 001: ESCALATE

## What the system received

Mr Bell (ID&V passed on the phone) can't get to £750, which is all of his available money. It was held after Meridian sent a scam-recovery request about a £2,600 payment he received. He says the payment was for a van he sold and the buyer collected in person. He has given a listing and chat messages as evidence and needs money for £900 rent due tomorrow.

6 events; attachments: account_hold_notice.txt, customer_evidence_listing.txt, customer_evidence_messages.txt, funds_recovery_request_MERIDIAN.txt.

## What the system did

- `check_record` → limit register / account hold register: Case 001 - Marcus Bell, account SYN-SC-01-1 / SYN-ACCT-01-1: current status of hold applied 2026-09-23 17:56 for inbound recovery request MER-FR-2026-081734 (amount, status, response deadline to Meridian). (recorded, not executed)
- `check_record` → incoming-payment records: Case 001 - Faster Payment credit 2026-09-21 14:10, GBP 2,600.00 from L FARRELL (Meridian), ref VAN, to SYN-SC-01-1 / SYN-ACCT-01-1: confirm details and any linked recovery/dispute flags. (recorded, not executed)
- `submit_internal_request` → Fraud Operations (inbound funds recovery): Case 001 – Marcus Bell, SYN-SC-01-1 / SYN-ACCT-01-1. Inbound APP recovery request MER-FR-2026-081734 from Meridian (received 23 Sep 17:55, response due within 2 working days) led to a system hold of £750.00 (all available funds) on 23 Sep 17:56. Disputed credit: £2,600 FPS 21 Sep 14:10 from L FARRELL, ref VAN; £1,850 already paid to customer's own Barclaycard (payee on file since 2022) before the request. On a verified call today (ID&V passed) the customer disputes the scam claim: he says he sold a 2017 Ford Transit via a marketplace, buyer 'Lou F.' collected it in person on Monday 21 Sep and paid by transfer on his drive; V5C handed over. Customer-supplied (unverified) evidence: listing marked 'collection only / no delivery', priced £2,600, marked sold 21 Sep; chat showing buyer arrived 13:52, said 'sending the money now… ref VAN' at 14:06, customer confirmed keys and V5C green slip at 14:11 (payment credited 14:10). This conflicts with the payer's statement to Meridian ('seller said it would be delivered Tuesday. No van'). Meridian supplied no police reference; no previous reports against payee; customer has 6 years with the bank, no fraud markers, no other unknown inbound credits in 90 days. Customer states rent of £900 is due tomorrow (25 Sep) and he has no access to funds – possible financial hardship. Please review the hold and the recovery request with the customer's evidence, decide whether the hold should be maintained or released, and respond to Meridian within the deadline. Decision needed: does the evidence support keeping the £750 hold, and should the bank request DVLA/V5C confirmation or further evidence from Meridian/the payer? (recorded, not executed)
- `send_secure_message` → Marcus Bell: Dear Mr Bell,

Following your call today, here's what our records show and what happens next.

On 23 September at 17:56 we placed a hold of £750.00 on your account. This was in response to a funds-recovery request from the bank that sent the £2,600 payment you received on 21 September (from L Farrell, reference "VAN"). The person who made that payment has told their bank it was a scam. Under the industry process we have to hold any of the disputed money still in the account while the claim is looked at. The hold does not mean we have decided you did anything wrong. Your account has no fraud markers on our records.

You told us you sold your Transit van and the buyer collected it in person on 21 September, and that you have the listing, the messages and the V5C handover. We have asked our Fraud Operations team to review the hold and the recovery request together with your account of the sale and the evidence you've given us. This review has been requested but no decision has been made yet. We can't promise the hold will be lifted or give you a date for the outcome. If you have more evidence, such as a copy of the V5C new keeper slip or confirmation from the DVLA that you've told them about the sale, please keep it ready.

We know your £900 rent is due tomorrow and you can't get to this money, and we're sorry this is so stressful. Our financial support team may be able to talk to you about your options while the review takes place. Would you like us to refer you to them? We would need to share your details and situation with them, so please reply in the secure portal to say whether you agree.

Please don't share passwords, PINs or one-time codes with anyone, including us.

Harrow & Vale Bank plc (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ESCALATE**: Hand the hold and Meridian recovery request MER-FR-2026-081734 to Fraud Operations to review against the customer's evidence and decide, and send the customer a secure message explaining the hold and asking whether he agrees to a financial support referral.

## What was escalated

Known: the £750 hold (all available funds) was applied automatically on 23 Sep 17:56 after Meridian's recovery request MER-FR-2026-081734 about the £2,600 credit on 21 Sep (ref VAN). £1,850 had already gone to the customer's own Barclaycard before the request. Customer for 6 years, no fraud markers. The customer disputes the claim with a listing (collection only, sold 21 Sep, £2,600) and a chat log showing the buyer collected the van and V5C at about 14:11, right after the 14:10 credit. This contradicts the payer's 'not delivered' statement, and Meridian gave no police reference. Tried: read-only checks of the hold register and incoming-payment records were requested, but no live system is connected, so no results came back. Customer: says rent of £900 is due tomorrow (possible financial hardship). He has been asked for consent to a financial support referral; no reply yet. Question for Fraud Operations: given the customer's evidence and the conflicting payer statement, should the £750 hold be kept or released, and what response or evidence request goes to Meridian within the 2-working-day deadline?

## What failed

Nothing failed.

## Final result

The £750 hold under Meridian request MER-FR-2026-081734 stays in place according to the case record. A Fraud Operations review of the hold, using the customer's evidence, has been requested but not decided. The customer has been told what the records show and asked whether he agrees to a financial support referral.

Message to the customer (secure portal, recorded, not sent):

> Dear Mr Bell,
>
> Following your call today, here's what our records show and what happens next.
>
> On 23 September at 17:56 we placed a hold of £750.00 on your account. This was in response to a funds-recovery request from the bank that sent the £2,600 payment you received on 21 September (from L Farrell, reference "VAN"). The person who made that payment has told their bank it was a scam. Under the industry process we have to hold any of the disputed money still in the account while the claim is looked at. The hold does not mean we have decided you did anything wrong. Your account has no fraud markers on our records.
>
> You told us you sold your Transit van and the buyer collected it in person on 21 September, and that you have the listing, the messages and the V5C handover. We have asked our Fraud Operations team to review the hold and the recovery request together with your account of the sale and the evidence you've given us. This review has been requested but no decision has been made yet. We can't promise the hold will be lifted or give you a date for the outcome. If you have more evidence, such as a copy of the V5C new keeper slip or confirmation from the DVLA that you've told them about the sale, please keep it ready.
>
> We know your £900 rent is due tomorrow and you can't get to this money, and we're sorry this is so stressful. Our financial support team may be able to talk to you about your options while the review takes place. Would you like us to refer you to them? We would need to share your details and situation with them, so please reply in the secure portal to say whether you agree.
>
> Please don't share passwords, PINs or one-time codes with anyone, including us.
>
> Harrow & Vale Bank plc
