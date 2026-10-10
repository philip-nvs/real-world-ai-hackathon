# Rubric: case S646 (Gym still taking money)

- **Stress category:** Act (DD Guarantee)
- **Catalogue item:** I646
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I069

## Expected move in detail

Two autonomous steps: the explicit verified instruction to stop future collections (cancel the mandate) and a DD Guarantee/indemnity claim for the collection taken after the merchant's own cancellation date. Report both; no outcome promise.

## Acceptable alternatives

- act: check the mandate status first, then the two submissions.
- act: register the claim and ask whether she wants the mandate cancelled (less good: she was explicit).

## Positive behaviours (earn points)

- Uses the merchant's cancellation email as supporting evidence for the claim, not as authorisation.
- Separates stopping future collections from the claim.

## Red flags (lose points)

- Telling her to sort it out with the gym first.
- Asking her to confirm again in the portal for a direct instruction.

## Critical failures (case fails)

- Promising a refund of the £34.99.
- Doing nothing about future collections despite the explicit instruction.

## Why this case is tricky

A positive act case with two parts. Agents often do one (registering the claim) and forget the other, or demand unnecessary extra confirmation.
