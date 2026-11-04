# Reconciliations

Seven live conflicts from `audit.json`. Each was reconciled by an isolated subagent that read only the raw files of the agents in conflict. The texts below are verbatim. The final section is the orchestrator's harmonisation. Reconcilers ran in parallel and used slightly different inputs for shared figures, so that section fixes the single figure set used in the blueprint.

---

#### Reconciliation: Operational Roadmap vs OpEx Runway

**Conflict** A09 and A20 assume ~24k USD/month burn and 10.4 months of runway, and A09 adds two hires from M5–M6. A12 models 24.5–27.5k with no hires and 8.3 months of runway. The fundraise start varies from M4 to M6. Neither burn figure includes the 25–55k USD year-1 compliance cost.

**Reconciled Position**
- **Burn (ASSUMED):** A12's cost lines, minus one engineer moved remote/offshore (−4k, per A09/A12), plus compliance at 2.5k/month (30k/year, low-mid of the range).
  - M1–4: **23.0k/month**
  - M5–6: **26.0k/month** (support specialist)
  - M7–12: **27.6k/month**, or **32.6k/month** if the seller is hired
  - **Agreed planning average: ~28k USD/month.**
- **Runway:** 250k GIVEN − 33k CapEx = 217k. That is **~8.2 months with zero revenue**, or **~8.5 months** with Base-case gross margin (~40 clinics at M6, ~70 at M8). Cash runs out around **mid-July 2027 (M9)**. A20's hard floor of 3 months' burn (~85k) is hit around **M6 (Apr 2027)**.
- **Hiring schedule:**
  - M1–4: 3 FTE only (GIVEN).
  - **M5 (Mar 2027):** full-time bilingual onboarding/support specialist (~3k). Replaces A12's part-time M7 contractor, because the founder is at 125% capacity even in the 150-clinic Base.
  - **M7 (May 2027):** Riyadh seller (~5k, commission-heavy), only if ≥40 paid clinics at M6 **and** a term sheet or bridge is committed. Otherwise KSA stays pilot.
- **Fundraise:** with 4–6 months of lead time and ~8.5 months of runway, **start M4 (Feb 2027)**, right after the MVP and the Q1 pilot gate. **Target close M8 (Jun 2027).** Raise ~500k (A15 Base gap ~560k). A 250k angel/strategic bridge is the minimum, with a decision by M6.
- **Targets:** 150 clinics stays the Base plan and 300 is the Stretch, valid only if the seller is hired at M7.

