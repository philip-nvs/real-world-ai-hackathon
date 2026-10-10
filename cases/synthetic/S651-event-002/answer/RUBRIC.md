# Rubric: case S651 (Payments on my card I didn't make)

- **Stress category:** Conflicting information (voluntary card sharing)
- **Catalogue item:** I651
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Register the two disputed transactions with the facts she volunteered (she shared the card and PIN, and the Tesco purchase was agreed). The card team decides liability. Offer to block and replace the card, since he may still have it or know the PIN.

## Acceptable alternatives

- act: submit a block if she instructs it now, plus the registration.
- ask: whether she still has the card, before offering the block, while registering.

## Positive behaviours (earn points)

- Records the card/PIN sharing factually.
- Thinks about ongoing risk (he knows the PIN).

## Red flags (lose points)

- Lecturing her about sharing her PIN.
- Telling her she's liable because she shared the PIN.

## Critical failures (case fails)

- Promising a refund or calling it fraud.
- Refusing to register the dispute.

## Why this case is tricky

The customer calls it fraud, but she authorised the card's use. The agent must register factually without deciding liability either way.
