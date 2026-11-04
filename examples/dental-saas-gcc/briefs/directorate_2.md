## Directorate 2 Brief: Operational Roadmap & Target Mapping (Agents 6-10)

**Directorate Verdict**
The 300-clinic goal (GIVEN) cannot be reached with the GIVEN team of three. The binding constraint is the founder, not engineering. Reaching 300 needs about 185 demos a month. That would put the founder at about 520 h/month against a sustainable 200 h [A09], and the realistic outcome for one seller is 110-150 clinics [A06]. Engineering can ship a pilot MVP by Jan 2027 and open paid sales in Feb 2027 [A08], so the product itself is achievable. The plan becomes operationally credible if it is reset to a committed Base of 150 paying clinics, keeps 300 as a Stretch, and adds 1-2 GCC hires from months 5-6. Even the Base plan goes over founder capacity from month 7 [A09]. Confidence: Medium.

**Consolidated Findings**
1. **The goal needs redefining.** "Paying" is undefined, there is no split between the UAE and KSA, and there are no interim gates [A06]. Adopted definition: invoice paid and not refunded within 30 days, plus at least 50 appointments booked in the trailing 30 days. Target split is about 60/40 UAE/KSA (ASSUMED) [A06][A07]. Confidence: High.
2. **Funnel maths.** With MVP live at month 3 there are about 9 selling months. That means about 33 net adds a month, or 36-38 gross at 2% monthly churn. At 20% demo-to-paid this is about 185 demos a month. One person can do 60-80 [A06][A09]. Confidence: Medium.
3. **OKR structure.** There is one owner per function: the founder covers Sales/CS, Engineer 1 the core product, and Engineer 2 the platform, localisation and reminders. Each owner carries at most 3 KRs per quarter, and every count KR is paired with a retention or activation KR [A07]. Confidence: High.
4. **WBS and critical path.** The MVP is about 720 h, or 6-7 two-week sprints at about 120 focused h/sprint. The critical path runs Foundations → Scheduling core → WhatsApp/SMS reminders → pilot. Two external blockers must start in Sprint 1 (Nov 2026): WhatsApp Business API approval (1-4 weeks, ASSUMED) and the KSA hosting/data-residency decision [A08]. PMS integration (150-300 h each) stays out of the MVP unless 30% or more of lost deals cite it [A08]. Confidence: Medium.
5. **Resource and burn.** Baseline burn is about 24,000 USD/month, which gives about 10.4 months of runway on 250,000 USD before revenue. A bilingual onboarding/support specialist (2,500-3,500 USD/month) by month 5 and an Arabic-speaking seller based in Riyadh (4,000-6,000 USD/month) by month 6 would cost 40,000-57,000 USD over 6 months and cut pre-revenue runway to about 8 months [A09]. Confidence: Medium.
6. **Adoption.** The daily user is the receptionist, not the owner who signs. Moving forward bookings and running double-entry are the main reasons clinics would leave. The fix is a 14-day parallel run, a bilingual training kit, a front-desk champion in each clinic, and a day-14 adoption threshold of 80% or more of bookings made in the product [A10]. Training load is 600-1,200 h a year at 150-300 clinics [A10]. Confidence: Medium.

**Key Numbers**

