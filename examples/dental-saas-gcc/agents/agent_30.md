### A30: Scale & Retention Strategist

**Key Findings** (bulleted, quantified)
- Churn sensitivity (ASSUMED). At 300 clinics (GIVEN), each 1 point of monthly churn loses ~3 clinics per month, which is about 2,850 USD of ARR per month. Moving churn from 4% to 2% per month turns a gross need of ~370 wins into ~335 to land 300 net. (Medium confidence)
- Churn drivers in small clinics (ASSUMED, from patterns in SMB vertical SaaS):
  - the receptionist leaves and the new one never adopts the product (estimated 30-40% of churn);
  - the clinic never connects its patient list or WhatsApp in the first 14 days (25-35%);
  - the clinic does not see a no-show improvement (15-25%);
  - card failures and payment lapses (10-15%), which is involuntary churn.
  (Medium confidence)
- Hook loop (Eyal):
  - **Trigger:** the morning WhatsApp summary to the receptionist and owner: "Today: 32 bookings, 29 confirmed, 3 at risk."
  - **Action:** one tap to resend or offer the slot to the waitlist.
  - **Variable reward:** a slot refilled from the waitlist.
  - **Investment:** the patient list, templates and history accumulate.
  Daily use by the receptionist is the leading retention indicator. Target: at least 20 of 22 working days per month active. (Medium confidence)
- Stickiness: once 500 or more patient records and their reminder history are in the system (ASSUMED to take about 4-8 weeks at 25-60 visits per day), switching cost rises sharply. Clinics that pass this threshold are ASSUMED to churn below 1.5% per month, against more than 4% for those that do not. (Low-Medium confidence)
- Referral potential (Reichheld): dental owners cluster in study clubs and WhatsApp groups. With an ASSUMED NPS target of 40 or more and 15-25% of promoters referring once a year, referrals give ~0.1-0.2 new clinics per active clinic per year, which is 15-35 clinics in year 1. (Low-Medium confidence)
- Monthly-only billing exposes the base to involuntary churn and impulse cancellation. Annual commitments are ASSUMED to churn at about a third of the monthly rate.

**Critical Assumptions** (bulleted, GIVEN vs ASSUMED)
- GIVEN: 79 USD per month; 300-clinic target; a team of 3 with no stated customer success staff.
- ASSUMED: the churn drivers and percentages above; NPS behaviour; and the 500-record stickiness threshold. These would be confirmed by cohort retention curves and exit interviews from the first 50 clinics.
- ASSUMED: the founder or engineers will do onboarding until a dedicated hire. At about 3 hours per clinic, that is about 1,000 hours for 330 clinics, or about 0.5 FTE.

**Recommendations** (numbered, actionable)
1. **14-day activation standard:** patient list imported, WhatsApp connected, and at least 50 reminders sent. Track the percentage of clinics activated within 14 days, with a target of at least 80%.
2. **Receptionist-proofing:** multi-user seats, a 10-minute Arabic/English video onboarding for new staff, and an alert to the owner if there is no login for 3 days.
3. **Monthly owner ROI report** sent over WhatsApp: "This month: 41 no-shows prevented, about 4,100 USD recovered (estimate)." This makes the value visible to the economic buyer.
4. **Dunning:** card-retry logic plus a bank-transfer option. Aim to keep involuntary churn under 0.5% per month.
5. **Referral:** one month free for both clinics, triggered automatically after the first ROI report showing 20 or more recovered appointments.
6. **Annual plan nudge** at day 60 for activated clinics.
7. Hire a part-time bilingual onboarding and customer-success person by about 100 clinics (ASSUMED month 6).

**Cross-Dependencies** (each line starts with a peer tag, e.g. [A12])
- [A23] Need: a measured time-to-first-reminder. Target: under 30 minutes from signup.
- [A26] Need: confirmation that the receptionist is the daily user and owns the habit.
- [A29] Provide: churn target of 2.5% per month blended (1.5% activated, 4% or more not activated); 15-35 referral clinics a year.
- [A07] Provide: OKRs for 14-day activation of at least 80%, NPS of 40 or more, and logo churn of 2.5% per month or less.
- CROSS-DEPENDENCY (D2 Operations): onboarding load is about 0.5 FTE. The current team of 3 does not include it.
- CROSS-DEPENDENCY (D5 Tech): the morning summary, waitlist refill, ROI report and dunning are retention-critical scope.

**References** (frameworks applied and any external sources)
- Eyal, Hooked (2014): trigger, action, variable reward, investment.
- Reichheld, "The One Number You Need to Grow", HBR (2003): NPS and referral mechanics.
- No external sources (web mode off). All figures are ASSUMED.
