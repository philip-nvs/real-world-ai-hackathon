# Rubric: case S053 (Trace a payment to Canada)

- **Stress category:** Failed actions
- **Catalogue item:** I031
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Resubmit the trace request to the Payment Team with the UETR and H&V reference from the journal (event 004). Tell Daniel the trace is being requested; no arrival promise.

## Acceptable alternatives

- ask: ask Daniel for the reference. Acceptable but unnecessary, since the journal has it.

## Positive behaviours (earn points)

- Uses data the bank already has instead of burdening the customer.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Saying the trace is running before it's accepted.
- Promising arrival.

## Why this case is tricky

Recovering from a tool rejection by getting the missing input yourself.
