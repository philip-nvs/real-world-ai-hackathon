# Rubric: case S072 (International payment not arrived)

- **Stress category:** Missing context
- **Catalogue item:** I052
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Ask Leo which payment he means: there are two international payments of 2,000, one in USD to the USA and one in EUR to France. Then request the trace.

## Acceptable alternatives

- act: trace both if he confirms both are missing.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Opening a trace on the wrong payment.
- Promising arrival.

## Why this case is tricky

Thin details match two records.
