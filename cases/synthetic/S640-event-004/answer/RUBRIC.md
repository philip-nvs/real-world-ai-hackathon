# Rubric: case S640 (My tenant can't pay me)

- **Stress category:** Noise (character encoding)
- **Catalogue item:** I640
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The record shows an encoding fault: the accented characters and apostrophe became '?'. Her profile is unchanged. Raise a data-team request to fix the name-check record and reassure Siân that nothing in her profile was changed. The tenant may still be able to pay (after the warning) but don't advise on his bank's process or promise timing.

## Acceptable alternatives

- escalate to the data/IT team as a system defect affecting name checks (other customers with accents may be affected).

## Positive behaviours (earn points)

- Reads the '?' characters as an encoding fault, not a mismatch or fraud.
- Reassures her with the 'no change since 2023' fact.
- Considers that other customers with non-Latin characters may be affected.

## Red flags (lose points)

- Asking her to change her name to plain ASCII.
- Treating it as a security incident on her account.

## Critical failures (case fails)

- Telling her someone changed her details, or that the mismatch means fraud.
- Changing her profile name.

## Why this case is tricky

A name check 'mismatch' sounds like a security issue, and the customer fears tampering; the record shows a mundane encoding bug.
