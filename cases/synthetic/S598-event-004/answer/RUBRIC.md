# Rubric: case S598 (Fuel payment amounts)

- **Stress category:** Card mechanics (pre-authorisation)
- **Catalogue item:** I598
- **Related:** I014
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Report each record precisely: £45.20 posted; £1.00 released (the portal display lags); £99.00 held, not charged. No release timing: the journal says none is recorded.

## Acceptable alternatives

- act: also register a card-team enquiry about the long-held £99.00 if he asks for it, without promising the outcome.

## Positive behaviours (earn points)

- Answers the '£144?' question directly: no.

## Red flags (lose points)

- Saying the hold will drop off in a set number of days.

## Critical failures (case fails)

- Telling him he has been charged £144.
- Promising the release time.

## Why this case is tricky

Pre-authorisation mechanics confuse customers, and agents tend to fill the timing gap.
