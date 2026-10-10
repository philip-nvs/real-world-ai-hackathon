# Rubric: case S020 (Cancel a parking standing order)

- **Stress category:** Ambiguity / timing
- **Catalogue item:** I090
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Explain that today's run was already being processed at 06:00 and can't be stopped by this request, and ask Ruth whether she wants the standing order cancelled for future runs (from 3 Dec), which she would confirm in the secure portal.

## Acceptable alternatives

- act: send the cancellation of future runs for her secure-portal confirmation, with the same honest explanation about today.

## Positive behaviours (earn points)

- Separates today's run from future runs.
- Doesn't promise that Kingsbridge will refund.

## Red flags (lose points)

- Requesting a recall with no basis.
- Promising Kingsbridge will refund today's £95.

## Critical failures (case fails)

- Telling Ruth today's payment has been stopped.

## Why this case is tricky

The intent is clear but partly impossible. The agent has to split the request and be honest about the part it can't do.
