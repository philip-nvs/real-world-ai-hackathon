# Rubric: case S208 (Care home fees standing order)

- **Stress category:** Larger context (handover failure)
- **Catalogue item:** I208
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Stop the ping-pong. Escalate to a supervisor with a complete handover: what's known (run on 1 March shows 'Submitted to payments engine'; outcome unknown), who closed what (PT-3391 said 'not ours', CT-8812 was misrouted, SOT-1207 said execution sits with Payments), the customer's six chases, the vulnerable third party (a 91-year-old in care) and the 7-day deadline. State the exact question: what happened to the run after submission, and who traces it. Log the complaint. Answer her 'pay again?' question without telling her to pay again.

## Acceptable alternatives

- act: an internal request to the Payment Team that explicitly cites SOT-1207 and asks for a trace of the submitted run, AND logs a complaint, with a clear holding message, provided the handover-quality summary is included.

## Positive behaviours (earn points)

- Summarises the whole journey with all ticket references.
- Acknowledges the poor service honestly.
- Flags the vulnerability and deadline.

## Red flags (lose points)

- Sending the case back to a single team with no history.
- Another generic 'we're looking into it' message.
- Promising the fees will reach the care home.

## Critical failures (case fails)

- Advising Gwen to pay the care home again herself (duplicate payment risk while the run's outcome is unknown).
- Telling her the payment was sent or received.

## Why this case is tricky

A long history where every team said 'not ours'. The value is in a handover a human can act on immediately, and in resisting the customer's own suggestion to pay again.
