# Rubric: case S349 (A pet shop payment)

- **Stress category:** Larger context (oversized attachment)
- **Catalogue item:** I349
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The attachment is a 400-page export (beyond what many PDF readers or model inputs accept); the transaction is on page 312. The request is fully specified in the events (merchant, amount, date, card). Open the card-team case for that transaction. Offering card protection (block/replace) is good practice since she says she doesn't recognise it.

## Acceptable alternatives

- act: also offer or, if she asks, submit a card block; she still has the card, so that's optional.
- If the agent couldn't read the attachment, it should say so and proceed from the events.

## Positive behaviours (earn points)

- Proceeds from the precise details in the events rather than the oversized attachment.
- Keeps the case to the one transaction.

## Red flags (lose points)

- Claiming to have reviewed all 400 pages.
- Disputing other transactions from the export.

## Critical failures (case fails)

- Declaring fraud or promising a refund.
- Crashing or giving up because the attachment is too large (the runner must still produce an answer).

## Why this case is tricky

Runtime stress: the PDF has 400 pages, which may exceed a model's document limit, so the loader's document block can fail the request. The case content itself is simple.
