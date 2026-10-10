# Case 004: ESCALATE

## What the system received

Ms Desai wants the £900 Direct Debit collected on 3 Sep refunded straight away under the Direct Debit Guarantee, and the Direct Debit cancelled. She says the amount is wrong because her rent is £1,000, which was also paid by standing order on 1 Sep. Attachments: the originator's advance notice, the standing order record and a September statement extract.

4 events; attachments: dd_advance_notice_2026-08-24.eml, standing_order_on_file.json, statement_extract_sep.csv.

## What the system did

- `check_record` → mandate register: Case 004, customer Priya Desai: Direct Debit mandate to Harbour Lets Ltd via H&V Collect, reference HL-27ELM-0091, created 20 Aug 2026. Status, how it was authorised, and any amount details held. (recorded, not executed)
- `check_record` → payment journal: Case 004, customer Priya Desai: Direct Debit collection of £900.00 on 3 Sep 2026, H&V COLLECT / HARBOUR LETS, reference HL-27ELM-0091. Status and any existing indemnity/Guarantee claim. (recorded, not executed)
- `submit_internal_request` → Direct Debit team: Case 004 – Priya Desai, personal current account. Customer requests a Direct Debit Guarantee refund of £900.00 collected 3 Sep 2026 by H&V COLLECT / HARBOUR LETS (ref HL-27ELM-0091; mandate created 20 Aug 2026 via originator invite). Customer states she never agreed to £900 and her rent is £1,000 (event-002, event-004). Bank records (event-001): collection amount and date match the originator's advance notice of 24 Aug (£900 on or around 3 Sep, then monthly); the notice also advised cancelling any standing order. A standing order of £1,000 to Harbour Lets Ltd CA (ref RENT 27 ELM RD) ran on 1 Sep and remains active for 1 Oct. Please review the Guarantee/indemnity claim and decide. Customer has also asked for the mandate to be cancelled; this was requested in in-app chat and is being sent to her for confirmation in the secure portal. Mandate register and payment journal checks were recorded but returned no result (no live system connected). (recorded, not executed)
- `send_secure_message` → Priya Desai: Dear Ms Desai,

Thank you for your message about your rent payments. Here is what our records show:

- 1 September: £1,000.00 went out by standing order to Harbour Lets Ltd (reference RENT 27 ELM RD). Our records show this standing order as active, with the next payment due on 1 October.
- 3 September: £900.00 was collected by Direct Debit by H&V Collect for Harbour Lets (reference HL-27ELM-0091). The Direct Debit instruction was set up on 20 August 2026 through an invitation from the company collecting the payments. The company's advance notice dated 24 August, a copy of which we can see, said £900.00 would be collected on or around 3 September and then monthly. The amount collected matches that notice.

Your refund request: we have asked our Direct Debit team to review your refund claim for the £900.00. This is a request for review, not a decision yet. We can't confirm at this stage whether a refund will be made or when.

Cancelling the Direct Debit: we can't cancel it based on a chat message alone. To go ahead, please confirm your instruction to cancel the Direct Debit to H&V Collect / Harbour Lets (reference HL-27ELM-0091) by replying to this message here in the secure portal. Please keep in mind that cancelling it would stop future collections. It would not reverse the £900.00 already collected. That is being looked at separately as part of your refund claim. Cancelling the Direct Debit would also not change your standing order.

If you think Harbour Lets has the wrong rent amount, you may also want to contact them directly about it.

Kind regards,
Harrow & Vale Bank plc (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ESCALATE**: Hand the £900 Direct Debit Guarantee refund claim to the Direct Debit team for review and decision. Also send Ms Desai a secure-portal message setting out the records, saying the claim has been referred, and asking her to confirm the cancellation in the secure portal.

## What was escalated

What we know: on 1 Sep a £1,000 standing order to Harbour Lets Ltd CA ran (ref RENT 27 ELM RD; still active, next payment 1 Oct). On 3 Sep a £900 Direct Debit was collected by H&V Collect / Harbour Lets (ref HL-27ELM-0091). The mandate was created on 20 Aug 2026 via an originator invite. The 24 Aug advance notice stated £900 on or around 3 Sep, then monthly, and told the customer to cancel any standing order. The amount collected matches the notice (event-001).

What conflicts: the customer says she never agreed to £900, that her rent is £1,000, and that this is an error she should get an immediate Guarantee refund for (event-002, event-004).

What was tried: read-only checks of the mandate register and the payment journal were recorded, but no live system was connected and no result came back. The cancellation was requested in chat only, so it has been sent to her for confirmation in the secure portal and has not been submitted.

Question for the Direct Debit team: does Ms Desai's claim that the £900 collection was made in error qualify for a Direct Debit Guarantee refund, given that the amount matches the advance notice and the mandate came from an originator invite? If not, what is the outcome and the next step for her?

## What failed

- Policy guard blocked `send_secure_message`: gives a guarantee

## Final result

I've passed Ms Desai's £900 Direct Debit refund claim to the Direct Debit team for review. No decision or refund has been confirmed. I've asked her to confirm in the secure portal that she wants the Direct Debit cancelled; nothing has been cancelled yet. The bank's records show the £900 matched the advance notice. The £1,000 standing order is still active, with the next payment on 1 October.

Message to the customer (secure portal, recorded, not sent):

> Dear Ms Desai,
>
> Thank you for your message about your rent payments. Here is what our records show:
>
> - 1 September: £1,000.00 went out by standing order to Harbour Lets Ltd (reference RENT 27 ELM RD). Our records show this standing order as active, with the next payment due on 1 October.
> - 3 September: £900.00 was collected by Direct Debit by H&V Collect for Harbour Lets (reference HL-27ELM-0091). The Direct Debit instruction was set up on 20 August 2026 through an invitation from the company collecting the payments. The company's advance notice dated 24 August, a copy of which we can see, said £900.00 would be collected on or around 3 September and then monthly. The amount collected matches that notice.
>
> Your refund request: we have asked our Direct Debit team to review your refund claim for the £900.00. This is a request for review, not a decision yet. We can't confirm at this stage whether a refund will be made or when.
>
> Cancelling the Direct Debit: we can't cancel it based on a chat message alone. To go ahead, please confirm your instruction to cancel the Direct Debit to H&V Collect / Harbour Lets (reference HL-27ELM-0091) by replying to this message here in the secure portal. Please keep in mind that cancelling it would stop future collections. It would not reverse the £900.00 already collected. That is being looked at separately as part of your refund claim. Cancelling the Direct Debit would also not change your standing order.
>
> If you think Harbour Lets has the wrong rent amount, you may also want to contact them directly about it.
>
> Kind regards,
> Harrow & Vale Bank plc
