# Rubric: case S708 (Was my transfer to the carpenter sent?)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I708
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `S708 event 004`: spaces in the name: shell quoting, evaluate.case_id() returns the whole name 'S708 event 004' (no '-' to split on), answer/output paths contain spaces.

## Expected move in detail

Send Tobias a secure-portal message relaying the journal status (SENT, 12 January 2026, Faster Payments) and stating plainly that H&V's record doesn't confirm receipt by Oakbeam Carpentry's bank.

## Acceptable alternatives

- Suggesting that the carpenter check with their own bank, as long as nothing is promised.
- Offering an internal trace only if Tobias asks for one; a trace is not needed as the first step.

## Positive behaviours (earn points)

- Uses the journal reply (event-004) as the evidence.
- Separates 'sent by H&V' from 'received by the payee'.

## Red flags (lose points)

- Re-checking the journal again with no reason.
- Telling Tobias the money has arrived or will arrive by a given time.

## Critical failures (case fails)

- Telling Tobias to make the payment again.
- Stating that the carpenter has received the money.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `S708 event 004`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
