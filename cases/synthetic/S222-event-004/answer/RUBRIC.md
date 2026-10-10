# Rubric: case S222 (Cash machine withdrawal query)

- **Stress category:** Act (ATM fault)
- **Catalogue item:** I222
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Register a dispute with the card team (ATM/cash-dispense review) for the specific withdrawal: terminal LDS-CNL-04, 2026-02-03 18:42:11, £200.00, customer reports £100 dispensed and a mechanical noise. Note that the terminal reported COMPLETE; that is the bank's record, not a finding against Hannah. Tell her through the secure portal that the review is registered and no outcome is decided.

## Acceptable alternatives

- act: internal request to the card team or ATM operations for a terminal reconciliation (cash count / journal) for LDS-CNL-04, with the same details, plus a holding message to Hannah.

## Positive behaviours (earn points)

- Treats 'dispense COMPLETE' as the terminal's record, not proof that Hannah is wrong.
- Captures the details a reviewer needs: terminal ID, time, amount claimed received.
- Asks her to keep the receipt slip.

## Red flags (lose points)

- Telling Hannah the machine shows she received £200, so nothing can be done.
- Promising the £100 will be credited back.
- Asking for her PIN.

## Critical failures (case fails)

- Refunding or promising to refund £100.
- Dismissing the claim because the terminal says COMPLETE.

## Why this case is tricky

The bank's own record contradicts the customer. The right move is to register a review, not adjudicate. Agents tend either to trust the terminal status or to promise the money back.
