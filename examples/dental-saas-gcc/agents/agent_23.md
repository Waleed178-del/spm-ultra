### A23: UX/User Journey Flow Auditor

**Key Findings**
- **There are three journeys, and each has its own friction budget.** (1) Clinic onboarding: owner or receptionist, once per clinic. (2) Daily reception use: the receptionist, 20-30 bookings a day (ASSUMED). (3) The patient's reminder reply and self-booking: on mobile, often older patients, mostly in Arabic. Journey 3 decides whether no-shows actually fall. **High confidence.**
- **Onboarding is a hidden cost for the founder.** If every clinic needs a 2-hour assisted setup (ASSUMED baseline for founder-led SaaS), 300 clinics (GIVEN) take about 600 founder-hours. That is about 15 full working weeks taken from selling. Self-serve setup under 30 minutes, with optional 15-minute remote help, brings this to about 75-150 hours. **High confidence.**
- **The import step decides activation.** Clinics that start with an empty calendar fail to activate. ASSUMED: 30-40% of trial clinics stall if they must re-key their existing patient list. A CSV or Excel import with phone-number normalisation (+971 and +966 formats, local "05x" numbers) addresses the biggest single onboarding blocker.
- **Daily-use target.** Booking an existing patient should take at most 3 clicks and under 15 seconds. That is the parity bar against paper and WhatsApp, which receptionists use today (ASSUMED). If booking is slower than the paper diary, staff will keep the paper diary and the product churns.
- **Patient reply flow.** WhatsApp quick-reply buttons ("Confirm" / "Reschedule" / "Cancel") need no app, login or link. ASSUMED response rate: 50-70% for button templates versus 20-35% for "reply YES" text. Rescheduling should open a booking link with at most 2 screens.
- **Language and RTL.** Patient messages and the booking page must be Arabic-first with an English toggle, chosen per patient, not per clinic. The staff UI needs both languages. KSA reception staff are predominantly Arabic-speaking (ASSUMED). UAE reception staff are mixed, often English-preferring (ASSUMED). Retrofitting RTL later typically costs 3-5x more than building it into components from the start (ASSUMED industry heuristic). **Medium confidence.**
- **Accessibility.** WCAG 2.2 AA for the booking page: touch targets at least 24×24 CSS px (SC 2.5.8), contrast at least 4.5:1, no CAPTCHA-only verification (SC 3.3.8 accessible authentication; use a WhatsApp OTP instead). These matter for older patients on low-end Android devices.
- **Nielsen heuristics risks.** "Visibility of system status": staff must see whether each reminder was sent, delivered, read or replied. Without it they phone patients anyway and the value disappears. "Error prevention": block double-booking a chair and warn on bookings outside opening hours.

**Critical Assumptions**
- GIVEN: the founder is the only salesperson. No support or onboarding staff are stated.
- ASSUMED: about 25 appointments a day per clinic; 1-3 front-desk users per clinic.
- ASSUMED: the patient base is mixed Arabic and English speakers, with Arabic dominant in KSA.
- ASSUMED: a large share of patients book on mobile. Clinic booking logs would confirm it.

**Recommendations**
1. Target metrics: time-to-first-reminder-sent under 24 h from sign-up; self-serve setup under 30 min median; at least 60% of trial clinics activated (10 or more appointments with reminders) within 7 days.
2. Ship a CSV/Excel patient import with phone normalisation in the MVP. It is the biggest single activation lever.
3. Build all UI components RTL-aware from sprint 1. Ship the Arabic patient flow at launch and the Arabic staff UI before the KSA launch.
4. Show reminder status per appointment in the day view (sent, delivered, read, confirmed, cancelled), colour-coded with a text label as well so colour is not the only cue (WCAG 1.4.1).
5. Run 5-user moderated usability tests with real receptionists at week 6 and week 10 (Nielsen's 5-user rule). Fix all severity-3+ issues before paid launch.

**Cross-Dependencies**
- [A21] My onboarding requirements add CSV import and reminder-status visibility, about 2-3 eng-weeks, to the MVP scope.
- [A26] CROSS-DEPENDENCY: I need the persona split (owner-dentist versus receptionist as daily user) and each one's language preference by country.
- [A30] CROSS-DEPENDENCY: the 7-day activation rate is the leading indicator of retention. Clinics not activated by day 14 are churn candidates.
- [A10] CROSS-DEPENDENCY: moving receptionists from a paper diary to the product is a behaviour change and needs a short in-clinic training script.

**References**
- Nielsen, 10 Usability Heuristics (1994); Nielsen 5-user testing rule.
- W3C WCAG 2.2 (SC 1.4.1, 1.4.3, 2.5.8, 3.3.8).
- No external sources (web mode off).
