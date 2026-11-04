### A29: CAC vs LTV Modeler

**Key Findings** (bulleted, quantified)
- ARPA: 79 USD per month (GIVEN). Gross margin is ASSUMED at 75-82%, because WhatsApp and SMS message fees (~5-10 USD per clinic per month, ASSUMED), hosting and support time eat into the margin. Gross-margin contribution is therefore ~60-65 USD per clinic per month.
- Churn: ASSUMED 2-3.5% per month logo churn, typical for SMB vertical SaaS sold monthly. Expected lifetime is 29-50 months.
- LTV (gross-margin basis) = 62 / churn:
  - 2.0% churn: 3,100 USD
  - 2.5% churn: 2,480 USD
  - 3.5% churn: 1,770 USD

  These are capped in practice by a 36-month horizon (about 2,230 USD). (Medium confidence)
- CAC by motion (ASSUMED, fully loaded):
  - Founder-led field: founder cost about 5,000 USD per month plus 800 USD travel and tools, divided by 8-15 closes per month, gives 390-725 USD.
  - Hired commissioned rep: 3,000 USD base plus 100 USD per close, divided by 8-12 closes per month, gives 350-475 USD.
  - Distributor partner at 25% revenue share: about 20 USD per month per clinic forever, equal to about 590 USD of lifetime value over 30 months, plus enablement.
  - Events: 400-700 USD. Paid digital: 400-900 USD.

  The blended CAC is ASSUMED at 450-750 USD. (Medium confidence)
- LTV:CAC = 2,480 / 600 ≈ 4.1x base case, with a range of 2.4x (worst) to 6.9x (best). This passes the Skok 3x test in the base case. (Medium confidence)
- **CAC payback is the binding constraint, not LTV:CAC.** Payback = CAC / 62 = 7-12 months. Skok's threshold for SMB is under 12 months. It passes, but narrowly. On cash, acquiring ~330 gross clinics at a 600 USD blended CAC costs ~198,000 USD, which is 79% of the 250,000 USD seed (GIVEN), before engineering salaries. (High confidence that this is a cash problem)
- Revenue realised in year 1 is small. A linear ramp to 300 clinics by month 12 accumulates an ASSUMED ~95,000-115,000 USD of cumulative revenue. This does not fund the acquisition spend in-year.
- Annual prepay at 10 months' price (790 USD) would pull ~5x the cash forward per clinic and make CAC payback effectively immediate on closing.

**Critical Assumptions** (bulleted, GIVEN vs ASSUMED)
- GIVEN: 79 USD per month; 250,000 USD; target of 300 clinics; founder sales.
- ASSUMED: gross margin of 75-82%; churn of 2-3.5% per month; founder loaded cost of 5,000 USD per month; the close rates and channel costs above. These would be confirmed by 90 days of cohort data and actual WhatsApp API invoices.
- ASSUMED: no free trial longer than 14 days; no onboarding cost beyond 2-3 hours per clinic.

**Recommendations** (numbered, actionable)
1. Track CAC payback per channel as the primary GTM metric. Gate spend at payback of no more than 12 months.
2. Offer annual prepay at 790 USD (2 months free) and target 30-40% annual mix. That alone generates an ASSUMED ~60,000-90,000 USD of extra year-1 cash at 300 clinics.
3. Distributor deals: prefer a one-off bounty (100-150 USD) over a perpetual 25% share. The perpetual share cuts LTV by about 25%.
4. Test 99 USD per month for new cohorts after month 4. At equal churn, LTV rises by 25% and payback falls to 6-10 months.
5. Pass message costs through, or cap them. Above 600 WhatsApp messages per month per clinic, charge for usage.
6. Budget a GTM cap of about 120,000 USD over 12 months. If blended CAC exceeds 900 USD by month 6, cut the target to about 200 clinics.

**Cross-Dependencies** (each line starts with a peer tag, e.g. [A12])
- [A13] Provide: 62 USD contribution per clinic per month; break-even on GTM at about 7-12 months per cohort.
- [A14] Need: a decision on annual prepay, the 99 USD tier and message pass-through.
- [A27] Need: actual closes per channel per month to replace the ASSUMED close rates.
- [A30] Need: measured monthly churn. Every 1 point of churn moves LTV by about 600-1,200 USD.
- [A07] Provide: OKRs for blended CAC of 750 USD or less, payback of 12 months or less, and annual mix of at least 30%.
- [A16] Provide: the pre-mortem trigger is CAC above 900 USD or churn above 4% per month by month 6.
- CROSS-DEPENDENCY (D3 Finance): GTM consumes about 50-80% of the seed at the 300 target. Engineering salaries cannot also be funded for 12 months without annual prepay or a bridge.

**References** (frameworks applied and any external sources)
- Skok, SaaS Metrics 2.0: LTV:CAC of at least 3x and CAC payback under 12 months.
- No external sources (web mode off). All figures are ASSUMED except those marked GIVEN.
