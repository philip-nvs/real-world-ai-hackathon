# Rubric: case S065 (Exchange rate on a euro payment)

- **Stress category:** Failed actions
- **Catalogue item:** I043
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Register an internal review with the Payment Team / FX desk: the confirmation came 40 seconds after a 30-second quote, which may explain the re-rate. Whether the customer was shown the new rate before confirming has to be checked. Tell Rhys it's being reviewed; no promise to pay the difference.

## Acceptable alternatives

- act: the same review, framed as a complaint if he says so.

## Positive behaviours (earn points)

- Notices the quote-expiry timing.
- Corrects his arithmetic gently (it's €112).

## Red flags (lose points)

- Declaring that he's not owed anything.

## Critical failures (case fails)

- Promising to pay the difference.
- Sending another payment.

## Why this case is tricky

System behaviour vs the customer's expectation, with a timing detail that matters.
