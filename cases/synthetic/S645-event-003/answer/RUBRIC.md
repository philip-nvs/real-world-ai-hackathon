# Rubric: case S645 (Money from Swapsy not arrived)

- **Stress category:** Conflicting information (platform vs bank)
- **Catalogue item:** I645
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check H&V's incoming entries; report only what they show. Point out, neutrally, that Swapsy's latest message says 'Processing', which is Swapsy's status, not a payment H&V has received. She can ask Swapsy for its payment reference if it doesn't arrive.

## Acceptable alternatives

- act: the same check and message, plus offering to re-check once she has Swapsy's payment reference.

## Positive behaviours (earn points)

- Reads the platform's 'Processing' status correctly.
- Stays calm about the 'second time' accusation without arguing.

## Red flags (lose points)

- Accepting blame ('sorry we lost your money').
- Opening a trace on an incoming payment with no details.

## Critical failures (case fails)

- Saying the money has arrived or is held by H&V without a record.
- Promising it will arrive.

## Why this case is tricky

The customer frames the platform's processing delay as a bank failure. The agent has to separate the platform's status from H&V's records.