**Adjustments Required**
- **A06:** Keep the 150 Base and the quarterly gates. Make 300 explicitly conditional on the M7 seller plus funds raised.
- **A09:** Keep the support hire at M5. Move the seller from M6 to M7, gated on both conditions. Assume one engineer remote/offshore. Runway becomes 8.5 months, not 10.4.
- **A12:** Replace the flat 25k ceiling with the phased 23 / 26 / 27.6 / 32.6k series. Add 2.5k/month compliance. Start the fundraise at M4, not M6.
- **A15:** Set Y1 fixed cost to ~28k/month, not 25k (about −36k Y1 FCF by A15's own sensitivity). Close at M8, not M9–12. Replace the 150-clinic close gate with ≥40 paid at M6 and ≥0.6x ARR/burn.
- **A20:** Runway is ~8.5 months. Its notes say "by M5–6 at the latest", but its own lead-time logic now requires M4. The hard-floor trip-wire moves to around M6. The M6 and M9 pivot checks stay.

**Residual Risk**
- An offshore engineer may not be possible if both engineers are already Gulf-based hires. Average burn would then be ~32k and runway ~7 months.
- Compliance could reach 55k (−1 month of runway).
- A raise closed at M8 rests on only ~40–70 clinics of traction, so round size and valuation will be weak.
- WhatsApp cost (~36% of price) could squeeze margin and shorten runway further.
- If the bridge is not committed by M6, the seller and the 300 Stretch are both off.

---

#### Reconciliation: Scale parameters vs CapEx estimate

**Conflict** A24 plans one in-country cell each for the UAE and KSA (2 cells, 400-800 USD/month at 300 clinics). A11's ~33,000 USD CapEx base case assumes a single UAE entity serving KSA cross-border with no second region. It excludes the 15,000-30,000 USD KSA entity and in-Kingdom hosting cost.

**Reconciled Position**
- **Agreed CapEx: 35,000 USD (ASSUMED; range 24,000-50,000).** A11's 33,000 USD base plus ~2,000 USD (ASSUMED) one-off KSA cell setup: region provisioning, IaC duplication, and a residency check in the pen-test scope. This equals A11's own 35,000 USD cap and is ~14% of the 250,000 USD GIVEN seed.
- **Build the KSA cell from launch.** Its run-cost is OpEx and already sits inside A24's 2-cell 400-800 USD/month, which is small. A24 prices a later retrofit of hard-coded single-cell assumptions at 3-6 eng-weeks, which is material for 2 engineers (GIVEN). Building it now also removes in-Kingdom hosting from A11's open cost list.
- **Defer the KSA entity** (MISA licence + CR, 15,000-30,000 USD ASSUMED), triggered by whichever comes first:
  - (a) written legal/tax advice that KSA PDPL/MISA/ZATCA-VAT rules require a local entity for cross-border B2B SaaS to Saudi clinics, obtained by month 2 (Jan 2027);
  - (b) KSA reaches 50 paying clinics (A11's threshold);
  - (c) a KSA clinic chain or regulator requires local contracting to buy.
- **Ring-fence a 25,000 USD entity contingency.** It is not CapEx and is not counted in the 217,000 USD runway until released. If the trigger fires, CapEx becomes ~50,000-65,000 USD.

**Adjustments Required**
- **A11:** Restate the base case as 35,000 USD with a KSA cell setup line. Replace "single UAE entity, no second region" with "UAE entity + KSA hosting cell; KSA entity deferred to trigger". Change the [A24] dependency from open to resolved.
- **A24:** No change to infra figures. State that the KSA cell is live at launch, and put cell routing and tenant-to-country pinning in the MVP, not later.
- **A12 (downstream):** Use 35,000 USD in months 1-2. Keep the 25,000 USD entity contingency outside runway until released. Effective runway cash is ~190,000 USD if held.
- **Risk & Compliance directorate (downstream):** Own trigger (a). Deliver a mandatory/not-mandatory ruling on the KSA entity and in-Kingdom processing by month 2.

**Residual Risk**
- All prices are ASSUMED and not verified against MISA, free-zone or hyperscaler fee schedules (WEB MODE OFF).
- If the legal opinion makes the entity mandatory before the first KSA sale, KSA revenue slips 2-4 months during formation. That pressures the 300-clinic GIVEN goal.
- KSA PDPL may also require in-Kingdom processing by WhatsApp/SMS providers. The cell does not fix that; it would surface as messaging COGS, not CapEx.
- Availability of a suitable in-Kingdom region from the chosen cloud provider is unverified.

---

#### Reconciliation: Tech stack vendor choices vs OpEx burn

**Conflict** A12 costs messaging at ~24 USD/clinic/month (400 appts × 2 msgs × 0.03 USD) and total variable cost at ~28.50 USD. A25 costs messaging at 9-18 USD (600 appts × 1 msg × 0.015-0.03 USD). A12's fixed burn also omits the second cell and year-1 compliance.

**Reconciled Position**
- **Appointment volume: 600 per clinic per month.** A22's load baseline is 25 appts/day × ~24 working days, and A25 uses the same figure. A12's 400 has no stated basis. ASSUMED.
- **Messages per appointment: 1 outbound utility-template reminder at 24 h.** Patient Confirm/Cancel replies are inbound within the service window and ASSUMED free. Booking confirmations show on the booking page or go by email, not WhatsApp.
- **Rate: 0.025 USD/message loaded**, the midpoint of A25's BSP range.
- **Agreed messaging COGS: 600 × 1 × 0.025 = 15.00 USD WhatsApp + ~1.50 USD SMS fallback (capped at 10%, A25) = 16.50 USD/clinic/month.**
- **Total variable cost: 21.00 USD/clinic/month:** messaging 16.50 + payments 2.50 + hosting across 2 cells 2.00.
- **Contribution: 79 − 21 = 58 USD/clinic/month (~73%).** Worst case is ~53 USD (0.03 rate, top of fee ranges).
- **Fixed burn, corrected:** 26,000 + ~450 (second cell, A22) + ~3,300 (compliance at 40k/yr, midpoint of 25-55k from the conflict record, not from these files) = **~29,750 USD/month**.
  - Break-even ≈ **513 clinics** (≈589 with A12's 28.50 variable cost).
  - At the 300-clinic goal, contribution is 17,400 USD: **not break-even at goal**.
  - Zero-revenue runway falls from ~8.3 to ~**7.3 months**.

**Levers that hold 21 USD:**
1. Include 600 outbound messages per clinic per month. A second nudge to non-responders counts against that cap. Overage is a ~0.04 USD/message pass-through.
2. Lock reminder templates to the utility category so Meta does not reclassify them as marketing.
3. Hard-cap SMS fallback at 10% of sends.
4. Offer annual prepay by bank transfer at a 10-15% discount to cut payment fees.
5. Sell a 2 h second reminder only as a paid add-on. Two reminders by default would raise COGS to ~31.50 and cut contribution to ~47.50.

**Adjustments Required**
- **A12:** Variable cost becomes 21.00 USD (messaging 16.50). Add ~450 USD/month second cell and ~3,300 USD/month compliance, for fixed burn of ~29,750. Restate runway at ~7.3 months. Move the fundraising start to month 5 (Apr 2027).
- **A22:** The load baseline of 15,000 outbound/day assumes 2 per appointment. Revise to ~7,500 WhatsApp + ~750 SMS per day at 300 clinics. Enforce the per-clinic cap and utility-only templates in the `MessageChannel` layer.
- **A25:** Narrow the tooling-table WhatsApp line to ~4,500 USD/month at 300 clinics. Confirm that BSP rate cards treat inbound replies as free and that the platform fee is under 500 USD/month.

**Residual Risk**
- All rates are ASSUMED (WEB MODE OFF). Meta reprices on its own schedule, and every ±0.01 USD/message moves contribution by ~6 USD.
- Appointment volume could be 400-800, which swings messaging cost from ~11 to ~22 USD.
- Clinics may reject the cap or demand two reminders.
- The compliance cost and the need for two cells depend on [A18]'s ruling on health data.
- At ~513 clinics, break-even lies outside the 12-month horizon. It needs follow-on funding or a price/mix change (premium tier).

---

#### Reconciliation: CAC/LTV assumptions vs break-even volume

**Conflict** A29 reports healthy unit economics (LTV:CAC ~4x). A13 puts operating break-even at ~500 clinics, above the 300 GIVEN target, while A16 cites ~300-340. They give opposite go/no-go signals because each uses different contribution and churn inputs.

**Reconciled Position** (all ASSUMED unless GIVEN)
- **Messaging COGS: ~15 USD/clinic/month.** This is the midpoint of the disputed 9-24 range (~500 msgs × 0.03).
- **Support: ~4 USD**, now counted (A13 noted it was hidden).
- **Contribution at 79 USD flat:** 79 − 2.4 (payment) − 15 (messaging) − 2 (hosting) − 4 (support) = **~55 USD/clinic/month**.
- **Churn:** **3%/month** (median of A13 3%, A29 2-3.5%, A16 3-5%).
- **LTV:** 55 / 0.03 = **~1,830 USD** (~1,220 if capped at 36 months).
- **CAC:** blended **~650 USD**, between A29 (450-750) and A16's founder-time figure (600-900).
- **LTV:CAC: ~2.8x**, which fails the 3x test. Payback is ~12 months, at the limit.
- **Break-even at 79 USD flat:** 25.5k fixed burn / 55 = **~465 clinics** (435-490 for 24-27k burn).

**Repriced scenario:** 99 USD core, a capped messaging allowance, metered overage.
- Contribution = 99 − 3 − 5 − 2 − 4 = **~85 USD**.
- LTV is **~2,830 USD** at 3% churn (2,430 at 3.5%).
- LTV:CAC is **~4.4x** (3.7x at 3.5% churn), with payback in ~7.6 months.
- **Break-even = 25.5k / 85 ≈ 300 clinics** (280-320).

**Go/no-go reading**
- **79 USD flat: NO-GO** as a financial plan. Unit economics are below 3x, and break-even is ~3x the realistic 150-clinic base case.
- **Repriced: conditional GO.** Unit economics pass and break-even matches the 300 GIVEN target. Volume is still the binding risk. At the 150 base case, contribution is ~12.8k against 25.5k burn, about −12.7k/month. Break-even is a month 18-24 event and needs annual prepay or a bridge round.
- The opposite signals are resolved: healthy per-unit economics are necessary but not sufficient, and both now use the same contribution figure.

**Adjustments Required**
- **A29:** Contribution 62 → 55, churn 2.5% → 3%, LTV 2,480 → ~1,830, LTV:CAC 4.1x → 2.8x, payback restated as ~12 months. Make 99 USD with metered messaging the base case, not a later test.
- **A13:** Messaging COGS 24 → 15, contribution 50 → 55. Break-even ~500 → ~465 at 79 flat, and ~300 repriced. Keep the SMART metric with an 80 USD contribution floor under repricing.
- **A16:** Correct the break-even citation. 300-340 holds only with messaging pass-through or repricing; at 79 flat it is ~465. Keep 150 clinics as plan of record, and add a trigger: contribution < 75 USD by month 6.

**Residual Risk**
- Per-clinic messaging volume is unverified. Each 5 USD of messaging cost shifts break-even at 79 USD by ~40 clinics.
- Churn at 99 USD is untested, and price elasticity in GCC independent clinics is unknown.
- CAC has no cohort data. Above 900 USD, LTV:CAC falls below 3x even when repriced.
- Burn uncertainty (24-27k/month) means ±20 clinics on break-even under repricing.
- Even repriced, year 1 does not reach profitability unless sales capacity grows beyond the founder (A16 Cause 1).

---

#### Reconciliation: Compliance requirements vs MVP scope

**Conflict** A18 treats appointment data as health data and needs consent, audit, minimisation, retention and residency controls in the MVP. A21's six must-haves (31 eng-weeks point estimate, 30-34 range) contain none of these, and capacity for a week-10 pilot is already short: ~28 eng-weeks by week 10 at 18 per engineer per quarter.

**Reconciled Position**
Health-data handling is a launch requirement, not a backlog item. A KSA PDPL penalty of up to SAR 5M exceeds the 250k USD GIVEN seed.

Compliance items added to the MVP (all ASSUMED estimates, ±30%):
1. Patient consent capture plus a WhatsApp reminder opt-in/opt-out log: 1.5 wk
2. Append-only audit log of staff reads and edits on patient records, with export: 2 wk
3. Coded optional visit reason (check-up / treatment / consult), with the free-text notes field removed: 0.5 wk
4. Retention with a 24-month default and an auto-purge job: 1 wk
5. UAE-region hosting from day one, structured so a second data plane can be added: 0.5 wk
6. 72h breach runbook and record of processing activities: 0.5 wk for alerting and access-log tooling. The founder and counsel write the documents.

**Added: 6 eng-weeks.**

Cut or deferred to pay for it:
- **Public booking link (5 wk)** moves to weeks 13-15. A21 itself says self-booking is secondary to reminders.
- **Self-serve subscription billing** shrinks from 5 wk to 2 wk (sign-up and roles only) for the pilot. Billing (~3 wk) is built in weeks 12-13, before paid conversion at the end of month 3. Pilots are free design partners and don't need it.
- **Dropping free-text notes** saves 0.5 wk on the patient record.
- **The KSA data plane (3-6 wk)** stays out of the MVP. No KSA clinic is onboarded until it exists, in months 4-5, which matches A21's KSA timing.

Pilot MVP = 8 + 2.5 + 6 + 4 + 3 + 6 = **29.5 eng-weeks**, which capacity reaches in week 11. **Pilot date: end of week 11, ≈ 18 Jan 2027** (build start Mon 2 Nov 2026). That is one week later than A21's week 10. Paid conversion stays at the end of month 3.

**Adjustments Required**
- **A21:** Swap the booking link for the compliance block and split billing out of pilot scope. Pilot moves to week 11. Remove the "notes" field. The KSA launch depends on the KSA region being live.
- **A18:** Accept a UAE-only MVP. KSA residency, the KSA-law DPA and ISO 27001 readiness gate the KSA launch, not the pilot. Register WhatsApp templates and SMS sender IDs in month 1.
- **A08 (via A21):** Re-baseline the sprint plan to 29.5 eng-weeks and a week-11 pilot. Weeks 12-15 go to billing, then the booking link.
- **D3 Finance:** Keep the 25-55k USD compliance cost and 0.5-1.5k USD/month dual-region infra from month 4.

**Residual Risk**
- Estimates are ±30%. A 20% overrun pushes the pilot to week 13-14.
- The KSA plane (3-6 wk) competes with the post-MVP backlog in months 4-5, so the KSA launch, and the sales curve built on it, could slip.
- The legal readings are unverified (WEB MODE OFF). If UAE emirate rules (DoH/DHA) require more, such as licensing or ADHICS certification, scope or launch timing could grow.
- Moving the booking link to weeks 13-15 weakens the patient-facing demo at pilot.

---

#### Reconciliation: 12-month clinic volume base case

**Conflict** A06, A09 and A16 set the plan of record at 150 net paying clinics. A27 calls 180-230 the base case, but that is only true if the commissioned rep and the distributor partner are counted as base.

**Reconciled Position**
- **Committed Base: 150 net paying clinics by 31 Oct 2027** (MRR 11,850 USD), all UAE-first. Assumed in base:
  - founder field + WhatsApp outbound (90-140 gross, A27);
  - a referral mechanic from month 4 (20-40 gross);
  - an AEEDC Feb 2027 co-exhibit at the low end (~15 closes);
  - a bilingual onboarding/support specialist hired by month 5, Mar 2027 (A09). Base needs this hire because founder load passes 125% from month 7.
  - ~165-185 gross wins less 2.5-3% monthly churn ≈ 150 net, inside A16's 110-180 founder-led range.
- **Stretch: 230 net clinics** (MRR 18,170 USD). On top of base, it assumes an Arabic-speaking commissioned rep from month 6, Apr 2027 (+35-55 gross), one UAE distributor partner from month 5 (+30-80 gross; A27 marks this as unvalidated), and KSA entry through the rep.
- **300 (GIVEN)** stays the stated goal but is not planned. It needs the top of every channel range at once (A27).
- **Why the rep and distributor are stretch:** both are contingent and unproven. A09 gates the rep on Q2 results, and A27 itself marks distributor uptake as unvalidated. Fundraising and runway should be sized on base, not on gated hires.

**Quarterly gates** (net paid clinics; "paid" = first invoice settled and not refunded within 30 days, per A06)

| Quarter end | Base | Stretch | Decision |
|---|---|---|---|
| Q1 (Jan 2027) | 10-15 paid pilots | 15-20 | Specialist hire confirmed |
| Q2 (Apr 2027) | 40 | 50 | If ≥40: hire rep, open KSA. If distributor <3 closes in 60 days: drop it |
| Q3 (Jul 2027) | 100 | 130 | KSA scale-up only if ≥60 UAE clinics |
| Q4 (Oct 2027) | 150 | 230 | |

**Adjustments Required**
- **A06:** Change Stretch from 300 to 230 and label 300 "goal, unplanned". Re-split the North Star: ~150 UAE for base; ~170 UAE + 60 KSA for stretch.
- **A09:** Keep the specialist in base. Move the rep cost (~4,000-6,000 USD/month) into the stretch budget, released only when the Q2 gate passes.
- **A16:** Keep 150. Name the distributor and rep as the stretch "second motion" from Recommendation 5.
- **A27:** Relabel 180-230 as stretch. Restate channel yields as net of churn. Put distributor and rep payouts in a gated budget line, not base GTM spend.

**Residual Risk**
- At A16's 3-5% churn, the high end pulls net base toward ~120.
- AEEDC timing (Feb 2027) is tight when the product only goes live in month 3, and may yield nothing.
- Agents assume very different demo-to-close rates: 20% (A06/A16) vs 30-40% (A27). The first 60 days of pipeline data decide which holds.
- Base MRR of ~11,850 USD stays well below burn of ≥24,000 USD/month. The fundraise (~Q3) must be sized on base.

---

#### Reconciliation: KSA entry gate and timing

**Conflict** The agents give four incompatible KSA triggers: A01 at 50-75 paying clinics; A18 a KSA stack + KSA DPA (A16 adds 60 clinics); A26 at 100+ UAE clinics in M6-12; and A22's KSA cell timing. At the modelled pace, a cell deployed at M4-5 would arrive far ahead of any clinic-count gate. Source check: A18's raw file has no clinic number, and A22's raw file has no M4-5 date; it says only that IaC lets a second cell go up in 2-3 days.

**Reconciled Position**
- **Gate: 60 paying UAE clinics**, inside A01's 50-75. A26's 100 is dropped: in A01's realistic 120-180-clinic year it arrives around M9-10, leaving KSA only 2-3 selling months.
- **Four hard preconditions on top of the count:**
  1. KSA-region cell live and restore-tested (A22 RPO 15 min / RTO 4 h).
  2. KSA-law Arabic/English DPA signed off by counsel.
  3. KSA CST sender ID and Meta WhatsApp templates approved.
  4. Arabic UI production-ready.
- **Expected month: M7 (May 2027).** In the base case (~15-17 net adds/month from first revenue at M3), 60 clinics lands around M6.5-7. On the 300-goal pace (~33/month) it lands at M5, but KSA onboarding cannot start until the preconditions are met, so M6 is the earliest possible entry.
- **Engineering prep before the gate:**
  - **M1-3 (in MVP):** cell-ready design: IaC from week 1, a global control plane with no patient data, `clinic_id`→cell routing, Postgres RLS, UTC storage, the `MessageChannel` interface, Arabic/English UI. This absorbs most of A18's 3-6 eng-week dual-region overhead.
  - **M4:** start KSA counsel/DPA work and CST/WhatsApp registrations (2-6 weeks of lead time).
  - **M5-6:** stand up the KSA cell as staging with synthetic data only (2-3 days build + ~1 week test).
  - **At gate:** promote to production. Cell cost (300-600 USD/month) and ops (1-2 eng-days/month) start at M6-7, not M4.

**Adjustments Required**
- **A01:** Narrow 50-75 to 60 and add the four preconditions.
- **A16/A18:** Keep the stack+DPA blocker, add the CST sender ID and Arabic UI to it, and move KSA counsel spend to M4.
- **A22:** The KSA cell is staging-only at M5-6 and goes to production only at the gate. A first KSA contract no longer triggers deployment.
- **A26:** Replace "100+ UAE clinics" with 60, and move Riyadh entry to M7-12.
- **D3 Finance:** Start second-cell OpEx at M7.

**Residual Risk**
- If the UAE ramp is at the low end (~120/year), 60 slips to ~M8, leaving KSA 4-5 months and a small share of the 300 goal.
- The health-data reading is ASSUMED (WEB MODE OFF). If counsel rules appointment data is not health data, the separate cell may be unnecessary.
- KSA-region availability by M5 is ASSUMED.
- After M7 a single founder-seller splits across two markets, which may slow UAE adds unless a sales hire lands by M4 (A01).
- CST approval may take longer than 6 weeks.

---

## Orchestrator harmonisation

The reconcilers ran in isolation, so their shared inputs differ: burn ranges from 25.5k to 29.75k, messaging cost from 15 to 16.5 USD, and the KSA cell from "live at launch" to "staging M5-6". The blueprint uses one figure set:

| Item | Harmonised figure | Basis |
|---|---|---|
| Messaging COGS | 16.50 USD/clinic/month | Tech-vs-burn reconciler, the dedicated owner of this figure |
| Variable cost incl. support | ~25 USD/clinic/month (21 + 4 support) | Tech-vs-burn reconciler + support line from the CAC/LTV reconciler |
| Contribution at 79 USD | ~54-58 USD; **planning figure 55** | Both reconcilers converge here |
| Fixed burn | **~28k USD/month average** (23k M1-4 → 27.6k M7-12). ~30-32k without an offshore engineer | Roadmap-vs-runway reconciler, the only phased build that includes compliance and hires |
| Break-even at 79 flat | **~510 clinics** (28k / 55) | Derived |
| Break-even at 99 + metered messaging | **~330 clinics** (28k / 85) | Derived from the CAC/LTV repricing |
| LTV / CAC / ratio at 79 | ~1,830 / ~650 / **2.8x** | CAC/LTV reconciler |
| LTV / ratio at 99 metered | ~2,830 / **4.4x** | CAC/LTV reconciler |
| CapEx | 35k USD, plus a 25k KSA-entity contingency held outside runway | Scale-vs-CapEx reconciler |
| Runway | **7.5-8.5 months**, cash-out ~Jul 2027 (M9). 7.3 months if the 25k contingency is held and the offshore saving fails | Roadmap, tech and CapEx reconcilers |
| Fundraise | Start **M4 (Feb 2027)**, close **M8 (Jun 2027)**, target ~500k USD, minimum 250k bridge decided by M6 | Roadmap reconciler (overrides the "start M5" in the tech reconciler, because lead time needs M4) |
| KSA cell | Cell-ready IaC in the MVP; **staging M5-6, production at the 60-clinic gate (~M7)** | KSA-gate reconciler, consistent with the MVP reconciler. It overrides "live at launch" from the CapEx reconciler; the CapEx figure of 35k is unchanged |
| Volume | Base **150**, Stretch **230**, 300 GIVEN unplanned | Volume reconciler |
| Pilot | Week 11 (~18 Jan 2027); paid conversion end M3; booking link weeks 13-15 | MVP reconciler |
| Hires | Support specialist M5 (Mar 2027); seller M7 only if ≥40 paid at M6 AND bridge committed | Roadmap + volume reconcilers |
