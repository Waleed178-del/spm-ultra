### A16: Project Pre-Mortem Lead

Premise (Klein premortem): it is November 2027. The company has failed: well short of 300 paying clinics, close to out of cash, and the founder is looking for a bridge round that nobody will lead. The causes below are worked back from that outcome and ranked by how much each contributed.

**Key Findings**
- **Cause 1: the sales funnel never had the capacity (contribution ~35%, High confidence).** 300 paid clinics in 12 months (GIVEN) means 25 net adds a month. Assume build plus pilots eats months 1-3 (ASSUMED, pre-product), so the real need is ~33 a month across months 4-12. At an ASSUMED 20% demo-to-paid close rate for SMB vertical SaaS sold founder-led, that is ~165 demos a month, or ~8 every working day. One founder who also runs fundraising, support escalations and admin realistically does 15-25 demos a week (ASSUMED), which gives 12-20 paid clinics a month. Projected month-12 count: **110-180 clinics**, not 300.
- **Cause 2: cash ran out before revenue caught up (contribution ~25%, High).** ASSUMED burn is ~22-27k USD a month: 2 engineers at 7-9k USD fully loaded each, founder at 3-4k, plus 3-5k for infra, SMS/WhatsApp, travel and licensing. That consumes the 250k (GIVEN) in **9-11 months**. Even 300 clinics gives only 23.7k MRR (GIVEN arithmetic), which is still at or below burn. Cumulative year-1 revenue on the 110-180 path is ~45-75k USD (ASSUMED ramp).
- **Cause 3: two countries split the effort (contribution ~15%, Medium).** KSA needs Arabic-first UX, separate payment rails, a separate data-residency posture and in-person selling in Riyadh/Jeddah. Running both markets from day 1 roughly halves the founder's selling density in each.
- **Cause 4: the product stayed a feature, not a workflow (contribution ~15%, Medium).** Independent clinics already book through phone, WhatsApp and the scheduler built into their PMS. Without a PMS sync or measurable no-show reduction, the clinic sees 79 USD/month (GIVEN) as optional. Assumed logo churn is **3-5%/month**, which erodes 30-45% of acquired clinics over a year.
- **Cause 5: a compliance or messaging block stopped onboarding (contribution ~10%, Low-Medium).** Sender-ID approval, a health-data residency question from a clinic, or a WhatsApp template rejection stalled go-live for weeks.

**Critical Assumptions**
- GIVEN: 300 clinics, 12 months, 250k USD, 2 engineers plus 1 founder-seller, 79 USD/clinic/month.
- ASSUMED: pre-product at start; 20% demo-to-paid close; burn 22-27k USD/month; churn 3-5%/month; 3-month build before first paid clinic. Confirm with founder payroll data and 10 discovery calls.
- ASSUMED: no existing dental network. If the founder has 50+ warm clinic relationships, Cause 1 drops to ~20%.

**Recommendations**
1. Re-baseline the 12-month target to **150 paid clinics** as the plan of record, and treat 300 as the stretch.
2. Launch one country first (UAE, Dubai plus Sharjah, ASSUMED denser and English-tolerant) and gate KSA entry on 60 paying UAE clinics.
3. Before month 2, sign 10 design-partner clinics on paid pilots of 1-3 months, to prove willingness to pay at 79 USD.
4. Make the no-show reduction metric (target -25%, ASSUMED) the core product promise and measure it per clinic from week 1.
5. Add a second selling motion by month 4 (dental distributors, supply reps, or commission-only reps) so the founder is not the only funnel.

**Cross-Dependencies**
- [A01] Needs the SWOT weakness list to confirm whether Cause 4 (feature, not workflow) is the dominant weakness.
- [A13] CROSS-DEPENDENCY: break-even sits at ~300-340 clinics against an ASSUMED 25k burn. A13 must confirm, because the GIVEN target only reaches break-even, never profit, inside year 1.
- [A29] Needs the CAC and payback figures. The pre-mortem assumes founder-time CAC of ~600-900 USD per clinic (ASSUMED).
- [A19] Cause 1 is a single-person dependency. A19 owns quantifying it.
- [A17] Hand-off: Causes 1-5 with contribution weights, to be tiered.

**References**
- Klein, G., "Performing a Project Premortem", HBR (2007).
- WEB MODE OFF: no external sources. Close rates and churn are ASSUMED. Confirm against OpenView/KeyBanc SaaS benchmarks and GCC dental-clinic interviews.
