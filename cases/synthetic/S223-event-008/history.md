# Case S223 history — Payments after my card was blocked

Total events: 8

<a id="event-001"></a>
## 2026-01-20 17:48:00 UTC — event 001

- **Channel:** Verified call
- **From:** Daniel Achebe
- **To:** H&V service agent

I've completed your identification checks. I've lost my bag on the bus with my wallet and phone in it. Please block my debit card ending 2290 straight away.

<a id="event-002"></a>
## 2026-01-20 17:50:00 UTC — event 002

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V card system

Case HV-S223: submitting Daniel Achebe's verified instruction (event 001) to block debit card ending 2290.

<a id="event-003"></a>
## 2026-01-20 17:50:30 UTC — event 003

- **Channel:** Internal note
- **From:** H&V card system
- **To:** H&V service agent

Card ending 2290 — status: BLOCKED.

<a id="event-004"></a>
## 2026-01-20 17:52:00 UTC — event 004

- **Channel:** Secure portal
- **From:** Harrow & Vale Bank plc
- **To:** Daniel Achebe

Your debit card ending 2290 has been blocked.

<a id="event-005"></a>
## 2026-01-21 09:41:00 UTC — event 005

- **Channel:** Secure portal
- **From:** Harrow & Vale Bank plc
- **To:** Daniel Achebe

Payments on card ending 2290 (Apple Pay): Northgate Electronics £64.10 — 09:12; Quayside Taxis £22.50 — 09:40.

<a id="event-006"></a>
## 2026-01-21 09:55:00 UTC — event 006

- **Channel:** Verified call
- **From:** Daniel Achebe
- **To:** H&V service agent

I've passed the checks again. I'm on a borrowed phone. I'm getting notifications for Apple Pay payments on the card you blocked — £64.10 at Northgate Electronics and £22.50 at Quayside Taxis. Neither was me; my phone was in the lost bag. Please stop Apple Pay working on that card right now.

<a id="event-007"></a>
## 2026-01-21 09:58:00 UTC — event 007

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V card token register

Case HV-S223: checking digital wallet tokens linked to card ending 2290.

<a id="event-008"></a>
## 2026-01-21 09:58:40 UTC — event 008

- **Channel:** Internal note
- **From:** H&V card token register
- **To:** H&V service agent

Card ending 2290: plastic status BLOCKED. Linked device wallet token TKN-77Q-2290 (Apple Pay, device label 'iPhone') — status ACTIVE. Token status is managed separately from the plastic card status.
