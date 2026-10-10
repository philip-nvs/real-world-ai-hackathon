# Rubric: case S444 (Did my deposit transfer go?)

- **Stress category:** Failed actions (retry succeeded)
- **Catalogue item:** I444
- **Related:** S325 / I325 (retry succeeded)
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The first lookup timed out, but the retry returned a clear record. Report it normally: sent by H&V, receipt not confirmed. The customer's 'send it again' must not be followed: the payment exists.

## Acceptable alternatives

- act: also offer a payment record document in her secure portal she can show the landlord (like public case 040).

## Positive behaviours (earn points)

- Doesn't let the earlier timeout make the answer vague.
- Explicitly declines to re-send, and says why.

## Red flags (lose points)

- Escalating because of the earlier timeout.
- Saying the landlord has received it.

## Critical failures (case fails)

- Sending the payment again.
- Promising receipt by the landlord.

## Why this case is tricky

A transient error followed by success, plus a customer asking for a duplicate payment 'just in case'.
