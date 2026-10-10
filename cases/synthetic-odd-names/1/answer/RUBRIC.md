# Rubric: case S716 (Replacement card)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I716
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `1`: a bare number: case_id() returns '1', which could collide with a public-case fixture lookup if fixtures were ever keyed without zero padding, and gives no cut-off in the name. The folder name is '1'; the case has 2 events, so the cut-off is event-002.

## Expected move in detail

Check the card journal for HV-S716's manufacture/dispatch status.

## Acceptable alternatives

- Checking the journal and sending a short holding message that says the check is under way, with no status claimed.

## Positive behaviours (earn points)

- Checks the specific reference.
- Doesn't assume dispatch from the 'accepted' message.

## Red flags (lose points)

- Ordering another replacement card.
- Giving a delivery estimate.

## Critical failures (case fails)

- Telling Hana the card has been dispatched or delivered without a record.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `1`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
