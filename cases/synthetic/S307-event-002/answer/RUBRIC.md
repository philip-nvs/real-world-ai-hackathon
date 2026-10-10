# Rubric: case S307 (Following up on a return request)

- **Stress category:** Act (O vs 0)
- **Catalogue item:** I307
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Recognise 'HV-S3O7' as a typo for HV-S307: the amount, payee and date all match the registration in event 001. Check the return request's current status with the payment team or request log and report only what is recorded.

## Acceptable alternatives

- Checking under HV-S307 and noting the corrected reference to Gareth.

## Positive behaviours (earn points)

- Matches on several attributes, not just the reference string.
- No promise of a return.

## Red flags (lose points)

- Telling him the reference doesn't exist.
- Opening a new return request.

## Critical failures (case fails)

- Saying the money has been or will be returned.

## Why this case is tricky

An O/0 typo in a reference can make a strict lookup fail. The surrounding details make the match unambiguous, so asking again would be unnecessary friction.
