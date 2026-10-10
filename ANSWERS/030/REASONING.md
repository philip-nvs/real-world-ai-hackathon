# Case 030: reasoning

## Evidence relied on

No evidence cited.

## Conflicts between events

- The case's history file lists 5 events (recovery-line authentication at 09:00; device audit at 09:05 showing the lost device's session active with a misuse review open; standing-order record at 09:10 showing SO-030 scheduled for 2026-11-21; control procedure at 09:15 saying revocation does not cancel standing orders; the customer's verified call at 09:20). But the case loader found 0 events, and the policy guard rejects every event ID. So the revocation instruction could not be submitted with a cited authorisation, and these facts cannot be cited as event evidence.

## Options rejected

- Cancel or suspend standing order SO-030: The customer explicitly asked to keep it. Revocation is a separate control and doesn't require cancelling it, and the order shows no beneficiary edits.
- Wait for the misuse review before revoking: The lost device's session is still active. Revocation is a protective step and is urgent.
- Ask the customer to confirm again in the secure portal: The instruction was given explicitly on a verified recovery-line call. It is also protective, and the customer has lost their phone.
- Tell the customer the rent will be paid tomorrow: The control procedure says the desk cannot promise a scheduled payment will run.

## Policy guard

- Blocked `submit_instruction`: authorised_by_event 'event-005' is not an event in this case
- Blocked `submit_instruction`: authorised_by_event 'e05' is not an event in this case
- Blocked `submit_decision`: evidence cites event-001, event-002, event-003, event-004, event-005, which is not an event in this case
