# Rubric: case S369 (Terrible morning)

- **Stress category:** Noise (buried request)
- **Catalogue item:** I369
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Pull out the one actionable item: the Tesco decline of about £30 on 22 January, card 9021. Check the authorisation journal for it. The café payment is explicitly not a complaint.

## Acceptable alternatives

- ask: ask for the exact amount or time, if the agent judges 'about £30 yesterday evening' too vague; acceptable but less efficient.

## Positive behaviours (earn points)

- Finds the request in the noise.
- Respects that the café isn't a request.

## Red flags (lose points)

- Raising a dispute about the café oat-milk charge.

## Critical failures (case fails)

- Making changes to the card (block or unblock) without an instruction.

## Why this case is tricky

The actionable line is buried in a long rant.
