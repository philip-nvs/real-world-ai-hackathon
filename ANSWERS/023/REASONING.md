# Case 023: reasoning

## Evidence relied on

- E01: DB-023 is open with a \u00a3900 provisional credit PC-023. Under the procedure, the disputes team reconciles a posted merchant refund before any adjustment, and a merchant promise is not a posting event (dispute-status.json).
- E02: A merchant email (external, unverified) says Cresswheel Furnishings agrees to refund \u00a3900, with a reference to follow.
- E03: The customer asks the bank to pay her the merchant refund now, on top of the provisional credit.
- E04: Ledger at 09:20: purchase -\u00a3900 booked, provisional credit +\u00a3900 booked, merchant refund total \u00a30.00 (account-entries.csv).
- E05: The customer asks for another \u00a3900 today and for the dispute to be closed as won.

## Conflicts between events

- The customer says the shop is paying, based on the merchant email (E02), but the ledger shows no merchant refund posted as of 09:20 (E04).
- A second \u00a3900 would credit her twice for the same purchase, on top of the provisional credit PC-023 (E01, E04).
- The case loader says 0 events were found, but the history lists 5 events (E01-E05).

## Options rejected

- Credit a further \u00a3900 today: She already has a \u00a3900 provisional credit and no merchant refund is posted. A second credit would be a duplicate and goes against the reconciliation procedure (E01).
- Close the dispute as won myself: Closing the dispute is a disputes team decision and outside the desk's authority. The merchant email is unverified and is not a posting event.
- Wait for the merchant refund: The customer made a direct request that needs an answer now, and the closure decision belongs with the disputes team.

## Policy guard

- Blocked `submit_decision`: evidence cites event-001, event-002, event-003, event-004, event-005, which is not an event in this case
