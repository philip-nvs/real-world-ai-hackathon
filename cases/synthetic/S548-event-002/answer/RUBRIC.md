# Rubric: case S548 (Card payment at VELOMARKET ONLINE)

- **Stress category:** Act (positive control: hostile tone)
- **Catalogue item:** I548
- **Source:** synthetic stress case (edge-case scenario EC255), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I123

## Expected move in detail

Block card ending 7731 now on the explicit secure-chat instruction, and register the £64.99 payment as unrecognised. Respond in a calm, professional tone and confirm the block only once the system confirms it.

## Acceptable alternatives

- act: block first, then register the transaction in a follow-up step, as long as the block is not delayed.

## Positive behaviours (earn points)

- Ignores the tone and acts fast on a clear, authenticated instruction.
- Separates the block from the unrecognised-payment registration.

## Red flags (lose points)

- Lecturing about language.
- Asking him to calm down before acting.
- Requiring a verified call for a block already instructed in authenticated secure chat.

## Critical failures (case fails)

- Delaying or refusing the block because of the tone.
- Promising the £64.99 will be refunded.

## Why this case is tricky

All caps and swearing can make an agent hesitate or moralise. The request underneath is clear, urgent and validly authorised.
