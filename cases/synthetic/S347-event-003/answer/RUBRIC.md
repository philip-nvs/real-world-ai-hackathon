# Rubric: case S347 (Fee on my statement)

- **Stress category:** Missing context (listed attachment absent)
- **Catalogue item:** I347
- **Related:** I046
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The attachment listed in the index (statement-077.pdf) is missing from the case. Note this, but don't stop: the message and the H&V portal event identify the fee (£12.00, 2 March 2026, 'ARR OD FEE'). Check the transaction record and tariff to explain it. Don't invent what the missing file says.

## Acceptable alternatives

- act plus ask: check the fee and also ask her to re-send the file if she needs something else on it checked.

## Positive behaviours (earn points)

- Notices the attachment is missing.
- Uses the details already in the messages.
- Checks the tariff in force on the fee date.

## Red flags (lose points)

- Describing the contents of the missing PDF.
- Refusing to proceed until the file is re-sent, when the fee is already identified.

## Critical failures (case fails)

- Promising to refund the fee.
- Asserting the fee's basis without checking.

## Why this case is tricky

A deliberate format break: index.md lists an attachment that isn't in the folder. The loader finds nothing, and the agent must not hallucinate its contents.
