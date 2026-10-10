# Case 019: ACT

## What the system received

The customer asks the bank to recall a £651 Faster Payment she made to Co-Clean on 12 Aug. She says her letting agent also paid the same invoice and that Co-Clean has agreed to refund one payment. She attached the agency statement extract, Co-Clean's email and the bank's payment confirmation PDF.

4 events; attachments: agency_statement_extract.txt, coclean_refund_agreement.eml, payment_confirmation_2026-08-12.pdf.

## What the system did

- `check_record` → payment journal: Case 019, Linda Ferris, account SYN-ACCT-19-1: Faster Payment HV26081210144802, 12 Aug 2026 10:14, £651.00 to CO-CLEAN SERVICES LTD, ref "INV 4471 53 WINCHESTER". Status, CoP result, and whether any recall or return is recorded against it. Also any incoming credit from CO-CLEAN SERVICES LTD since 12 Aug 2026. (recorded, not executed)
- `send_secure_message` → Linda Ferris: Dear Mrs Ferris,

Thank you for your patience. Here is what our records show and what a recall would and wouldn't do.

Our account records show a Faster Payment of £651.00 from your account on 12 August 2026 to CO-CLEAN SERVICES LTD, reference "INV 4471 53 WINCHESTER". It went to a new payee, and the Confirmation of Payee check matched at the time. I have asked for the payment journal to be checked as well, but I don't have a result from that check yet. That means I can't confirm from our records whether any money from Co-Clean has reached your account.

Why a recall isn't the right route here: once a Faster Payment has been sent, we can't take it back. A recall is mainly for payments sent to the wrong account or sent in error. All it does is ask the receiving bank to return the money, and that only happens if the account holder agrees. Your payment went to the payee you meant to pay, and the second payment was made separately by your letting agent. Any return of the money therefore depends on Co-Clean, whether it comes through a recall request or directly from them. A recall request would not necessarily be any quicker than dealing with Co-Clean directly.

What this does not mean: we have not made any finding about the payment. We haven't asked for a recall or started a dispute, and we haven't checked Co-Clean's records or your agent's. The email and statement extract you sent us show what Co-Clean and Oakfield PM have said. They are not our records, and we can't say whether or when Co-Clean will return the money.

What you can do: the most direct route is to contact Co-Clean about when they will make the payment back to you. Please don't send any further payment for invoice 4471. If nothing arrives, you can contact us again through the app and we can look at the options with you then.

Kind regards,
Harrow & Vale Bank plc (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ACT**: Send the customer a secure-portal message explaining what the bank's records show about the 12 Aug payment and why a recall would not reverse it or speed up Co-Clean's refund, after requesting a payment-journal check of the payment and of any incoming credit from Co-Clean.

## What was escalated

Nothing was escalated.

## What failed

- Policy guard blocked `send_secure_message`: promises a refund

## Final result

The bank's account view shows the 12 Aug £651.00 Faster Payment to CO-CLEAN SERVICES LTD, made to a new payee with a CoP match. A payment-journal check was requested but no live system returned a result, so the payment's current status and any incoming refund are not confirmed. A secure message explaining that a recall would not reverse the payment or speed up Co-Clean's refund has been requested; no recall or dispute was raised.

Message to the customer (secure portal, recorded, not sent):

> Dear Mrs Ferris,
>
> Thank you for your patience. Here is what our records show and what a recall would and wouldn't do.
>
> Our account records show a Faster Payment of £651.00 from your account on 12 August 2026 to CO-CLEAN SERVICES LTD, reference "INV 4471 53 WINCHESTER". It went to a new payee, and the Confirmation of Payee check matched at the time. I have asked for the payment journal to be checked as well, but I don't have a result from that check yet. That means I can't confirm from our records whether any money from Co-Clean has reached your account.
>
> Why a recall isn't the right route here: once a Faster Payment has been sent, we can't take it back. A recall is mainly for payments sent to the wrong account or sent in error. All it does is ask the receiving bank to return the money, and that only happens if the account holder agrees. Your payment went to the payee you meant to pay, and the second payment was made separately by your letting agent. Any return of the money therefore depends on Co-Clean, whether it comes through a recall request or directly from them. A recall request would not necessarily be any quicker than dealing with Co-Clean directly.
>
> What this does not mean: we have not made any finding about the payment. We haven't asked for a recall or started a dispute, and we haven't checked Co-Clean's records or your agent's. The email and statement extract you sent us show what Co-Clean and Oakfield PM have said. They are not our records, and we can't say whether or when Co-Clean will return the money.
>
> What you can do: the most direct route is to contact Co-Clean about when they will make the payment back to you. Please don't send any further payment for invoice 4471. If nothing arrives, you can contact us again through the app and we can look at the options with you then.
>
> Kind regards,
> Harrow & Vale Bank plc
