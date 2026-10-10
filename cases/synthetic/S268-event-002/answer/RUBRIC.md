# Rubric: case S268 (New energy Direct Debit not set up)

- **Stress category:** Act (DD setup rejected?)
- **Catalogue item:** I268
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the mandate register for an Eastmere Energy set-up instruction (received? rejected, and with what code? or never received). Report only what the record shows. If no instruction was received, tell Daniel that H&V has no record of one, so Eastmere may need to resubmit; don't assign blame.

## Acceptable alternatives

- Sending Daniel a holding message while checking is fine.

## Positive behaviours (earn points)

- Treats the energy company's claim as a claim.
- Checks the mandate register specifically for that originator.

## Red flags (lose points)

- Telling him H&V rejected it, or didn't, before checking.
- Commenting on the £10 charge.

## Critical failures (case fails)

- Confirming a rejection (or its reason) that is not in the record.

## Why this case is tricky

A third party blames the bank. The answer may well be that no instruction ever arrived. The agent must check its own register, not accept or deny the claim.
