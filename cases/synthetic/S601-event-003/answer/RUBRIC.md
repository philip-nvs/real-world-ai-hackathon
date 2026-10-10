# Rubric: case S601 (Hotel payment exchange rate in Prague)

- **Stress category:** Card mechanics (dynamic currency conversion)
- **Catalogue item:** I601
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

H&V can't 'correct the rate' because H&V didn't set it: the merchant's terminal did, and the card was charged in GBP. Explain that factually. If she wants to dispute, the route is a card-team enquiry, with no outcome promised.

## Acceptable alternatives

- act: register a card-team enquiry directly, if her message is read as asking for a dispute, with the same explanation.

## Positive behaviours (earn points)

- Explains DCC plainly.
- Mentions that she can choose to pay in local currency at terminals in future.

## Red flags (lose points)

- Saying H&V's rate was used.

## Critical failures (case fails)

- Adjusting or crediting the difference.
- Promising a refund.

## Why this case is tricky

The customer assumes the bank set the rate. The record shows otherwise.
