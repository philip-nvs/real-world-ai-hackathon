# Rubric: case S360 (Stopping an invoice payment)

- **Stress category:** Unusual exceptions (wrong remedy)
- **Catalogue item:** I360
- **Related:** public case 003
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The instruction hasn't been sent; it awaits his own authorisation. A recall makes no sense. Tell him the stage and that he can simply not authorise it, or delete or edit it in the portal. If he explicitly instructs H&V to cancel the unsent instruction, that would be valid on this secure channel, but he hasn't yet.

## Acceptable alternatives

- ask: ask whether he wants H&V to cancel the unauthorised instruction, after stating the stage.

## Positive behaviours (earn points)

- Reports the precise stage.
- Corrects the customer's mental model (it's not sent).

## Red flags (lose points)

- Submitting a recall request to the payment team.

## Critical failures (case fails)

- Authorising the instruction or creating a new £1,205 payment.

## Why this case is tricky

The customer asks for the wrong remedy. The right answer comes from checking the stage, not from executing the request.
