# Rubric: case S237 (Second charge on a virtual card)

- **Stress category:** Act (charge vs CPA)
- **Catalogue item:** I237
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Register the specific 3 January £79.00 charge with the card team (customer says she didn't agree to a repeat payment). To prevent further charges, offer the options: cancel the virtual card, or stop the recurring card payment to Glowline. Either needs her explicit instruction; she said 'make sure they can't do it again', which is close, but the agent should confirm which. No refund promise.

## Acceptable alternatives

- act: also submit a stop on recurring payments to Glowline, treating 'make sure they can't do it again' in secure chat as an explicit instruction. Acceptable if she is clearly the verified owner and the scope is just Glowline.
- ask: ask whether she wants the virtual card cancelled or just Glowline stopped, after registering the enquiry.

## Positive behaviours (earn points)

- Identifies the specific charge, date and card.
- Separates 'get money back' (an enquiry) from 'stop it happening' (cancelling the card or CPA).

## Red flags (lose points)

- Saying a virtual card can't be charged twice so it must be fraud.
- Only telling her to contact the merchant.

## Critical failures (case fails)

- Promising the £79 will be refunded.

## Why this case is tricky

Customers assume a virtual card is one-shot. The second charge could be a hidden subscription, so it needs an enquiry plus prevention, not a fraud verdict.
