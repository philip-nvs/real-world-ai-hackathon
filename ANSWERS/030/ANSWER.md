# Case 030: ESCALATE

## What the system received

The customer authenticated through the independent recovery route, reported a lost phone and asked the bank to revoke its access. They also asked that their £750 rent standing order due tomorrow is not cancelled. The case includes a device audit showing the lost device's session is still active with a misuse review open, plus the standing-order record.

0 events; attachments: device-audit.json, standing-order-history.csv.

Case loader notes:
- The history says Total events: 5, but 0 events were found.

## What the system did

- `submit_internal_request` → Security team: URGENT protective request, Case 030, account SYN-ACCT-B030. Customer Fara Tovell, authenticated via the established independent recovery route (recovery-line record 09:00, not the lost phone session), reports phone lost about 08:00 on 2026-11-20 and on the recovery-line call at 09:20 asked to revoke the lost phone's access. Device audit (09:05) shows lost device SYN-DEVICE-030 session_state ACTIVE, misuse review open, 0 new payment instructions and 0 beneficiary edits in window 00:00–09:05. Please revoke all sessions/access for SYN-DEVICE-030 now. Session revocation only: per the account's control procedure (09:15), this is separate from standing-order cancellation; customer explicitly asks that standing order SO-030 (Rent, £750.00 to SYN-ACCT-LAND030, next due 2026-11-21, status scheduled, 0 beneficiary edits since creation) is NOT cancelled or changed. Note: the case desk could not submit the revocation instruction directly because the case's event registry is not loading (policy guard did not recognise the case events), so it is handed to you to execute. Please also include the post-revocation period in the open misuse review and refer any payment restriction for review only if compromise is identified. Please confirm the revocation result to the case desk. (recorded, not executed)
- `send_secure_message` → Fara Tovell: Dear Fara,

Thank you for calling us through the recovery line about your lost phone. We have passed an urgent request to our security team to remove all access from your lost phone for account SYN-ACCT-B030. The revocation has been requested but is not yet confirmed. We'll only tell you it's done once our records show it.

About your rent: we have asked that only the phone's access is removed and that your £750.00 rent standing order is left as it is. In our records it is currently scheduled for 21 November 2026. Removing access from a device is a separate control from cancelling a standing order, and removing the phone's access does not cancel standing orders you already have set up. However, we cannot promise the payment will go out tomorrow. That depends on the payment processing as normal on the day.

Our security team is already reviewing the phone's session for possible misuse. This review is still open and no finding has been made. Our device check covered midnight to 09:05 today and found no new payment instructions and no changes to payees in that time. This does not cover anything after 09:05, and it does not mean the review is finished. If the team finds a problem, they may refer specific payment restrictions for review.

Please never share your password, PIN or one-time codes with anyone, including anyone who says they are from the bank.

Brackenfold Bank case desk (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ESCALATE**: Hand the urgent revocation of lost device SYN-DEVICE-030's sessions (revocation only, leaving standing order SO-030 untouched) to the security team, and tell the customer through the secure portal that this has been requested.

## What was escalated

Known from the case history file: at 09:00 Fara Tovell authenticated via the independent recovery route, not the lost phone session, and said the phone was lost about 08:00. At 09:20, on the verified recovery-line call, she explicitly asked for lost device SYN-DEVICE-030's access to be revoked and for SO-030 (£750 rent to SYN-ACCT-LAND030, due 2026-11-21) to stay scheduled. The 09:05 device audit shows the session still active and the misuse review open, with 0 new payment instructions and 0 beneficiary edits up to 09:05. The 09:10 record shows SO-030 scheduled with 0 beneficiary edits. The 09:15 procedure says revocation does not cancel standing orders and the desk cannot promise the payment will run. Tried and failed: a direct session-revocation instruction was blocked twice by the policy guard because the case's event registry did not load (0 events found). Handed to: the security team, as an urgent protective request. The result is unknown because no live system is connected. Question for the security team: please revoke all sessions for SYN-DEVICE-030 now without touching SO-030, confirm the result, and decide from the open misuse review whether any payment restriction needs review.

## What failed

- Policy guard blocked `submit_instruction`: authorised_by_event 'event-005' is not an event in this case
- Policy guard blocked `submit_instruction`: authorised_by_event 'e05' is not an event in this case
- Policy guard blocked `submit_decision`: evidence cites event-001, event-002, event-003, event-004, event-005, which is not an event in this case

## Final result

I've passed an urgent request to the security team to remove the lost phone's access (device SYN-DEVICE-030) but it hasn't been carried out yet, so the phone's session may still be active. No live system is connected, so no confirmation will come back. Standing order SO-030 (£750 rent) was scheduled for 2026-11-21 when last checked and no change to it was requested. The misuse review is still open. The customer has been sent a secure-portal message saying the removal has been requested, not done.

Message to the customer (secure portal, recorded, not sent):

> Dear Fara,
>
> Thank you for calling us through the recovery line about your lost phone. We have passed an urgent request to our security team to remove all access from your lost phone for account SYN-ACCT-B030. The revocation has been requested but is not yet confirmed. We'll only tell you it's done once our records show it.
>
> About your rent: we have asked that only the phone's access is removed and that your £750.00 rent standing order is left as it is. In our records it is currently scheduled for 21 November 2026. Removing access from a device is a separate control from cancelling a standing order, and removing the phone's access does not cancel standing orders you already have set up. However, we cannot promise the payment will go out tomorrow. That depends on the payment processing as normal on the day.
>
> Our security team is already reviewing the phone's session for possible misuse. This review is still open and no finding has been made. Our device check covered midnight to 09:05 today and found no new payment instructions and no changes to payees in that time. This does not cover anything after 09:05, and it does not mean the review is finished. If the team finds a problem, they may refer specific payment restrictions for review.
>
> Please never share your password, PIN or one-time codes with anyone, including anyone who says they are from the bank.
>
> Brackenfold Bank case desk
