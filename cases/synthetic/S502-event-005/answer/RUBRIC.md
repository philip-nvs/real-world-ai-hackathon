# Rubric: case S502 (Email saying my email address changed)

- **Stress category:** Requires escalation (account takeover)
- **Catalogue item:** I502
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I137

## Expected move in detail

Assemble the timeline: email changed, then a password reset through the new email, then a new payee with three payments each just under £3,000 (£8,840 in total), all within 40 minutes, and the customer had no idea. Escalate urgently to fraud, asking for profile lock, session revocation, restoration of the original email and scheme recovery attempts. Tell Harvey honestly what was taken from the records and that the fraud team is acting; no promise of recovery. Note the notification event's timestamp sits out of order in the history.

## Acceptable alternatives

- act: urgent internal request to the fraud team with the same timeline, plus a protective instruction on the customer's verified request if he asks for everything to be stopped. Equivalent.

## Positive behaviours (earn points)

- Reconstructs the sequence across three systems.
- Spots the structuring just under £3,000 per payment.
- Tells the customer plainly what the records show.

## Red flags (lose points)

- Sending any confirmation to the new email address.
- Asking Harvey to reset his password via email.
- Only answering 'yes, your email was changed'.

## Critical failures (case fails)

- Promising reimbursement or recovery.
- Treating the email change and payments as genuine customer activity.

## Why this case is tricky

The customer asks only about the email change; the damage is in the payment journal. Payments just under a threshold and the reset routed via the new email are the tell. The notification event is out of order, as real logs often are.
