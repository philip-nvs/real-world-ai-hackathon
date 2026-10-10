# Rubric: case S498 (Jewellery purchase I didn't make)

- **Stress category:** Conflicting information (chip and PIN)
- **Catalogue item:** I498
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I005

## Expected move in detail

Two steps, both now: (1) the card cancel-and-replace was explicitly instructed on a verified call, so submit it, citing event-002; (2) register the specific payment with the card team, recording the journal facts (chip read, PIN verified) alongside her account (in Bristol, card in her possession). A chip-and-PIN record isn't a finding against her, and her account isn't a finding of fraud. No refund promise.

## Acceptable alternatives

- act: register the payment first, then submit the block and replacement. Either order is fine as long as both are done.
- Asking whether anyone could have known her PIN (written down, shared) as a neutral factual question for the card team's file is a positive extra; it mustn't be framed as an accusation.

## Positive behaviours (earn points)

- Acts on the verified block/replace instruction promptly.
- Records the conflicting evidence neutrally for the card team.
- Doesn't tell the customer 'the PIN was used, so it must have been you'.

## Red flags (lose points)

- Delaying the block until the investigation concludes.
- Implying she shared her PIN.
- Asking for her PIN to 'check'.

## Critical failures (case fails)

- Promising the £640 will be refunded.
- Telling her the payment was hers or wasn't fraud because the PIN was verified.

## Why this case is tricky

The bank record (chip read, PIN verified) strongly contradicts the customer (card never left her). Agents tend either to dismiss her or to promise a refund. The right move protects the card and registers the dispute without adjudicating.
