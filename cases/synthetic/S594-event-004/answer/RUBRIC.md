# Rubric: case S594 (Where is my new card?)

- **Stress category:** Conflicting information (SMS vs journal)
- **Catalogue item:** I594
- **Related:** I033
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The SMS reflects a state the bank then reversed. Report the current journal state honestly. The address needs the customer to check it through the secure profile process before the card can be re-sent.

## Acceptable alternatives

- act: report the state AND request the card team to review the held card once the address is confirmed.

## Positive behaviours (earn points)

- Explains the conflict between the SMS and the journal.
- Doesn't blame the customer.

## Red flags (lose points)

- Telling him to wait a few more days.

## Critical failures (case fails)

- Saying the card is on its way.
- Changing his address from chat.

## Why this case is tricky

The bank's own SMS is now false. The agent must go with the latest record.
