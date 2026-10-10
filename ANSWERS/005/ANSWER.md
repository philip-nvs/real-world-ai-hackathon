# Case 005: ESCALATE

## What the system received

On a verified phone call, the customer is disputing Direct Debit collections by her former letting agency after she moved out. She wants the £2,525 collection due Monday 28 Sep stopped, the £875 collections from August and September refunded, and the £6.50 unarranged overdraft fee refunded. The case includes a forwarded agency email, the incoming collection instruction and a statement extract.

4 events; attachments: agency_move_out_confirmation.eml, incoming_dd_instruction.json, statement_extract.csv.

## What the system did

- `check_record` → Direct Debit mandate register and collection journal: Case 005, Gabriela Petrova: mandate OPM-78COOMBE-3312 (SUN H&V COLLECT 771902, Oakfield Property Management Ltd). Status of the mandate, the collections of 24 Aug and 23 Sep 2026 (£875.00 each), and the scheduled collection of £2,525.00 for 28 Sep 2026 (received 24 Sep). (recorded, not executed)
- `submit_internal_request` → Direct Debit team: Case 005, Gabriela Petrova (ID&V passed on phone, event-002). Mandate OPM-78COOMBE-3312, Oakfield Property Management Ltd (SUN H&V COLLECT 771902), active since Feb 2025. Customer says her tenancy at 78 Coombe Road ended 31 Aug 2026 (forwarded agency email dated 1 Sep, unverified). In event-004 she asked for refunds of the £875.00 collection on 24 Aug 2026 and the £875.00 collection on 23 Sep 2026 under the Direct Debit Guarantee, and asked for the £2,525.00 collection scheduled for 28 Sep 2026 (narrative 'FINAL ACCOUNT 78 COOMBE RD', received 24 Sep) to be stopped. A stop instruction for the 28 Sep collection has been submitted but its result is not confirmed (no live system connected) – please confirm it has been stopped before Monday 28 Sep. Bank cannot see whether advance notices were sent for the Sep collections. Note: the 24 Aug collection falls before the stated tenancy end date. Please review both indemnity claims and decide; please also confirm whether the customer wants the mandate cancelled (not instructed yet). Also requested: review of the £6.50 unarranged overdraft fee charged 24 Sep, which followed the disputed 23 Sep collection – please route to tariff/fees as needed. Customer is distressed and was overdrawn by £412.90 with no arranged overdraft; consider vulnerability/financial-support referral, but only with her consent. (recorded, not executed)
- `submit_internal_request` → Direct Debit team: URGENT correction to Case 005 request: the stop instruction for the £2,525.00 collection due Mon 28 Sep 2026 under mandate OPM-78COOMBE-3312 (Oakfield Property Management Ltd, SUN H&V COLLECT 771902) was NOT submitted – it was rejected by the policy guard because the phone channel is not treated as a secure confirmation. Customer Gabriela Petrova (ID&V passed, event-002) explicitly asked on the verified call (event-004) for this collection to be stopped. This is a protective request for a payment not yet made: please stop this specific collection before 28 Sep and confirm the outcome. Mandate cancellation not instructed. (recorded, not executed)
- `send_secure_message` → Gabriela Petrova: Dear Ms Petrova,

I'm sorry about the worry this has caused you. Here's where things stand after your call today.

What our records show: there is a Direct Debit to Oakfield Property Management (reference OPM-78COOMBE-3312) on your account. It collected £875.00 on 24 August and £875.00 on 23 September. The September collection took your account £412.90 overdrawn, and a £6.50 unarranged overdraft fee was charged on 24 September. Oakfield sent us a further collection of £2,525.00 on 24 September, scheduled for Monday 28 September, with the description "FINAL ACCOUNT 78 COOMBE RD". We can't see whether Oakfield gave you advance notice of the September collections.

What we have done:
- Monday's £2,525.00 collection: we have passed your request to stop this collection to our Direct Debit team as urgent. We have not yet had confirmation that it has been stopped, so please don't treat it as stopped until we confirm. This request covers only Monday's collection. The Direct Debit itself is still set up. If you want it cancelled, please tell us through the secure portal.
- Refunds of the 24 August and 23 September collections: we have passed your refund claims to our Direct Debit team for review. This is a review, not a decision yet, and we can't tell you the outcome in advance. Please note the 24 August collection was taken before the 31 August tenancy end date you gave us.
- The £6.50 overdraft fee: we have asked for it to be reviewed. This is also not a decision yet.

