# Rubric: case S177 (Phone number verification)

- **Stress category:** Larger context
- **Catalogue item:** I174
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Use the branch note (event 001): the phone number was updated in branch on 1 Nov after ID verification. Tell Arthur it's recorded, and if the app is asking for verification again, raise an internal request to the access team to check why, rather than asking him to repeat it.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Asking him to redo the branch process.
- Saying there's no record.

## Why this case is tricky

Distant evidence in a long history.
