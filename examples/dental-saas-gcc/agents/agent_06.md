### A06: SMART Taxonomy Engine

**Key Findings**
- The headline goal "300 paying clinics within 12 months" (GIVEN) is Specific on count and Time-bound (Nov 2026 to Oct 2027, GIVEN start), but it fails three SMART tests as written: "paying" is undefined (trial, first invoice, or retained after 30 days?), there is no country split (UAE vs KSA), and there is no interim trajectory, so slippage cannot be detected before month 9. Confidence: High.
- Achievability check (Doran "A"): assuming MVP ready at month 3 (ASSUMED, basis: 2 engineers, greenfield build), the selling window is ~9 months, requiring ~33 net new clinics/month, or ~36-38 gross/month at 2% monthly logo churn (ASSUMED, typical SMB SaaS range 1.5-3%). For a single founder-seller at an ASSUMED 20% demo-to-paid conversion, that is ~180-190 demos/month, ~9 per working day. Ceiling for one in-person seller across two countries is ~3-4 demos/day (ASSUMED), i.e. 60-80 demos/month and 12-16 closes/month. Modelled 12-month outcome: 110-150 clinics. The 300 target is ~2x the realistic ceiling without added sales capacity or a self-serve channel. Confidence: Medium.
- Relevance: 300 clinics x 79 USD (GIVEN) = 23,700 USD MRR, but cumulative year-1 cash collected under a linear ramp from month 3 is only ~107,000 USD (ASSUMED ramp), against 250,000 USD capital (GIVEN). The count goal is relevant to fundraising signal, not to self-funding. Confidence: Medium.
- Measurability gap: no target for activation (clinics actually using the calendar daily) exists; a clinic paying but not booking is a churn risk that the headline metric hides.

**Critical Assumptions**
- GIVEN: 300 clinics, 12 months, 79 USD/clinic/month, 250,000 USD, 2 engineers + 1 founder-seller.
- ASSUMED: MVP live at end of month 3 (Feb 2027); 20% demo-to-paid; 2% monthly logo churn; 60/40 UAE/KSA split by clinic count (basis: UAE easier first entry, English-tolerant; KSA larger pool but Arabic-first and data-residency friction). Source that would confirm: UAE DHA/DoH and KSA MoH licensed-clinic registries.

**Recommendations**
1. Rewrite the North Star as: "By 31 Oct 2027, 300 clinics with an active paid subscription (invoice paid, at least 50 appointments booked in the trailing 30 days), split ~180 UAE / ~120 KSA."
2. Adopt a Base target of 150 paying clinics (Medium confidence achievable) and keep 300 as the Stretch target, explicitly conditional on adding a second seller or self-serve trial by month 5.
3. Set quarterly SMART gates: Q1 (Jan 2027) 10 pilot clinics live, free or discounted; Q2 (Apr 2027) 40 paid; Q3 (Jul 2027) 100 paid; Q4 (Oct 2027) 150 Base / 300 Stretch.
4. Define "paying" as first invoice settled and not refunded within 30 days; report gross adds, churned logos and net count monthly.
5. Add a funnel input target: 70 qualified demos/month from month 4, measured weekly.

**Cross-Dependencies**
- [A07] Needs my Base/Stretch split and quarterly gates to cascade Key Results; I need their KR weighting back to confirm activation metrics are cascaded.
- [A13] CROSS-DEPENDENCY: requires the break-even clinic count at the real burn; if break-even exceeds 150 clinics the Base target is not financially Relevant.
- [A15] Needs the 150 vs 300 scenario pair for NPV/ROI; I need their discount assumptions to rate "Relevant".
- [A29] CROSS-DEPENDENCY: the 20% demo-to-paid and churn assumptions must be validated against CAC/LTV.

**References**
- Doran, There's a S.M.A.R.T. Way to Write Management's Goals and Objectives, Management Review (1981).
- No external sources (web mode off); all market rates ASSUMED.