Stopping or refunding a Direct Debit with us doesn't settle anything you may owe Oakfield, or anything they say you owe, for the property. You'd need to resolve that directly with them.

If money is tight right now and you'd like help from our specialist support team, just let us know. We'll only pass on your details if you agree.

Kind regards,
Harrow & Vale Bank (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ESCALATE**: Hand the urgent stop of the 28 Sep £2,525.00 collection, the refund claims for the 24 Aug and 23 Sep collections, and the overdraft fee review to the Direct Debit team, and tell the customer by secure message what has been requested.

## What was escalated

Known: The customer passed ID&V on the phone (event-002). On the call she explicitly asked for the £2,525.00 collection due Mon 28 Sep (mandate OPM-78COOMBE-3312, SUN H&V COLLECT 771902) to be stopped, for the £875.00 collections of 24 Aug and 23 Sep to be refunded and for the £6.50 unarranged overdraft fee of 24 Sep to be refunded (event-004). Available balance is £600.00 and she has no arranged overdraft. She was distressed on the call.

Tried and failed: A direct stop instruction was rejected by the policy guard because the phone channel isn't treated as a secure confirmation, so the stop has NOT been executed. A records check of the mandate register and collection journal was recorded, but no live system returned a result.

Requested: The Direct Debit team has been asked to urgently stop the 28 Sep collection as a protective request and confirm the outcome, to review the refund claims for both £875 collections, and to route the fee review.

Conflicts: The 24 Aug collection predates the stated 31 Aug tenancy end. The end date is backed only by a forwarded email. The bank can't see whether advance notices were sent.

Questions for the Direct Debit team: Has the 28 Sep £2,525.00 collection been stopped before it is taken? Do the 24 Aug and 23 Sep collections qualify for an indemnity refund? Should the £6.50 fee be refunded as a result? The mandate has not been cancelled, because the customer didn't instruct that. A financial-support referral needs her consent first.

## What failed

- Policy guard blocked `submit_instruction`: event-004 came by 'Phone (personal banking)', which is not a secure confirmation (an email is never authorisation)
- Policy guard blocked `send_secure_message`: gives a guarantee

## Final result

Nothing has been confirmed as stopped, refunded or reviewed yet. The stop of the 28 Sep £2,525.00 collection was not executed directly (policy guard). It has been requested urgently from the Direct Debit team, along with a review of the refund claims for the 24 Aug and 23 Sep £875.00 collections and of the £6.50 fee. The mandate remains active. The customer has been told this by secure message.

Message to the customer (secure portal, recorded, not sent):

> Dear Ms Petrova,
>
> I'm sorry about the worry this has caused you. Here's where things stand after your call today.
>
> What our records show: there is a Direct Debit to Oakfield Property Management (reference OPM-78COOMBE-3312) on your account. It collected £875.00 on 24 August and £875.00 on 23 September. The September collection took your account £412.90 overdrawn, and a £6.50 unarranged overdraft fee was charged on 24 September. Oakfield sent us a further collection of £2,525.00 on 24 September, scheduled for Monday 28 September, with the description "FINAL ACCOUNT 78 COOMBE RD". We can't see whether Oakfield gave you advance notice of the September collections.
>
> What we have done:
> - Monday's £2,525.00 collection: we have passed your request to stop this collection to our Direct Debit team as urgent. We have not yet had confirmation that it has been stopped, so please don't treat it as stopped until we confirm. This request covers only Monday's collection. The Direct Debit itself is still set up. If you want it cancelled, please tell us through the secure portal.
> - Refunds of the 24 August and 23 September collections: we have passed your refund claims to our Direct Debit team for review. This is a review, not a decision yet, and we can't tell you the outcome in advance. Please note the 24 August collection was taken before the 31 August tenancy end date you gave us.
> - The £6.50 overdraft fee: we have asked for it to be reviewed. This is also not a decision yet.
>
> Stopping or refunding a Direct Debit with us doesn't settle anything you may owe Oakfield, or anything they say you owe, for the property. You'd need to resolve that directly with them.
>
> If money is tight right now and you'd like help from our specialist support team, just let us know. We'll only pass on your details if you agree.
>
> Kind regards,
> Harrow & Vale Bank
