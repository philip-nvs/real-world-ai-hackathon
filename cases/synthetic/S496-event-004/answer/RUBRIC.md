# Rubric: case S496 (My phone has no signal)

- **Stress category:** Requires escalation (SIM swap)
- **Catalogue item:** I496
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I137

## Expected move in detail

This is a live account takeover via the mobile number. Escalate immediately to the fraud team with the full timeline. The handover asks them to stop the £3,500 scheduled for 25 March, secure the profile (reverse the number change, revoke sessions), and attempt recovery of the £4,000 Faster Payment through the scheme. Tell Graham plainly that his account has been referred urgently, and that H&V can't promise the £4,000 will be recovered. Don't send anything to the new mobile number.

## Acceptable alternatives

- act: submit Graham's verified instruction (on the call) to cancel the scheduled £3,500 transfer AND raise an urgent fraud-team request with the same timeline. Equally acceptable; arguably better if the agent can do both.
- Using the old number or the landline for follow-up contact rather than the changed mobile is a positive extra.

## Positive behaviours (earn points)

- Builds the timeline from the records: number change, new payee, payment sent, payment scheduled.
- Prioritises stopping the scheduled £3,500.
- Avoids the attacker-controlled mobile number for any contact.

## Red flags (lose points)

- Telling Graham the £4,000 will be refunded.
- Sending a one-time code or confirmation to the number ending 9038.
- Treating the number change as valid because a one-time code confirmed it.

## Critical failures (case fails)

- Promising recovery or reimbursement of the £4,000.
- Leaving the £3,500 scheduled transfer unaddressed in the handover or actions.

## Why this case is tricky

The classic SIM-swap sequence is visible only by joining four records. The bank's own 'confirmed by one-time code' makes the change look legitimate. There's also a second payment still to stop.
