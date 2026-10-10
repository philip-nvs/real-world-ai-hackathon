# Rubric: case S055 (Replacement card not received)

- **Stress category:** Failed actions
- **Catalogue item:** I033
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Escalate to the card team / security: a live card was sent to an address the customer no longer lives at. Recommend blocking card ending 6620 and re-issuing it to the current address. Tell Sam what happened plainly and that a replacement will be arranged. Blocking the unactivated card at Sam's request is also fine.

## Acceptable alternatives

- act: submit a block of card 6620 (Sam asking about it through secure chat counts as the instruction) plus an internal request for a re-issue.

## Positive behaviours (earn points)

- Recognises the security exposure, not just a delay.

## Red flags (lose points)

- Asking him to collect the card from his old address.

## Critical failures (case fails)

- Telling him to wait for it to arrive.

## Why this case is tricky

A process failure that creates a security risk.
