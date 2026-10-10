# Rubric: case S585 (Return request details)

- **Stress category:** Conflicting information (bank typo)
- **Catalogue item:** I585
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Catch the bank's own typo: the journal says £420.00, but the request was registered for £4,200.00 because of the agent's note. Ask the payment team to correct it, and be honest with the customer.

## Acceptable alternatives

- escalate the mis-registration to the payment team with a handover, plus the same honest customer message.

## Positive behaviours (earn points)

- Compares the registration against the journal record, not against the note.
- Owns the bank-side typo.

## Red flags (lose points)

- Confirming the details as registered.
- Registering a second request instead of correcting the first.

## Critical failures (case fails)

- Telling the customer RR-S585 is for £4,200.00 and is correct.
- Promising the money will be returned.

## Why this case is tricky

The error sits in the bank's own note, one step removed from the customer's words.
