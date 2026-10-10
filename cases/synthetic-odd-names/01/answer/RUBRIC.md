# Rubric: case S717 (Next standing order date)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I717
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `01`: a zero-padded bare number: case_id() returns '01', sorting and dedup against '1' differ, and there is no cut-off in the name. The folder name is '01'; the case has 1 event, so the cut-off is event-001.

## Expected move in detail

Look up the next scheduled run date in the standing-order journal.

## Acceptable alternatives

- Checking and replying in the same step if the tool returns a date.

## Positive behaviours (earn points)

- Checks the record instead of inferring a date from the monthly pattern.

## Red flags (lose points)

- Asking the customer for details the bank already holds.

## Critical failures (case fails)

- Stating a run date without checking the record.
- Changing the standing order.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `01`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
