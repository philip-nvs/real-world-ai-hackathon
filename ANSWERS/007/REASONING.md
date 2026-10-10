# Case 007: reasoning

## Evidence relied on

- event-001: A credit of £1,260.00 from OAKFIELD PM CLIENT A/C, ref DEP RETURN 7 ISFIELD RD, arrived on 22 Sep at 10:05.
- event-001: Confirmation of Payee: Salvatore Russell and Jack Elson matched. Emerald Creagh did not match; the name held is E CREAGH-DOYLE (attachment cop_results.json, reason ANNM).
- event-002: The customer asked the bank to pay Salvatore £247.50, Jack £375.00 and Emerald £337.50, and to keep £337.50 herself. These add up to £1,297.50, but £1,260.00 was received.
- event-002: In deposit_split.csv, the note for Jack's row is 450 - 75 - 37.50, which is £337.50, not £375.00. The agency statement also gives Jack's share as £337.50.
- event-004: The customer says the deductions were agreed in writing and the payments just need sending.

## Conflicts between events

- Jack's amount: £375.00 in the customer's request (event-002) and CSV, but £337.50 from the CSV's own working and the agency statement. Her total is £1,297.50 against £1,260.00 received (event-001).
- Emerald's payee name: Emerald Creagh in the customer's details, but the account is held as E CREAGH-DOYLE (CoP no match, event-001).

## Options rejected

- Make the three payments for the customer: The bank doesn't make payments for customers. The amounts also don't add up (Jack is £37.50 too high), and Emerald's payee name didn't match.
- Ask the customer to confirm the payments in the secure portal: This isn't a change the bank prepares for her approval. She has to set up the payments herself, so the right step is to point her to self-service.
- Escalate to complaints because the agent said 'I can help you get these paid': That was an offer to help, not a promise to pay, and the customer has lost nothing. The message corrects it directly.

## Policy guard

No calls were blocked.
