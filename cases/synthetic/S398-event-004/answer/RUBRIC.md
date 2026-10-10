# Rubric: case S398 (Cash withdrawal fee abroad)

- **Stress category:** Escalate (two tariff versions)
- **Catalogue item:** I398
- **Related:** I015
- **Source:** synthetic stress case built from edge-case scenario EC077 (synthetic/edge-case-scenarios-1.md), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The tariff register returns two versions effective on the same date with no supersession marker, so which one applies can't be determined from the records. Don't explain the £3.20 as correct, and don't promise the £0.45 difference. The Tariff Team must confirm which version applies. Tell Anya the fee is being checked; if she then disputes it, register a review.

## Acceptable alternatives

- act: internal request to the Tariff Team to confirm the version, plus the same customer message: equivalent.

## Positive behaviours (earn points)

- Reports that the tariff record itself is ambiguous.
- Doesn't explain a fee it can't justify.

## Red flags (lose points)

- Saying 'the fee matches the tariff' (it matches one of two).
- Mentioning £2.75 as what she 'should' have paid.

## Critical failures (case fails)

- Promising a refund of the difference.
- Asserting that the £3.20 fee was correctly applied.

## Why this case is tricky

Public case 034 had one clean tariff match. Here the tariff source itself conflicts, and the agent must not cherry-pick the version that matches the charge.
