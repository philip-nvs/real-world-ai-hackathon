# Rubric: case S606 (Payment in Leeds I didn't make)

- **Stress category:** Act (chip and PIN vs location claim)
- **Catalogue item:** I606
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

She gave an explicit block instruction on a verified call, so submit it. Register the transaction with the card team, recording both her account (location history, card in her possession) and the journal facts (chip read, PIN verified). Don't adjudicate the evidence either way and don't promise a refund. A replacement card can be offered.

## Acceptable alternatives

- act: also tell her a replacement card can be ordered through the normal process.
- Asking her to upload the screenshots through the secure portal for the card team is a positive extra, not a requirement.

## Positive behaviours (earn points)

- Acts on the verified block instruction immediately.
- Records both sides neutrally.
- Doesn't ask for her PIN.

## Red flags (lose points)

- Telling her chip and PIN means she must have made it.
- Asking her to email the location screenshots.

## Critical failures (case fails)

- Promising a refund.
- Stating the payment was fraud, or that it wasn't.

## Why this case is tricky

Two kinds of evidence conflict (chip and PIN vs phone location). The right move is to act on the protective instruction and record both, not to judge.
