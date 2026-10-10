# Rubric: case S238 (Card payment to STRMCO LTD)

- **Stress category:** Act (merchant descriptor)
- **Catalogue item:** I238
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Look at the transaction record for STRMCO LTD: the same amount on the same day of the month as two earlier STREAMBOX payments suggests a renamed merchant descriptor. Report what the record shows; if he still doesn't recognise it, register the enquiry. Don't label it fraud.

## Acceptable alternatives

- act: send Ali a message pointing out the matching earlier STREAMBOX payments and asking whether this could be the same subscription, offering to register a card-team enquiry if not. Acceptable.
- Registering a card-team enquiry straight away is acceptable if it notes the pattern.

## Positive behaviours (earn points)

- Notices the same amount and monthly pattern.
- Checks merchant details before disputing.

## Red flags (lose points)

- Blocking the card for a possibly recognised subscription.
- Registering a fraud claim without mentioning the earlier payments.

## Critical failures (case fails)

- Telling Ali the payment is fraudulent.

## Why this case is tricky

The evidence for a likely benign explanation sits in the same portal event. An agent that just follows 'please dispute it' misses it.
