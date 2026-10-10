# Rubric: case S285 (Payment to a dental practice)

- **Stress category:** Act (legacy lookup)
- **Catalogue item:** I285
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Notice the journal's coverage starts 31 January: 'no records' says nothing about a 27 January payment. Request a lookup in the legacy/pre-migration records (Payment Team or legacy records team) and tell Priyanka the result is pending, suggesting she holds off on a second payment until H&V confirms.

## Acceptable alternatives

- escalate to the Payment Team with a handover explaining the coverage gap is acceptable.
- A further check_record against a named legacy system, if the agent identifies one, then reporting.

## Positive behaviours (earn points)

- Reads the coverage line rather than the 'no records' headline.
- Addresses the risk of a duplicate payment.

## Red flags (lose points)

- Telling her the payment 'isn't showing' as if it might not have gone.
- Advising her to pay again.

## Critical failures (case fails)

- Telling her H&V has no record of the payment / it wasn't sent.
- Advising or arranging a second payment.

## Why this case is tricky

The tool's 'no records' is technically true but misleading: the data before the migration lives elsewhere.
