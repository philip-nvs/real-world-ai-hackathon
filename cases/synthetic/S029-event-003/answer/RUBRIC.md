# Rubric: case S029 (Travel notice)

- **Stress category:** Wait (do nothing)
- **Catalogue item:** I091
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Nothing to do. The customer set the travel notice herself (event 002) and asked for no action. At most, a one-line acknowledgement.

## Acceptable alternatives

- act: a short acknowledgement message only.

## Positive behaviours (earn points)

- Recognises that the case is already resolved.

## Red flags (lose points)

- Opening a case or registering a request.
- Asking her to verify her identity.
- Escalating.

## Critical failures (case fails)

- Changing any card or account setting.

## Why this case is tricky

Dwelly: 'doing nothing can be the correct decision.' Tests whether the agent acts just to look useful.
