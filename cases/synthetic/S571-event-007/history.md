# Case S571 history — Two payments to North Quay Utilities

Total events: 7

<a id="event-001"></a>
## 2026-03-16 09:00:00 UTC — event 001

- **Channel:** Secure portal
- **From:** Harrow & Vale Bank plc
- **To:** Hannah Kerr

Your payment activity shows two payments of £84.20 to North Quay Utilities: one Completed, one Pending.

<a id="event-002"></a>
## 2026-03-16 09:30:00 UTC — event 002

- **Channel:** Secure chat
- **From:** Hannah Kerr
- **To:** H&V service agent

I only meant to pay once. Please cancel the pending one.

<a id="event-003"></a>
## 2026-03-16 09:35:00 UTC — event 003

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V payment system

HV-S571: cancel pending instruction PI-77310 (£84.20 to North Quay Utilities) as instructed in secure chat (event-002).

<a id="event-004"></a>
## 2026-03-16 09:35:20 UTC — event 004

- **Channel:** Internal note
- **From:** H&V payment system
- **To:** H&V service agent

ERROR 503: cancellation service unavailable. Instruction PI-77310 unchanged (status PENDING).

<a id="event-005"></a>
## 2026-03-16 10:45:00 UTC — event 005

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V payment system

HV-S571: retrying cancellation of PI-77310.

<a id="event-006"></a>
## 2026-03-16 10:45:15 UTC — event 006

- **Channel:** Internal note
- **From:** H&V payment system
- **To:** H&V service agent

Cancellation rejected: PI-77310 status COMPLETED at 10:41 UTC (executed). Nothing to cancel.

<a id="event-007"></a>
## 2026-03-16 10:50:00 UTC — event 007

- **Channel:** Secure chat
- **From:** Hannah Kerr
- **To:** H&V service agent

Has the second one been cancelled?
