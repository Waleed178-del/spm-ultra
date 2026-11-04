### A13: Break-Even & Yield Analyst

**Key Findings** (bulleted, quantified)
- Unit contribution at 79 USD per clinic per month (GIVEN):
  - Payment processing ~3%: -2.40 USD (ASSUMED)
  - WhatsApp/SMS reminders: -20 to -30 USD, base -24 USD (ASSUMED: ~800 messages/month at ~0.03 USD)
  - Incremental hosting and storage: -2 USD (ASSUMED)
  - Support time at ~1 hour per clinic per month, valued at ~0 USD while founder and engineers absorb it (this hides the cost)
  - **Contribution of ~50 USD per clinic per month (~63% margin), ASSUMED.** Confidence: Medium.
- Operating break-even at a fixed cost of ~25,000 USD/month (ASSUMED lean 3-person Gulf team) = 25,000 / 50 = **~500 paying clinics**. Confidence: Medium.
- **At the 300-clinic goal (GIVEN), the business is still loss-making**: contribution 15,000 USD vs fixed ~25,000 USD gives **~-10,000 USD/month**. Hitting the goal ≠ being profitable. Confidence: High (the direction holds for any plausible cost base).
- Sensitivities (break-even clinic count):
  - Messaging billed as pass-through (contribution ~74 USD): **~340 clinics**
  - Blended ARPA 99 USD with messaging capped: **~360 clinics**
  - Fixed cost cut to 18,000 USD (offshore engineer): **~360 clinics**
  - All three combined: **~245 clinics**, i.e. break-even before the 300 goal
  - Monthly churn of 3% (ASSUMED, typical for SMB SaaS): at 300 clinics, about 9 clinics are lost per month. That needs ~34 gross adds per month to grow 25 net per month.
- Sales velocity implied by the goal: 300 clinics in 12 months = **25 net closes per month**, or roughly 1.2 per working day, by one founder across two countries. If close rate from demo is ~20% (ASSUMED), that is **~125-170 demos per month**. Confidence: High that this is beyond one person's capacity.
- Yield on seed: at 300 clinics, ARR of 284,400 USD (GIVEN arithmetic) gives ARR/seed = **1.14x**. At a realistic 150 clinics it is 0.57x. Confidence: Medium.

**Critical Assumptions** (bulleted, GIVEN vs ASSUMED)
- GIVEN: 79 USD per clinic per month; 300 clinics target; 250,000 USD seed; 3-person team.
- ASSUMED: average independent clinic has 1-3 dentists and ~300-500 appointments per month. Confirm via the UAE MOHAP/DHA/DoH and KSA MOH clinic registries plus 10 clinic interviews.
- ASSUMED: price excludes VAT; monthly billing; no setup fee.
- ASSUMED: fixed cost ~25,000 USD/month. My own estimate, built independently of the peer burn model.

**Recommendations** (numbered, actionable)
1. Redefine the 12-month financial target as **operating break-even at ~500 clinics, or ~300 clinics with repriced or metered messaging**. Keep 300 as the customer target, but reprice so that 300 = break-even.
2. Make reminder messaging a metered add-on or capped allowance. This one change moves break-even from ~500 to ~340 clinics.
3. Track contribution per clinic monthly. Alarm if it falls below 45 USD.
4. Track gross adds against churn separately. Report net clinic adds of at least 25 per month from month 4 as the plan threshold.

**Cross-Dependencies** (each line starts with a peer tag, e.g. [A12])
- [A11] I exclude CapEx from the break-even fixed base except ~200 USD/month depreciation.
- [A12] Need the confirmed fixed-burn figure. A burn above 25,000 USD pushes break-even above 500 clinics (~20 clinics per 1,000 USD of burn).
- [A14] Need the final price and packaging. Every +10 USD ARPA lowers break-even by ~80 clinics.
- [A29] Contribution of ~50 USD/month is the LTV input. With 3% churn, LTV is ~1,670 USD (contribution basis).
- [A06] Proposed SMART metric: "≥300 paying clinics AND contribution ≥50 USD/clinic AND net burn ≤10,000 USD/month by Oct 2027".
- [A16] Pre-mortem trigger: fewer than 60 paying clinics by month 6.
- CROSS-DEPENDENCY (Go-to-Market directorate): 125-170 demos per month for one founder is not credible. A sales or partner channel is needed.

**References** (frameworks applied and any external sources)
- Horngren et al., Cost Accounting: cost-volume-profit (CVP) analysis, contribution margin, break-even volume.
- No external sources (WEB MODE OFF). Messaging and churn rates are ASSUMED. Confirm via WhatsApp BSP pricing and SMB SaaS benchmark reports.
