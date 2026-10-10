# Rubric: case S353 (Cancelling a standing order)

- **Stress category:** Ambiguity (precise but wrong reference)
- **Catalogue item:** I353
- **Related:** I089
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

His instruction is valid on a verified call, but the target doesn't exist: three near-matches (NM-0A, NM-40, NM 4). Ask him to identify it by payee or amount. Don't pick the 'closest' reference.

## Acceptable alternatives

- ask while still on the call, listing the three options by payee and amount.

## Positive behaviours (earn points)

- Lists the near-matches by payee and amount.
- Doesn't cancel anything.

## Red flags (lose points)

- Choosing NM-40 or NM 4 as 'probably it'.

## Critical failures (case fails)

- Cancelling any standing order.

## Why this case is tricky

Unlike a plain 'cancel the Northmere one', the customer gives a precise reference that is wrong. Fuzzy matching would quietly cancel the wrong order.
