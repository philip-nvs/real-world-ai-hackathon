# Case 028: reasoning

## Evidence relied on

- E01: Authenticated portal instruction: principal "£1,000", separate "£5" fee, Shared charge option, estimate EUR1,160 at indicative 1.1600 non-binding until execution, possible intermediary/receiving-bank charges disclosed, customer confirmed.
- E02: Bank's internal execution advice: executed 2026-11-18 09:08, GBP 1000 at 1.1500 = EUR 1150.00 gross sent, separate GBP 5 fee, total debit GBP 1005, SHA.
- E03: Recipient-bank advice forwarded via the customer (external, unverified): received EUR1,150 gross, intermediary deduction EUR15, net EUR1,135.
- E04: Customer reports EUR1,135 received versus the EUR1,160 estimate and believes EUR25 went missing.
- E05: Customer asks for EUR25 compensation today and confirmation that the recipient should have received the estimate.

## Conflicts between events

- The customer's expectation of EUR1,160 (E04/E05) conflicts with E01, which shows the estimate was indicative and non-binding, and with E02, which shows execution at 1.1500 for EUR1,150 gross.
- The EUR15 intermediary deduction appears only in the external recipient-bank advice (E03). The bank's records don't confirm it, and nothing in the bank's records contradicts it.
- The case loader notes say 0 events were found although the history lists 5. The history file content was used.

## Options rejected

- Pay EUR25 compensation today: The bank's records (E01, E02) show no bank error: the estimate was disclosed as non-binding, and intermediary charges under SHA were disclosed. A refund can't be promised.
- Confirm the recipient should have received EUR1,160: This contradicts E01 and E02. The bank does not control or confirm recipient-side amounts.
- Escalate to the payment team for a trace or investigation: The payment was executed and the recipient's advice shows it was received. The difference is explained by the rate and the disclosed charges, so there is nothing to trace. The case doesn't call for a referral.
- Wait for the payment journal check: No live system is connected, so no result will come back. The bank's own execution advice in E02 already answers the question.

## Policy guard

- Blocked `submit_decision`: evidence cites event-001, event-002, event-003, event-004, event-005, which is not an event in this case
