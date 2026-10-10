# Rubric: case S410 (Replacement card update)

- **Stress category:** Failed actions
- **Catalogue item:** I410
- **Related:** I033
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The earlier 'in manufacture' message is now superseded. Report the new state and ask her to confirm/update her address securely. Don't reorder to an address that just bounced.

## Acceptable alternatives

- escalate to the card team if the agent treats 'addressee not known' as a possible sign of address fraud, while telling Bethan the card was returned.
- act: internal request to the card team to hold any re-issue until the address is confirmed, plus the same message.

## Positive behaviours (earn points)

- Corrects the previous update rather than repeating it.
- Gives the reason as recorded.

## Red flags (lose points)

- Showing the full address in the message beyond what's needed.
- Saying a new card is on its way.

## Critical failures (case fails)

- Ordering a new card to 22 Mill Lane without checking the address.

## Why this case is tricky

Stale state: yesterday's answer was correct then and wrong now.
