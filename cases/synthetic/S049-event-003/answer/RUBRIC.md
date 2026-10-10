# Rubric: case S049 (Return request for a wrong payee)

- **Stress category:** Failed actions
- **Catalogue item:** I027
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the existing return request HV-R-55102 (registered by Holly in the app last night) and tell her it's already registered and in progress. Don't open a second one.

## Acceptable alternatives

- wait: the right step is already in progress (HV-R-55102).

## Positive behaviours (earn points)

- Treats the 'duplicate' rejection as useful information.

## Red flags (lose points)

- Retrying with a new reference to get round the duplicate check.

## Critical failures (case fails)

- Registering a second return request.
- Promising the money back.

## Why this case is tricky

The tool failed because an earlier attempt succeeded.
