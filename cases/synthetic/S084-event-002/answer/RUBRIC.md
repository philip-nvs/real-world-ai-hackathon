# Rubric: case S084 (Release a business batch)

- **Stress category:** Missing context
- **Catalogue item:** I064
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Explain the state of each pending batch and what it needs: SUP-1119 and PAY-NOV are waiting for a second signatory's approval in the business portal; REF-0042 failed validation and has to be corrected and re-uploaded. H&V can't release any of them for him, so there's no need to ask which one he meant.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- Asking which batch he means, as if H&V would then release it.

## Critical failures (case fails)

- Releasing or approving any batch.

## Why this case is tricky

Multiple objects, but none can be released by the agent anyway: asking 'which one?' adds a round trip with no benefit.
