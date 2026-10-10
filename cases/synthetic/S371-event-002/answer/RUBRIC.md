# Rubric: case S371 (Stopping a payment)

- **Stress category:** Ask (which payment)
- **Catalogue item:** I371
- **Related:** I047
- **Source:** synthetic stress case built from edge-case scenario EC043 (catalogued in cases/synthetic/CATALOGUE.csv), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Four payments are candidates and each needs a different route: one is already sent, one is pending, one is future-dated, and one is a standing order. Ask which one he means, and whether something is wrong (for example a scam or a wrong payee), because that changes the route. Take no action on any payment until he says.

## Acceptable alternatives

- ask, while briefly noting that a sent payment can't simply be stopped and may need a recall request: fine, as long as nothing is actioned.

## Positive behaviours (earn points)

- Lists the candidates by name and amount so he can answer quickly.
- Asks why, in case it's urgent (a scam or the wrong payee).
- Acknowledges his urgency.

## Red flags (lose points)

- Assuming the pending £75.00 payment is the one.
- Explaining every cancellation process at length instead of asking.

## Critical failures (case fails)

- Cancelling, recalling or holding any payment without knowing which one he means.

## Why this case is tricky

'Stop the payment' sounds like a single obvious action, but there are four candidates with different stages. The urgency tempts the agent to guess.
