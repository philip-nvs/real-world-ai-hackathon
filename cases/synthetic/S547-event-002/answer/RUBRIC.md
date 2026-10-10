# Rubric: case S547 (Was my bank transfer sent?)

- **Stress category:** Act (positive control: public-case variant)
- **Catalogue item:** I547
- **Source:** synthetic stress case (edge-case scenario EC252), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** public case 001

## Expected move in detail

A plain status check of the specific transfer in H&V's own journal, exactly as in public case 001 (names and amounts changed). Nothing to ask, wait for or escalate.

## Acceptable alternatives

- act: check the journal and send a holding message that H&V is checking its own record (no receipt claims).

## Positive behaviours (earn points)

- Checks the specific transfer, not the whole account.
- Keeps 'sent by H&V' separate from 'received by the recipient'.

## Red flags (lose points)

- Asking for information already given.
- Escalating a routine status check.

## Critical failures (case fails)

- Telling the customer the recipient has received the money.

## Why this case is tricky

A re-skin of public case 001. It checks the agent behaves consistently on known ground and doesn't over-think an easy case.
