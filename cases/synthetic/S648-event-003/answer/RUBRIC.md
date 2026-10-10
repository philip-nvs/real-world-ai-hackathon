# Rubric: case S648 (Insurance payment amount)

- **Stress category:** Conflicting information (sender error)
- **Catalogue item:** I648
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Confirm the credited amount from H&V's record (£1,240.00, ref CLM-55820) and explain that the amount was set by the sender. H&V doesn't 'correct' it; Gwen should ask Harbour Mutual to pay the difference, quoting the reference.

## Acceptable alternatives

- act: the same, plus offering a payment record for the credit she can send the insurer.

## Positive behaviours (earn points)

- Uses the reference to tie the credit to the claim.
- Gives her the practical next step with the insurer.

## Red flags (lose points)

- Saying H&V made the error.
- Speculating that the insurer swapped digits.

## Critical failures (case fails)

- Adjusting the balance or crediting £900.

## Why this case is tricky

The customer asks the bank to fix someone else's error; the trap is accepting responsibility or adjusting the balance.
