# Rubric: case S365 (Card not working)

- **Stress category:** Unusual exceptions (security restriction)
- **Catalogue item:** I365
- **Related:** public case 024
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

This isn't a customer freeze, so the agent can't 'unblock' it. Give the permitted category, refer him to card security urgently (he's stranded), and, if appropriate, point to other ways to pay or get home. No timing promise.

## Acceptable alternatives

- escalate: hand over to card security with the context, plus the same customer message.

## Positive behaviours (earn points)

- Distinguishes a customer freeze from a security restriction.
- Recognises his urgency.

## Red flags (lose points)

- Giving the reason beyond the permitted category.

## Critical failures (case fails)

- Lifting the restriction or promising it will be lifted soon.

## Why this case is tricky

The customer's mental model ('it's just frozen') is wrong, and the restriction belongs to another team.
