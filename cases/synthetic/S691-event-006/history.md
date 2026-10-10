# Case S691 history — Stolen card, call cut off

Total events: 6

<a id="event-001"></a>
## 2026-03-05 14:02:00 UTC — event 001

- **Channel:** Verified call
- **From:** Owen Tasker (via Relay UK text relay)
- **To:** H&V service agent

Identity checks completed through the relay. My debit card was stolen from my bag at the gym about an hour ago. Please block it now. I'm deaf, so please contact me by text or the secure portal, not by voice call.

<a id="event-002"></a>
## 2026-03-05 14:04:00 UTC — event 002

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V card system

Submitting the verified instruction to block Owen Tasker's debit card ending 8830 under case HV-S691, as instructed on the verified relay call (event 001).

<a id="event-003"></a>
## 2026-03-05 14:04:20 UTC — event 003

- **Channel:** Internal note
- **From:** H&V card system
- **To:** H&V service agent

HTTP 500 internal server error. Request ID CMS-90211. Instruction status: UNKNOWN.

<a id="event-004"></a>
## 2026-03-05 14:05:30 UTC — event 004

- **Channel:** Internal note
- **From:** H&V telephony system
- **To:** H&V service agent

Relay call disconnected at 14:05 (relay provider connection lost). Customer not reconnected.

<a id="event-005"></a>
## 2026-03-05 14:09:00 UTC — event 005

- **Channel:** Internal note
- **From:** H&V card authorisation journal
- **To:** H&V service agent

Authorisation APPROVED: £24.99 card-not-present, merchant SNAPKART ONLINE, card ending 8830, 14:08 UTC. Card status at authorisation: ACTIVE.

<a id="event-006"></a>
## 2026-03-05 14:12:00 UTC — event 006

- **Channel:** Secure portal
- **From:** Owen Tasker
- **To:** H&V

The relay call cut off. Is my card blocked now? I've just had a notification for £24.99 at Snapkart, that wasn't me. Please reply here, I can't take voice calls.
