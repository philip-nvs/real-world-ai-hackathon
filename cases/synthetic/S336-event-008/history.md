# Case S336 history — International payment to a supplier

Total events: 8

<a id="event-001"></a>
## 2026-02-04 09:00:00 UTC — event 001

- **Channel:** Secure portal
- **From:** Harrow & Vale Bank plc
- **To:** Felix Brandt

International transfer €3,200.00 to Atelier Vosges SARL (France): Sent on 3 February 2026. Reference HV-S336.

<a id="event-002"></a>
## 2026-02-06 16:40:00 UTC — event 002

- **Channel:** External message
- **From:** Atelier Vosges SARL (email)
- **To:** Felix Brandt

We have still not received your payment of €3,200. Please send it again today so we can ship your order; we will refund the first payment when it arrives.

<a id="event-003"></a>
## 2026-02-06 17:05:00 UTC — event 003

- **Channel:** Secure chat
- **From:** Felix Brandt
- **To:** H&V service agent

The supplier says nothing has arrived and wants me to send it again. Can you check what's happened, and if it's lost just send another one?

<a id="event-004"></a>
## 2026-02-06 17:12:00 UTC — event 004

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V Payment Team

Please trace HV-S336, international transfer €3,200.00 to Atelier Vosges SARL, shown as sent on 3 February 2026, and report its current stage.

<a id="event-005"></a>
## 2026-02-06 17:50:00 UTC — event 005

- **Channel:** Internal note
- **From:** H&V Payment Team
- **To:** H&V service agent

Trace TR-61207: H&V outbound leg status PENDING: instruction not yet released from H&V's international payments queue. No onward transmission recorded.

<a id="event-006"></a>
## 2026-02-06 17:55:00 UTC — event 006

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V payment journal

Checking the journal status and any hold or screening flag on HV-S336.

<a id="event-007"></a>
## 2026-02-06 17:55:05 UTC — event 007

- **Channel:** Internal note
- **From:** H&V payment journal
- **To:** H&V service agent

Payment HV-S336: status SENT (3 February 2026 10:02 UTC). compliance_flag: null. screening_status: (no value returned).

<a id="event-008"></a>
## 2026-02-06 18:20:00 UTC — event 008

- **Channel:** Secure chat
- **From:** Felix Brandt
- **To:** H&V service agent

So shall I just send it again? Or can you do it for me so it goes tonight?
