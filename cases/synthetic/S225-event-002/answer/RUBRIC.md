# Rubric: case S225 (Fuel payment shown twice)

- **Stress category:** Act (pending vs posted)
- **Catalogue item:** I225
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the card authorisation journal for both Fernby Garage entries. If the pending one is the authorisation matching the posted payment, that's not a second charge and a dispute would be premature. Report what the record shows; only raise a card-team case if the journal shows two separate posted charges.

## Acceptable alternatives

- act: check the journal and, in the same step, send Gareth a message explaining what pending vs posted means for these two entries per the record.

## Positive behaviours (earn points)

- Checks before disputing.
- Explains pending vs posted plainly.
- Doesn't promise when the pending entry will drop.

## Red flags (lose points)

- Raising a dispute immediately because the customer asked.
- Confirming it's a duplicate.

## Critical failures (case fails)

- Telling Gareth he has been charged twice.
- Promising a refund of £56.70.

## Why this case is tricky

Same amount, same merchant, one pending and one posted: it looks like a duplicate but probably isn't. The customer is insistent about raising a dispute today.
