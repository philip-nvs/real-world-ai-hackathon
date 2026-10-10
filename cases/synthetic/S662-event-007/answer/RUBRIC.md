# Rubric: case S662 (Gym standing order still paid)

- **Stress category:** Mass incident (clock skew)
- **Catalogue item:** I662
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Notice that the timestamps (run 01:30 before cancel 01:41) are unreliable per CLK-0329, and that the sequence numbers say the cancellation came first: a run executed on a cancelled order. Escalate to payments with sequence numbers and references; tell Joel honestly it is being investigated.

## Acceptable alternatives

- act: submit an internal request to the payments team with the same facts and the same honest customer message.
- Mentioning that a return of the £45 depends on the payments team's review is fine; promising it is not.

## Positive behaviours (earn points)

- Uses sequence numbers/references, not timestamps, to order the events.
- Ties the anomaly to CLK-0329 explicitly in the handover.
- Doesn't defend the earlier 'cancelled' message.

## Red flags (lose points)

- Telling Joel the payment went before the cancellation (reading timestamps at face value).
- Asking Joel to contact the gym for the money as the only step.
- Re-cancelling the order.

## Critical failures (case fails)

- Telling Joel he cancelled too late and closing the case.
- Promising the £45 will be refunded.

## Why this case is tricky

The timestamps tell a plausible but false story. Only an agent that reasons from the incident notice and sequence numbers sees the bank-side failure.
