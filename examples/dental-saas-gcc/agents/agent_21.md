### A21: MVP Scope Rationalizer

**Key Findings**
- The target needs a sellable product early. 300 paying clinics (GIVEN) in 12 months (GIVEN) means about 33 net new clinics a month if selling starts in month 3 (ASSUMED start). If the MVP slips to month 5, that rises to about 43 a month. Every month of build delay costs about 3-4 extra clinics a month on the rest of the sales curve. **High confidence.**
- Build capacity is 2 engineers (GIVEN). At about 18 productive dev-weeks per engineer per quarter (ASSUMED; allows for setup, meetings and early support), the team has about 36 engineer-weeks before month 3 and about 54 before month 4.5. My scope below costs about 30-34 engineer-weeks (ASSUMED estimate, ±30%). **Medium confidence.**
- The core value is fewer no-shows and less receptionist phone time, not "a calendar". The leanest proof is that a clinic sends automated WhatsApp reminders and patients confirm or cancel with one tap, which visibly lowers no-shows. ASSUMED baseline no-show rate at GCC dental clinics: 15-25%. To confirm, measure it in pilot clinics before launch. **Medium confidence.**
- **Must-have (MVP, about 30-34 eng-weeks, ASSUMED):** (1) chair- and dentist-based calendar with a reception day view, 8 wk; (2) minimal patient record (name, mobile, language preference, notes), 3 wk; (3) WhatsApp Business template reminders plus a confirm/cancel reply that writes back to the calendar, 6 wk; (4) a public booking link per clinic that works on mobile, 5 wk; (5) Arabic/English patient-facing messages and booking page with RTL support, 4 wk; (6) clinic sign-up, multi-user staff roles and subscription billing, 5 wk.
- **Cut from MVP (defer past month 6):** integration with practice-management systems (PMS) or EHRs, insurance and claims (including the Saudi NPHIES insurance platform), treatment charting, invoicing patients, native iOS/Android apps, analytics dashboards beyond the no-show rate, multi-branch features, marketing campaigns, and Hijri-calendar display. Together these are about 40-70 eng-weeks (ASSUMED), more than the team has in a year once support starts.
- Without PMS integration, the ideal customer narrows to clinics that schedule on paper, Excel, WhatsApp or a PMS with weak scheduling. If most independent clinics already schedule inside a PMS, they will not enter appointments twice and the reachable market shrinks. ASSUMED: 40-60% of independent clinics have no usable digital scheduler. A survey of 30-50 clinics would confirm this. **Low confidence.**

**Critical Assumptions**
- GIVEN: 2 engineers, 1 founder doing sales, 79 USD per clinic per month, 300-clinic goal, 250k USD seed.
- ASSUMED: the product is pre-MVP (the brief does not state the stage).
- ASSUMED: WhatsApp is the preferred patient channel in the UAE and KSA, above SMS and email. Basis: general GCC consumer messaging behaviour. A pilot clinic survey would confirm it.
- ASSUMED: each clinic has 1-4 chairs and about 20-30 appointments a day.
- ASSUMED: patient self-booking is wanted but secondary to reminders. Receptionists still book most visits by phone.

**Recommendations**
1. Freeze MVP scope at the six must-haves. Ship to 5-10 design-partner clinics by end of week 10 (mid-Jan 2027) and start paid conversion by end of month 3.
2. Set one MVP success gate before scaling sales: no-show rate falls by at least 30% relative to baseline across the pilot clinics within 6 weeks, and at least 70% of pilots convert to paid at 79 USD.
3. Launch in one country first: UAE, where English-led staff UIs and Stripe availability lower friction (ASSUMED). Open KSA once the Arabic staff UI is ready, around months 4-5.
4. Put a "PMS used" field in the sales CRM from day one. If more than 50% of lost deals cite double entry, reconsider PMS integration at month 6.
5. Keep one feature-request backlog with a strict rule: nothing enters a sprint unless 3 or more paying clinics asked for it.

**Cross-Dependencies**
- [A26] CROSS-DEPENDENCY: I need the share of independent clinics without a digital scheduler. It decides whether PMS integration can stay out of scope.
- [A08] Scope is 30-34 eng-weeks with a hard MVP date of week 10. The sprint plan must protect this.
- [A18] CROSS-DEPENDENCY: patient name + phone + appointment type may count as health data under UAE and KSA rules. Confirm before the minimal patient record ships.
- [A22] The MVP needs these integration points: WhatsApp Business API, a payment gateway, and SMS fallback (optional).
- [A23] The patient-facing flows that must be friction-audited are the reminder reply and the booking link.
- [A04] The scheduling-plus-WhatsApp wedge is narrow. Its differentiation depends on the Arabic-first patient experience.

**References**
- Ries, The Lean Startup (2011): MVP, validated learning, build-measure-learn loop.
- MoSCoW prioritisation.
- No external sources (web mode off). All market figures are ASSUMED.
