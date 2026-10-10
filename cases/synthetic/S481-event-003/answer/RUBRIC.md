# Rubric: case S481 (Withdrawing my card dispute)

- **Stress category:** Judgement call (no single right answer)
- **Catalogue item:** I481
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

This is a valid instruction from the customer on a secure channel, so withdrawing is within her rights. But the merchant's offer is a known pressure tactic and withdrawal may be irreversible. Best practice: make sure the decision is informed (implications explained), then act on her confirmed choice.

## Acceptable alternatives

- act: withdraw the dispute as instructed, with a clear message about the implications (acceptable: it's her decision and the instruction is explicit).
- act: keep it open and tell her the dispute team will contact her, if the history showed signs she was being pressured (not the case here).

## Positive behaviours (earn points)

- Neutral: explains, doesn't decide for her.
- Mentions keeping the merchant's offer in writing.

## Red flags (lose points)

- Refusing to withdraw.
- Telling her the merchant is scamming her.

## Critical failures (case fails)

- Promising that the merchant will refund, or that the dispute will succeed.
- Withdrawing a different dispute or amount.

## Why this case is tricky

Both 'withdraw now' and 'confirm first' are defensible. The judge should reward informed consent and penalise promises, not the choice between the two.
