### A15: NPV & ROI Calculator

**Key Findings** (bulleted, quantified)
- Method:
  - 5-year annual free cash flows, plus a terminal value at a multiple of Year-5 ARR.
  - Discount rate **40%** (ASSUMED seed-stage venture hurdle rate).
  - Contribution margin 63% at an ARPA of 79 USD (GIVEN price).
  - CapEx of 33,000 USD in Year 1.
  - Fixed costs ~25,000 USD/month in Year 1.
  - All inputs are ASSUMED unless noted.
- **Plan case (300 clinics at M12, GIVEN target, linear ramp):**
  - Clinics at year-end: Y2 700, Y3 1,200, Y4 1,700, Y5 2,100.
  - Fixed costs: Y2 450,000 USD, Y3 600,000 USD, Y4 750,000 USD, Y5 900,000 USD.
  - Free cash flow (thousand USD): Y1 **-236**, Y2 -151, Y3 -33, Y4 +116, Y5 +235.
  - Terminal value of 3x Y5 ARR (1.99M USD ARR) = 5.97M USD.
  - **NPV ≈ +0.93M USD; IRR ≈ 113%.** NPV excluding terminal value ≈ -0.18M USD.
  - Undiscounted payback: about **year 5.3**.
  - Confidence: Low, because the terminal value is about 120% of NPV.
- **Base case (150 clinics at M12, half the target pace, ASSUMED as realistic for a single-seller motion):**
  - Clinics at year-end: Y2 400, Y3 700, Y4 1,000, Y5 1,250.
  - Fixed costs: Y2 400,000 USD to Y5 700,000 USD.
  - Free cash flow (thousand USD): Y1 -284, Y2 -236, Y3 -172, Y4 -92, Y5 -28.
  - Terminal value 3x (1.19M USD ARR) = 3.56M USD.
  - **NPV ≈ +0.25M USD; IRR ≈ 62%.** No payback within 5 years.
  - Confidence: Low.
- **Downside case (75 clinics at M12, 3% monthly churn, 2x terminal multiple):**
  - Free cash flow (thousand USD): Y1 -309, Y2 -268, Y3 -236, Y4 -196, Y5 -172.
  - **NPV ≈ -0.31M USD.** IRR is not meaningful.
  - Confidence: Medium.
- Cash: in the plan case, Year 1 consumes ~236,000 of the 250,000 USD GIVEN, leaving **~14,000 USD at M12**. In the base case cash runs out at **~month 10 (Aug-Sep 2027)**. Cumulative external funding needed beyond the seed: plan ~170,000 USD, base ~560,000 USD, downside >900,000 USD. Confidence: Medium.
- Every scenario's value depends on the terminal multiple and on follow-on funding. **The 250,000 USD seed alone does not produce a self-funding business in any scenario.** Confidence: High.
- ROI on seed at M12 (ARR divided by capital deployed): plan 284,400 / 236,000 = **1.2x ARR per dollar burned**; base 142,200 / 250,000 = 0.57x. Capital efficiency above ~1.0x in year 1 is investable. Below 0.6x a follow-on round becomes hard to raise. Confidence: Medium.

**Critical Assumptions** (bulleted, GIVEN vs ASSUMED)
- GIVEN: 250,000 USD seed; 79 USD price; 300-clinic, 12-month target; start Nov 2026.
- ASSUMED: 40% discount rate. At 25% the plan-case NPV rises to ~+1.8M USD; at 60% it falls to ~+0.39M USD.
- ASSUMED: 3x ARR terminal multiple for a small Gulf vertical SaaS. Confirm through regional SaaS M&A comparables.
- ASSUMED: net-of-churn clinic counts; no price increase over 5 years; taxes ignored (UAE corporate tax of 9% only applies above the profit threshold, which is immaterial before profit).

**Recommendations** (numbered, actionable)
1. Treat the venture as **two-stage financing**. Budget for a ~400,000-600,000 USD follow-on round at month 9-12, gated on more than 150 clinics and more than 1.0x ARR/burn.
2. Use **NPV excluding terminal value** and **ARR per dollar burned** as the internal go/no-go metrics, not headline IRR.
3. Re-run this model at month 6 with actual net adds and churn. Kill or pivot if the trajectory tracks the downside case (fewer than 40 clinics by M6).
4. Any lever that raises ARPA or margin (repricing, metered messaging) is worth more than an equal percentage gain in volume, because volume needs founder time.

**Cross-Dependencies** (each line starts with a peer tag, e.g. [A12])
- [A11] Uses CapEx of 33,000 USD in Year 1. A KSA entity would add 15,000-30,000 USD.
- [A12] Uses fixed costs of 25,000 USD/month. Each +1,000 USD/month adds -12,000 USD to Year-1 free cash flow.
- [A13] Contribution margin 63%. Break-even sits at or above the 300 target, consistent with Y1 losses.
- [A14] An ARPA of 94 USD would lift plan-case NPV by roughly +0.45M USD.
- [A06] SMART milestone: 150 or more clinics and 1.0x ARR/burn by M12 to unlock the follow-on round.
- CROSS-DEPENDENCY (Strategy directorate): the plan only works as a venture-funded path; the founder must commit to raising again within 9 months.

**References** (frameworks applied and any external sources)
- Brealey, Myers & Allen, Principles of Corporate Finance: DCF, NPV, IRR, payback, terminal value.
- No external sources (WEB MODE OFF). The discount rate, multiples and ramp are ASSUMED.
