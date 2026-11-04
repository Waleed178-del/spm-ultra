## Directorate 4 Brief: Risk, Compliance & Adversarial Stress-Testing (Agents 16-20)

**Directorate Verdict**
The plan as given is not survivable without changes. Two linked risks dominate: missing the 300-clinic goal (P ~80%) and running out of cash before break-even (P ~55%). Together they carry ~45% of total scored risk [A17]. Even if 300 clinics were reached, 23.7k USD MRR (GIVEN arithmetic) only roughly equals the ASSUMED ~24-25k USD/month burn, so year 1 ends at break-even at best [A16]. The plan becomes viable as a staged bet under five conditions: UAE-only first, a 150-clinic plan of record, a sales channel beyond the founder, data minimisation with in-country hosting, and hard trip-wires. Confidence: **High** on direction, **Medium** on the exact probabilities (WEB MODE OFF, all market figures ASSUMED).

**Consolidated Findings**
1. **Sales capacity is the binding constraint.** The GIVEN target needs ~33 paid adds a month across months 4-12, or ~165 demos a month at an ASSUMED 20% close rate. One founder can deliver 12-20 adds a month, so the realistic month-12 count is **110-180 clinics** [A16]. The founder is a 100% single point of failure on pipeline, and replacement takes 3-6 months [A19]. (High)
2. **Runway is shorter than the headline.** Burn of ~24k USD/month gives ~10.4 months [A20]. Adding A18's year-1 compliance cost (25-55k USD) and dual-region infra (0.5-1.5k USD/month) [A18] cuts runway to **~8-9 months**. (Medium-High)
3. **Appointment data should be treated as health data.** That brings UAE health-data localisation (Federal Law 2/2019) and KSA PDPL transfer restrictions, so launching both countries needs **two isolated in-country data planes**. The KSA PDPL penalty ceiling (up to SAR 5M per violation) exceeds the whole seed [A18]. (Medium. Requires local counsel.)
4. **Operational SPOFs:** two engineers with a bus factor of 1 per component, a single messaging channel (WhatsApp BSP), a single payment gateway (a KYC freeze stops 100% of collections), and a single acquisition channel [A19]. (Medium-High)
5. **Continuity requirements:** clinics lose front-desk operations within ~1-2h of an outage, which sets RTO 4h / RPO 15 min. DR must be multi-AZ in-country, not cross-border. The founder holds all root credentials, so break-glass escrow is needed by month 1 [A20]. (High)
6. **Medium-tier commercial risks:** churn above 4%/month (P 45%), price resistance at 79 USD for scheduling alone (P 35%), PMS incumbents bundling free scheduling (P 40%) [A17].

**Mandatory controls (deduplicated)**
- UAE-first launch. Gate KSA on 60 paying UAE clinics plus a KSA-region stack plus a KSA DPA [A16][A18].
- Make visit reason optional and coded, with no clinical free text, 24-month retention, consent logs and a 72h breach runbook [A18].
- Messaging and payment abstraction layers. WhatsApp primary, SMS fallback within 1h, a second gateway pre-qualified [A19][A20].
- Trip-wires. **Month 6:** fewer than 40 paid clinics or MRR under 3k USD triggers a burn cut of ~20% and a KSA freeze. **Month 9:** fewer than 90 clinics or churn above 5% triggers a pivot to B2B2B via PMS vendors or distributors, or a re-price to 129-149 USD. **Cash floor:** 72k USD (3 months of burn) triggers wind-down or acqui-hire talks [A20][A17].
- 10 paid design-partner pilots at the full 79 USD by month 2. Re-price if more than 50% refuse [A16][A17].

**Key Numbers**

| Metric | Value | GIVEN/ASSUMED | Source |
|---|---|---|---|
| Target clinics / horizon | 300 / 12 mo | GIVEN | brief |
| MRR at 300 clinics | 23.7k USD | GIVEN (arithmetic) | brief |
| Required paid adds, months 4-12 | ~33/mo | ASSUMED (3-mo build) | [A16] |
| Realistic month-12 clinics | 110-180 (plan 150) | ASSUMED | [A16] |
| Monthly burn | ~24k USD (range 22-27k) | ASSUMED | [A16][A17][A20] |
| Runway incl. compliance | ~8-9 mo | ASSUMED | [A18][A20] |
| Year-1 compliance cost | 25-55k USD | ASSUMED | [A18] |
| P(goal miss) / P(runway out) | 80% / 55% | ASSUMED | [A17] |
| Monthly logo churn | 3-5% | ASSUMED | [A16][A17] |
| RTO / RPO (booking DB) | 4h / 15 min | ASSUMED | [A20] |
| Founder replacement time | 3-6 mo | ASSUMED | [A19] |
| Month-6 / Month-9 trip-wire | <40 / <90 clinics | ASSUMED | [A20] |

**Internal Conflicts Resolved**
- **Burn figure:** [A16] gave 22-27k, [A17] 25k and [A20] 24k USD/month. **24k wins** as the midpoint, kept as a range. Runway is quoted net of [A18]'s compliance cost, because [A16], [A17] and [A20] all omitted it.
- **Re-baselined trajectory:** [A17]'s monitoring curve ends at 190, while [A16] recommends 150. **150 wins** as the plan of record, because it sits at the midpoint of the capacity-derived range. Keep [A17]'s monthly curve as the stretch track.
- **Fundraise timing:** [A20] said start by month 5-6, based on 10.4 months of runway. With compliance cost included, runway is ~8-9 months, so **the fundraise starts at month 3-4**.
- **DR vs. residency:** conventional cross-region DR conflicts with [A18]'s localisation finding. **Residency wins.** DR is in-country multi-AZ, and residual regional risk is accepted and documented [A20].
- **Second seller vs. burn cut:** [A19] wants extra sales capacity by month 4, while [A20] wants burn cut at month 6. Resolved with **commission-heavy or distributor channels**: variable cost only, no fixed salary.

**Cross-Dependencies for Other Directorates**
- CROSS-DEPENDENCY (D3 Finance, [A12][A13]): add 25-55k USD compliance cost and 0.5-1.5k USD/month dual-region infra. Confirm burn and break-even (~300-340 clinics).
- CROSS-DEPENDENCY (D5 Tech, [A21][A22]): MVP must ship consent capture, audit logs, coded visit reasons, in-country multi-AZ, and provider-agnostic messaging, payments and PMS adapters, plus CSV/ICS export.
- CROSS-DEPENDENCY (D6 GTM, [A29]): founder-only funnel caps adds at 12-20/month. Need a CAC figure (ASSUMED 600-900 USD founder-time) and a non-founder channel by month 4.
- CROSS-DEPENDENCY (D1 Strategy, [A01][A02]): UAE-first sequencing and the scheduling-vs-PMS-bundle threat (P 40%) need strategic confirmation.
- CROSS-DEPENDENCY (D2 Ops, [A09][A10][A25]): founder time split (at least 70% on sales), a clinic adoption success rate, and a vendor shortlist (BSP, SMS aggregators, gateways) with exit terms.
