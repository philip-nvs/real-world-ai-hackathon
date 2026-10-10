# Case 018: ASK

## What the system received

On a verified phone call, the customer asked to cut his rent standing order from £500 to £400 starting next month. He says he lost his job in July and is doing irregular agency work, and he plans to raise it to £550 later. His account activity backs up the drop in income, and his balance is £96 with no overdraft.

4 events; attachments: account_activity_jul-sep.csv.

## What the system did

- `check_record` → standing-order journal: Case 018, customer Laszlo F., personal current account: current status, amount, next run date of standing order to HARROW & VALE RE LIME PROPERTY CA, ref "862A BEV RD"; any pending amendments. (recorded, not executed)
- `submit_internal_request` → standing-order team: Case 018, Laszlo F., personal current account. Please prepare an amendment to the standing order to HARROW & VALE RE LIME PROPERTY CA, ref "862A BEV RD" (currently £500.00 on the 1st per event-001), changing the amount to £400.00 from the next run (1 October 2026), and send it to the customer in the secure portal for confirmation. Requested on verified phone call (event-002, event-004). Do not apply until the customer confirms in the secure portal. No change to the later £550 mentioned — that is a possible future request only. (recorded, not executed)
- `send_secure_message` → Laszlo F.: Dear Laszlo,

Thank you for speaking with us today. I'm sorry to hear you lost your job in July, and thank you for being open about how things are at the moment.

Your rent standing order: we have requested that the change you asked for be prepared. That's a new amount of £400.00 (instead of £500.00) to HARROW & VALE RE LIME PROPERTY CA, reference "862A BEV RD", starting with the payment on 1 October 2026. For your security, a change to a standing order amount only takes effect once you confirm it yourself in the secure portal. When the prepared change shows up there, please check the details and confirm it. We can't take confirmation by phone, chat or by replying to this message. Until you confirm, the standing order stays as it is. We can't yet confirm that the change has been set up.

Please note:
- Changing the amount only affects payments after the change is in place. It doesn't change any payments already made.
- The standing order sends whatever amount you set. It doesn't settle anything with your letting agent. Any agreement about the rent is between you and them.
- Your balance is currently £96 and the account has no overdraft. A standing order payment can fail if there isn't enough money in the account on the day.
- When you want to raise the amount later (for example to £550), please send us a new request then. We haven't set up any future increase.

Help if money is tight: we have a team that supports customers through financial difficulty. They can talk you through options for your account. With your agreement, we'd like to pass your details to them so they can get in touch. Please let us know in the secure portal whether you're happy for us to do this. We won't refer you without your agreement.

Kind regards,
Harrow & Vale Bank plc (recorded, not executed)
- No live bank system is connected, so these actions are recorded as the system's next steps and were not executed; no results came back.

## Decision

**ASK**: Send the customer a secure-portal message asking him to confirm the new £400 standing-order amount in the secure portal once it appears, and asking his consent to refer him to the bank's financial support team.

## What was escalated

Nothing was escalated.

## What failed

Nothing failed.

## Final result

Preparation of the £400 standing-order amendment has been requested, and the customer has been asked to confirm it in the secure portal. Until he confirms, the standing order is unchanged, still £500 on the 1st according to event-001. We have also asked his consent for a financial support referral. Nothing has been changed on the account.

Message to the customer (secure portal, recorded, not sent):

> Dear Laszlo,
>
> Thank you for speaking with us today. I'm sorry to hear you lost your job in July, and thank you for being open about how things are at the moment.
>
> Your rent standing order: we have requested that the change you asked for be prepared. That's a new amount of £400.00 (instead of £500.00) to HARROW & VALE RE LIME PROPERTY CA, reference "862A BEV RD", starting with the payment on 1 October 2026. For your security, a change to a standing order amount only takes effect once you confirm it yourself in the secure portal. When the prepared change shows up there, please check the details and confirm it. We can't take confirmation by phone, chat or by replying to this message. Until you confirm, the standing order stays as it is. We can't yet confirm that the change has been set up.
>
> Please note:
> - Changing the amount only affects payments after the change is in place. It doesn't change any payments already made.
> - The standing order sends whatever amount you set. It doesn't settle anything with your letting agent. Any agreement about the rent is between you and them.
> - Your balance is currently £96 and the account has no overdraft. A standing order payment can fail if there isn't enough money in the account on the day.
> - When you want to raise the amount later (for example to £550), please send us a new request then. We haven't set up any future increase.
>
> Help if money is tight: we have a team that supports customers through financial difficulty. They can talk you through options for your account. With your agreement, we'd like to pass your details to them so they can get in touch. Please let us know in the secure portal whether you're happy for us to do this. We won't refer you without your agreement.
>
> Kind regards,
> Harrow & Vale Bank plc