| Metric | Value | GIVEN/ASSUMED | Source agent |
|---|---|---|---|
| Target clinics, 12 months | 300 (Stretch) | GIVEN | [A06] |
| Committed Base target | 150 clinics | ASSUMED (capacity model) | [A06][A09] |
| MRR at 300 / 150 clinics | 23,700 / 11,850 USD | GIVEN arithmetic | [A07] |
| Year-1 cash collected, 300-clinic linear ramp | ~107,000 USD | ASSUMED | [A06] |
| Monthly logo churn | 2% | ASSUMED | [A06][A07] |
| Demo-to-paid conversion | 20% (≈67% demo→trial × 30% trial→paid) | ASSUMED | [A06][A07] |
| Demos/month needed at 300 | ~185 | ASSUMED | [A06][A09] |
| Founder demo ceiling | 60-80/month | ASSUMED | [A06][A09] |
| Founder load at 300 / 150 clinics | ~520 / ~250 h/month vs 200 sustainable | ASSUMED | [A09] |
| Engineering capacity | ~120 h/sprint; ~3,100 h/year | ASSUMED | [A08] |
| MVP effort | ~720 h (6-7 sprints) | ASSUMED ±30% | [A08] |
| Pilot / paid launch | Jan 2027 / Feb 2027 | ASSUMED | [A08][A07] |
| Baseline burn / runway | ~24,000 USD/month / ~10.4 months | ASSUMED | [A09] |
| Hires, months 5-12 | 40,000-57,000 USD | ASSUMED | [A09] |
| Onboarding time per clinic | 3 h + 1 h follow-up at launch, 1 h by month 6 | ASSUMED | [A09][A10] |
| Quarterly gates (committed / stretch) | Q1 10 pilots; Q2 40/50; Q3 100/140; Q4 150/300 | ASSUMED | [A06][A07] |

**Internal Conflicts Resolved**
1. **Quarterly gates.** [A06] set Q2 40, Q3 100, Q4 150, while [A07] set Q2 50, Q3 140, Q4 300. **Resolution:** [A06]'s gates become committed OKRs and [A07]'s become aspirational ones, graded at 0.7. The reason is that [A09]'s capacity model independently caps output near 150.
2. **Conversion rates.** [A06] used 20% demo-to-paid and [A07] used 30% trial-to-paid. These describe different funnel stages, so they are reconciled into one chain (about 67% × 30% ≈ 20%) rather than one replacing the other.
3. **Onboarding hours.** [A09] modelled 3 h per clinic, while [A10] modelled 3 h + 1 h now and 1 h by month 6. **Resolution:** [A10]'s figure wins, because [A10] holds the training mandate. [A09]'s founder-load figures for months 1-6 are therefore slightly understated, which strengthens the case for hiring.
4. **Engineering support allocation.** [A08] proposed a fixed 25% reserve, while [A09] proposed 40% from month 7. **Resolution:** keep 25% if the support specialist is hired by month 5, otherwise 40%. This makes the hire a dependency of the roadmap.
5. **MVP date.** [A07]'s Q1 KR ("in production by 31 Jan") and [A08]'s 6-7 sprints conflicted. **Resolution:** a pilot build with WBS items 1.0-4.0 and 6.0 (about 560 h) goes to 10 pilot clinics in Jan 2027, and the paid launch with the booking widget and CSV import follows in Feb 2027.

**Cross-Dependencies for Other Directorates**
- **CROSS-DEPENDENCY (D3 Finance, [A12][A13][A15]):** reconcile the burn of about 24,000 USD/month and runway of about 10.4 months. Test break-even clinic count under the 150 and 300 scenarios. If break-even is above 150, the Base target does not cover costs.
- **CROSS-DEPENDENCY (D6 GTM, [A29][A30]):** validate the 20% demo-to-paid rate, 2% churn and a CAC ceiling of about 950 USD (12 months of revenue). The Stretch target only holds if a self-serve or referral channel delivers 25% or more of new clinics by Q3.
- **CROSS-DEPENDENCY (D4 Risk & Compliance, [A17][A19]):** the founder is a single point of failure for 100% of revenue. Rate receptionist non-adoption as High probability / High impact. Decide whether appointment data counts as health data under KSA PDPL and UAE rules, because that sets hosting location and could force re-platforming of WBS 1.0.
- **CROSS-DEPENDENCY (D5 Tech, [A21][A22][A23]):** ratify the MVP boundary (no PMS or EMR integration; CSV import and bilingual RTL stay in). Confirm WhatsApp API and KSA hosting are on the critical path. Receptionist booking must take under 30 seconds.
