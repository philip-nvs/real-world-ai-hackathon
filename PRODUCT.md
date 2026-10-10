# Product

## Problem

- A bank's service team works open cases: a customer request, a history of events across channels (secure chat, email, calls, internal notes), and attachments.
- For each case, someone has to decide the single right next step from scattered and sometimes conflicting events.
- A wrong step is costly. Examples: promising a refund, acting on an email as if it were authorisation, telling a customer to pay again, or escalating without a handover.

## Assumption

- One next step per case (act, ask, wait or escalate) is what a case handler needs, not a full resolution plan.
- Unsafe moves can be caught by fixed rules, without a model judging them.
- The bank's real tools can sit behind the same four tool shapes without changing the agent: check a record, raise an internal request, submit an instruction, send a secure message.

## Solution

- Upload a case folder, run the agent on it, and read its answer. Re-run a case at any time; export each case's latest answer as a zip.
- For each case, the agent decides one of four next steps:
  - **act**: take the step now with the bank tools.
  - **ask**: ask the customer or a team for what's missing.
  - **wait**: hold until an expected event arrives.
  - **escalate**: hand over to a person.
- Each answer has three parts:
  - `ANSWER.md`: what was received, what was done, the decision, what was escalated, what failed, and the final result.
  - `REASONING.md`: the evidence (with event IDs), conflicts between events, options rejected, and policy-guard blocks.
  - A trace: every model turn, tool call, tool result, guard block and the final decision.
- A policy guard blocks each of the following and sends the agent back to re-plan:
  - promising a refund, a fraud finding, delivery or receipt by a recipient, or a guarantee
  - asking for passwords, PINs or one-time codes
  - advising a customer to pay again
  - re-sending or duplicating a payment
  - an account-changing instruction not backed by a customer event on a secure channel (an email is never authorisation)
  - escalating without a handover
- A case that crashes or times out still gets an **escalate** answer with a handover note.

## Reference

- [README.md](README.md)
