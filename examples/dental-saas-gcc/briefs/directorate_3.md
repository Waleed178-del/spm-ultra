## Directorate 3 Brief: Financial Feasibility & Economic Modeling (Agents 11-15)

**Directorate Verdict**
Financially this is a **conditional pass, and it depends on a second funding round**.
- CapEx is not the problem: ~33,000 USD [A11].
- The 250,000 USD seed (GIVEN) funds ~8.3 months of fixed burn with zero revenue [A12]. Even if the 300-clinic goal is hit exactly, cash at M12 is about zero [A15 adjusted to A12 burn].
- At 79 USD flat with reminders bundled in, contribution is only ~50 USD/clinic. Operating break-even sits at **~520 clinics**, so 300 clinics is still a ~-11,000 USD/month loss [A13].
- In the realistic base case (150 clinics at M12), cash runs out around **month 9-10 (Aug-Sep 2027)** [A15].
- Repricing to provider-based tiers with metered messaging [A14] brings break-even down to ~360-370 clinics. This is the most valuable financial lever available.
- Confidence: **Medium** on the direction, **Low** on NPV/IRR magnitudes, because terminal value drives them.

**Consolidated Findings**
1. **Launch CapEx ~33,000 USD** (range 22,000-48,000). Only ~7,000 USD is IAS 16 hardware. Engineering salaries are expensed. A KSA entity would add 15,000-30,000 USD and is deferred [A11].
2. **Fixed burn ~24,500 USD/month (M1-6) rising to ~27,500 USD/month (M7-12), averaging ~26,000 USD.** Payroll for the 3 GIVEN staff is ~17,000 USD/month of this [A12].
3. **Hidden variable cost: WhatsApp/SMS reminders of ~24 USD/clinic/month, about 30% of the price.** Total variable cost is ~28.50 USD/clinic, so contribution is ~50 USD/clinic (63%) [A12][A13].
4. **Hitting the goal does not mean profitability.** 300 clinics x 50 USD = 15,000 USD contribution, against ~26,000 USD fixed cost [A13].
5. **Sales velocity:** 300 clinics in 12 months needs 25 net adds per month. With an assumed 3% monthly churn and 20% demo close rate, that means **~125-170 demos per month for one founder**. This is not credible without a channel [A13].
6. **Monetization:**
   - Reject freemium and per-booking fees.
   - Adopt tiers keyed to number of dentists: Solo 59 / Clinic 99 / Clinic Plus 149 USD, each with a reminder allowance. Blended ARPA is ~94 USD (Low-Medium confidence).
   - Add a 150 USD onboarding fee and an annual prepay option at 10x the monthly price.
   - Price in AED/SAR. VAT makes KSA prices 12% higher at the counter than UAE prices [A14].
7. **Valuation (40% discount rate, 3x ARR terminal):**

| Case | NPV | IRR | Payback |
|---|---|---|---|
| Plan | +0.93M USD | ~113% | ~Y5.3 |
| Base | +0.25M USD | ~62% | none in 5 years |
| Downside | -0.31M USD | not meaningful | none |

   NPV excluding terminal value is negative in every case. External funding needed beyond the seed is **~170,000 USD (plan), ~560,000 USD (base), and over 900,000 USD (downside)** [A15].

**Key Numbers**

| Metric | Value | GIVEN/ASSUMED | Source agent |
|---|---|---|---|
| Seed capital | 250,000 USD | GIVEN | brief |
| Price | 79 USD/clinic/month (AED 290 / SAR 296) | GIVEN (FX conversion ASSUMED stable peg) | [A14] |
| Target ARR at 300 clinics | 284,400 USD | GIVEN arithmetic | [A13] |
| Launch CapEx | ~33,000 USD (22,000-48,000) | ASSUMED | [A11] |
| Fixed burn, average Y1 | ~26,000 USD/month | ASSUMED | [A12] |
| Variable cost per clinic | ~28.50 USD/month (reminders ~24) | ASSUMED | [A12][A13] |
| Contribution per clinic | ~50 USD/month (63%) | ASSUMED | [A13] |
| Break-even, 79 USD flat | ~520 clinics | ASSUMED | [A13] adjusted |
| Break-even, tiered plus metered messaging | ~360-370 clinics | ASSUMED | [A13][A14] |
| Runway with zero revenue | ~8.3 months (to ~Jul 2027) | ASSUMED | [A12] |
| Cash at M12, plan case | ~0-15,000 USD | ASSUMED | [A15][A12] |
| Cash-out month, base case (150 clinics) | ~M9-10 | ASSUMED | [A15] |
| Blended ARPA, tiered | ~94 USD | ASSUMED | [A14] |
| LTV (contribution, 3% churn) | ~1,670 USD | ASSUMED | [A13] |
| NPV plan / base / downside | +0.93M / +0.25M / -0.31M USD | ASSUMED | [A15] |
| Follow-on raise needed | 400,000-600,000 USD by M9-12 | ASSUMED | [A12][A15] |

**Internal Conflicts Resolved**
- **Fixed burn: 25,000 USD [A13][A15] vs ~26,000 USD [A12].** [A12] wins because it is the only bottom-up build and includes the month-7 support hire.
  - Break-even rises from 500 to ~520 clinics.
  - Plan-case cash at M12 falls from ~14,000 USD to roughly 0-2,000 USD.
- **ARPA: 79 USD (GIVEN) [A13][A15] vs 94 USD [A14].** The base model keeps 79 USD because it is GIVEN and 94 USD is untested. The 94 USD figure is an upside case worth ~+0.45M USD NPV [A15], pending willingness-to-pay interviews.
- **Fundraising timing: start by M6 [A12] vs close at M9-12 [A15].** These fit together: start the raise at M6 (~90,000 USD of cash left) and close by M9. Base-case cash-out at M9-10 leaves no slack for a later start.
- **Yield wording: "1.14x ARR/seed" [A13] vs "1.2x ARR per dollar burned" [A15].** These use different denominators. Keep [A15]'s ARR per dollar burned as the go/no-go metric.
- **Duplication removed:** messaging cost appeared in [A12] and [A13]. The single figure is ~24 USD/clinic/month.

**Cross-Dependencies for Other Directorates**
- CROSS-DEPENDENCY (D6 Go-to-Market): ~125-170 demos per month is beyond one founder. Needs a partner or reseller channel (dental suppliers) or an early sales hire. Positioning should lead with no-show cost recovery [A13][A14].
- CROSS-DEPENDENCY (D4 Risk & Compliance):
  - Whether KSA requires a local entity, VAT registration (15%) and ZATCA e-invoicing.
  - UAE/KSA PDPL rules for patient data and possible in-Kingdom hosting. Each could add 15,000-30,000 USD in CapEx [A11][A14].
- CROSS-DEPENDENCY (D5 Tech Architecture):
  - The reminder channel choice (WhatsApp vs SMS) and a metering capability decide whether contribution is ~50 or ~74 USD/clinic.
  - Architecture must stay cloud-only with no clinic hardware; supplying hardware would add ~300 USD per clinic [A11][A12].
- CROSS-DEPENDENCY (D2 Operations): headcount must stay at 3 plus one part-time support contractor until MRR covers new hires. Relocating one engineer to a lower-cost location adds ~2-3 months of runway [A12].
- CROSS-DEPENDENCY (D1 Strategy): proposed SMART milestones are at least 150 paying clinics, at least 1.0x ARR/burn and contribution of at least 50 USD/clinic by M12. Kill/pivot trigger: fewer than 40-60 clinics by M6 [A13][A15].
