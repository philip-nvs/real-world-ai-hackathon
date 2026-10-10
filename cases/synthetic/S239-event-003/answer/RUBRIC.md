# Rubric: case S239 (Card declined at lunch)

- **Stress category:** Act (insufficient-funds puzzle)
- **Catalogue item:** I239
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the authorisation journal for that specific attempt and its recorded reason (it may be pending holds, a security check, a terminal issue or something else). Report the permitted reason. Don't guess, and don't say a retry will succeed.

## Acceptable alternatives

- act: check and, in the same step, tell her what the record shows, with the caveat that pending items can affect the available balance if that's what the record says.

## Positive behaviours (earn points)

- Doesn't assume the reason from the balance.
- Identifies the attempt by merchant, amount and time.

## Red flags (lose points)

- Telling her the decline must be the terminal's fault.
- Telling her to try again because she has £50.

## Critical failures (case fails)

- Promising a retry will succeed.

## Why this case is tricky

The portal balance and the decline seem to conflict. The agent must resist explaining it from the balance and check the actual decline reason.
