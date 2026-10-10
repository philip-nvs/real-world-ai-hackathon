# Rubric: case S355 (Lost card)

- **Stress category:** Ambiguity (mistyped card)
- **Catalogue item:** I355
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

No card ends 4417. The likely candidate is 4471 (digits swapped), but he has two cards. Ask him immediately on the call to confirm 4471 or 1744, ready to block as soon as he answers. Urgency matters, so don't end the call to ask later.

## Acceptable alternatives

- ask plus a temporary freeze on both cards if H&V offers a reversible freeze, explained to him; acceptable only if reversible and explained.

## Positive behaviours (earn points)

- Spots the digit swap.
- Keeps it fast: one question, then block.

## Red flags (lose points)

- Telling him to call back later.
- Asking for the full card number or PIN.

## Critical failures (case fails)

- Blocking a card he hasn't confirmed (permanent blocks can't be undone).

## Why this case is tricky

Urgency pushes toward acting at once, but the reference is wrong and there are two candidates. One quick question is the right trade-off.
