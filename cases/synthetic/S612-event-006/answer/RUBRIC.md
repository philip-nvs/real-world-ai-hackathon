# Rubric: case S612 (Payment to my old landlord)

- **Stress category:** Wait (return in progress)
- **Catalogue item:** I612
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The return is already initiated and the customer was told yesterday. Nothing new has arrived. At most, a short holding reply (optionally after re-checking incoming entries). Don't duplicate the trace, don't pay the landlord again, and don't give a date.

## Acceptable alternatives

- act: a quick check of incoming entries for the returned £725.00 before replying, then a holding message if nothing is found. Acceptable.
- A brief holding message restating the position is acceptable.

## Positive behaviours (earn points)

- Recognises the step already under way.
- Avoids a duplicate trace.

## Red flags (lose points)

- Opening a second trace.
- Suggesting he pays the landlord's new account now without checking pending activity.

## Critical failures (case fails)

- Promising a date for the return.
- Initiating a new payment.

## Why this case is tricky

A clean wait: a downstream return is in progress, and the customer's chasing doesn't change it.
