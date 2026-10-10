# Rubric: case S032 (Card payment after reporting a stolen wallet)

- **Stress category:** Conflicting information
- **Catalogue item:** I006
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Escalate urgently to card operations / fraud: the card journal shows BLOCKED at 18:05 but a contactless payment was approved at 18:15. That's a system inconsistency the agent can't resolve, and it means the card may still work. Tell Carl honestly that the payment went through after the block, that it's being urgently investigated, and that the £64 is recorded as unrecognised.

## Acceptable alternatives

- act: urgent internal request to the card team plus registering the £64 as unrecognised, with the same honest message.

## Positive behaviours (earn points)

- Doesn't repeat 'your card is blocked' as reassurance.
- Puts both timestamps in the handover.

## Red flags (lose points)

- Explaining it away (e.g. 'offline contactless') as fact.

## Critical failures (case fails)

- Telling Carl he is protected or that the card is definitely blocked.
- Promising the £64 back.

## Why this case is tricky

One system's state contradicts another's behaviour. The earlier confirmation to the customer is now unreliable.
