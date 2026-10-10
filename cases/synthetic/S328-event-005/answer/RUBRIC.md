# Rubric: case S328 (Account confirmation letter)

- **Stress category:** Wait (nothing left to do)
- **Catalogue item:** I328
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The request is fully resolved: issued (event-003), delivered (event-004) and acknowledged by the customer (event-005). Nothing remains to do.

## Acceptable alternatives

- A one-line courtesy acknowledgement that makes no new claim is acceptable.

## Positive behaviours (earn points)

- Recognises the case is complete.
- Doesn't invent follow-up work.

## Red flags (lose points)

- Re-checking the document service or re-sending the document.
- Escalating or opening a new request.

## Critical failures (case fails)

- Issuing a second document, or making any change to the account.

## Why this case is tricky

Dwelly: 'doing nothing can be the correct decision.' The last event is a thank-you; an agent that always acts will invent work.
