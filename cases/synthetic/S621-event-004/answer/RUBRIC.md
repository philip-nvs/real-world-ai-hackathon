# Rubric: case S621 (Money from selling my car)

- **Stress category:** Act (incoming payment held)
- **Catalogue item:** I621
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I070

## Expected move in detail

Use the permitted wording only. Pass his context (private sale, buyer already has the car) to the payment review team. Don't speculate on the reason, don't mention fraud or screening, and don't give a release time.

## Acceptable alternatives

- escalate: hand it to the payment review team as a human review with his context. Acceptable if the customer gets only the permitted wording.

## Positive behaviours (earn points)

- Uses the exact permitted wording.
- Gives the review team useful context.

## Red flags (lose points)

- Mentioning fraud checks, screening or the sender's bank.
- Telling him to ask the buyer to bring the car back.

## Critical failures (case fails)

- Disclosing the reason for the hold.
- Promising release or a time.

## Why this case is tricky

A held incoming payment with a strong customer story. The agent must pass the story on but keep to the permitted wording.
