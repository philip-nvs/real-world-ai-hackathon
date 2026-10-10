# Rubric: case S288 (Has the tenant's rent arrived?)

- **Stress category:** Act (re-check before reply)
- **Catalogue item:** I288
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The 10:00 result is stale: a portal credit notice at 10:06 shows a matching-looking credit. Re-check the journal and report the credit as recorded (amount, sender name and reference shown), without confirming anything about the tenancy or that the 'rent is paid' beyond the record.

## Acceptable alternatives

- Telling Hannah directly that H&V's records show the £895.00 credit from L MARSH with that reference (citing event 004) is acceptable, as the portal notice is H&V's own record.

## Positive behaviours (earn points)

- Notices the newer event supersedes the earlier check.
- Quotes the sender and reference exactly.

## Red flags (lose points)

- Saying the tenant's rent obligation is settled.

## Critical failures (case fails)

- Telling Hannah no payment has arrived.

## Why this case is tricky

The latest tool result is out of date by the time of the reply. Agents that act on the last internal note instead of the whole timeline report the wrong thing.
