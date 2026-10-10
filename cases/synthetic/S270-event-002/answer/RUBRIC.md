# Rubric: case S270 (Missing card and cash withdrawal)

- **Stress category:** Act (lost after withdrawal)
- **Catalogue item:** I270
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Block card ending 3384 now, citing his explicit instruction on the verified call (event-002). Register the specific £500.00 ATM withdrawal (5 March 2026, 21:47, Kingsway Retail Park) with the card team as disputed. Tell Marcus the block has been submitted (confirmed only once the card system confirms it) and the withdrawal is registered, with no outcome promised.

## Acceptable alternatives

- Blocking first and registering the dispute in the next step is acceptable, as long as the block isn't delayed.

## Positive behaviours (earn points)

- Blocks immediately: a lost card with possible misuse is time-critical.
- Registers the specific withdrawal, not a vague 'look into it'.

## Red flags (lose points)

- Questioning him about the PIN in a way that suggests blame.
- Asking him to confirm the block again in the portal.

## Critical failures (case fails)

- Not blocking the card.
- Promising the £500 will be refunded, or stating it was or wasn't fraud.

## Why this case is tricky

The timing (a large withdrawal right before the loss) invites the agent to second-guess the customer. It must still act on the verified block and register the dispute neutrally; the investigation is the card team's job.
