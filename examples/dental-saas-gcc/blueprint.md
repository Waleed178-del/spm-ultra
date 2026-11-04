# Master Feasibility Blueprint: Dental Clinic Scheduling SaaS (UAE + KSA)

Run: standard mode, 6 directorates, 30 specialists, 7 reconciliations. WEB MODE OFF.

---

### Executive Summary & Master Viability Matrix [Rating: Low Viability]

**Verdict: Low viability for the plan as submitted. The restructured plan below scores Medium.**

The submitted plan has three parts: 300 clinics in 12 months, 79 USD flat, a founder who sells alone, and 250k USD of seed. Each of these fails on its own:

1. **Volume.** One founder can reach about 150 net paying clinics. 300 needs about 165-185 demos a month against a ceiling of 60-80 [A06, A09, A16, A27]. P(goal miss) is about 80% [A17].
2. **Price.** At 79 USD flat with WhatsApp reminders bundled, contribution is about 55 USD per clinic. Break-even is about 510 clinics. **Hitting 300 still loses about 11-12k USD a month** [A13, A12, A29; reconciled].
3. **Cash.** Burn is about 28k USD a month once compliance and one support hire are included. 250k lasts about 7.5-8.5 months, so cash runs out around July 2027 (M9). That is before the 150-clinic base case is reached [A12, A15, A20; reconciled].

The underlying business is sound:
- The pain is real. No-shows are ASSUMED at 15-25%, worth 10-47x the fee [A04, A26].
- The tech is easy for 2 engineers [A21, A22, A24].
- At 99 USD with metered messaging, LTV:CAC is about 4.4x and break-even is about 330 clinics [A29, A13; reconciled].

**The restructured plan:** reposition as WhatsApp-first no-show recovery, reprice to about 99 USD with a capped messaging allowance, launch UAE-first, plan for 150 clinics with 230 as stretch, start fundraising in February 2027, and gate every hire on traction. With those changes this is a fundable niche SMB SaaS, but it is a two-round company, not a one-round one.

**Data caveat:** WEB MODE was OFF. Every market figure is ASSUMED and is a hypothesis to verify. That covers clinic counts, no-show rates, WhatsApp rates, competitor prices, churn, CAC and regulatory readings. GIVEN figures are only: 300 clinics, 12 months, 250k USD, 2 engineers + 1 founder, 79 USD.

| Dimension | Score (1-5) | One-line rationale |
|---|---|---|
| Strategic position & market | 3 | Real, quantifiable pain and an adequate pool (ASSUMED 5,000-9,000 clinics), but standalone scheduling is a red ocean, and AI front-desk tools will commoditise it by about 2028-29 [A01, A03, A05] |
| Operational executability | 2 | Founder is a 100% single point of failure for sales. Load reaches 125% even at 150 clinics [A09, A19] |
| Financial feasibility | 2 | 79 USD flat gives LTV:CAC 2.8x and break-even about 510 clinics. Seed covers about 8 months. NPV is positive only on terminal value [A13, A15, A29] |
| Risk & compliance | 2 | Appointment data is likely health data, which needs in-country hosting. KSA PDPL fines (SAR 5M) exceed the seed. Single-sourced on Meta [A18, A19] |
| Product & tech architecture | 4 | Modular monolith with country cells. MVP in about 29.5 eng-weeks. Infra about 400-800 USD/month at 300 clinics [A21, A22, A24] |
| GTM & commercialization | 3 | Clear ICP and wedge. Unit economics pass only after repricing. Channels beyond the founder are unvalidated [A26, A27, A29] |
| **Overall** | **2.7** | **Low as submitted. Medium if restructured** |

**Hard Truth:** At 79 USD the business loses money even if it hits 300 clinics, and one founder cannot get past about 150. The 250k seed is not a path to break-even. It buys about 8 months to prove 40-70 paying clinics and raise about 500k by mid-2027. If that raise fails, the company stops [A13, A15, A16, A20].

---

### Section I: Strategic Position & Market Forces (Agents 1-5 Summary)

**PESTLE** [A02]
- **Legal (dominant):** UAE Federal Law 2/2019 on health-data localisation and KSA PDPL + NCA point to in-country hosting in each country. The cost is about 15-30k USD a year.
- **Economic:** VAT is 5% in the UAE and 15% in KSA. KSA may also trigger ZATCA e-invoicing.
- **Social/technical:** the product needs Hijri dates, per-country weekends, Arabic RTL and WhatsApp as the default channel.
- **Seasonality:** Ramadan (about Feb-Mar 2027) and Jul-Aug cut effective selling months to about 8.
- Confidence: High on localisation, Medium on the regulatory reading.

**SWOT** [A01]
- **Strengths:** focused vertical, low build cost, bilingual and WhatsApp-native.
- **Weaknesses:** a single seller, no stated network, pilots or PMS integration.
- **Opportunities:** no-show recovery, recall, waitlist auto-fill, and small chains of 2-5 sites.
- **Threats:** PMS suites bundling free scheduling (P 40% [A17]), marketplaces, and the free manual-WhatsApp substitute.

**Five Forces** [A03]
- Rivalry: HIGH. Substitutes: HIGH (a receptionist plus a phone).
- Entry barriers: low to moderate.
- Supplier power: HIGH (Meta/WhatsApp) [A03, A25].
- At 79 USD the product is stuck in the middle: standalone tools are ASSUMED at 20-60 USD and PMS suites at 50-300 USD.

**Blue Ocean** [A04]
- Eliminate: EMR, billing and claims.
- Raise: two-way WhatsApp confirmation and Arabic-first UX.
- Create: a waitlist refill and a monthly "recovered revenue" report.
- Positioning: "fill empty chairs", not "online booking".
- The uncontested window is ASSUMED at about 24-36 months [A04, A05].

**Horizon** [A05]
- The independent clinic pool shrinks an ASSUMED 10-20% over 5 years through consolidation.
- In about 60% of scenarios, an AI receptionist becomes the winning form.
- Build this as phase 1 of an AI front desk, with multi-location tenants.

**Market math**
- Pool: ASSUMED 5,000-9,000 independent clinics, planning midpoint 6,500 [A01, A03, A26].
- 300 clinics means about 4.6% penetration in year 1 from a cold start [A01].
- Sequence: UAE first (Dubai and Sharjah), KSA behind a clinic-count gate (see VII) [A01, A26; reconciled].

---

### Section II: Operational Milestones & Tracking Roadmap (Agents 6-10 Summary)

**SMART goal, re-baselined** [A06; reconciled]

Definition of "paying": invoice settled, not refunded within 30 days, and 50 or more appointments booked in the trailing 30 days.

| Quarter end | Committed Base | Stretch | Gate decision |
|---|---|---|---|
| Q1 (Jan 2027) | 10-15 paid pilots | 15-20 | Confirm support specialist hire |
| Q2 (Apr 2027) | 40 | 50 | At 40 or more, plus a committed bridge: hire Arabic-speaking seller (M7). Drop distributor if fewer than 3 closes in 60 days |
| Q3 (Jul 2027) | 100 | 130 | KSA production only after the 60-UAE-clinic gate |
| Q4 (Oct 2027) | **150** (MRR 11,850 USD) | **230** (MRR 18,170 USD) | 300 (GIVEN) stays the stated goal and is unplanned |

**OKR structure** [A07]
- One owner per function: the founder (Sales/CS), Engineer 1 (core product), Engineer 2 (platform, localisation, messaging).
- At most 3 KRs per owner per quarter.
- Every count KR is paired with an activation or retention KR. Example: 80% or more of bookings made in the product by day 14 [A10, A30].

**WBS and critical path** [A08, A21; reconciled]
- Pilot MVP: about 29.5 eng-weeks. This includes a 6 eng-week compliance block.
- Critical path: Foundations, then scheduling core, then WhatsApp reminders, then the compliance block, then the pilot.
- **Pilot: end of week 11, about 18 Jan 2027.** Billing ships weeks 12-13. Paid conversion happens at the end of M3. The public booking link ships weeks 13-15.
- External blockers that start in Sprint 1:
  - WhatsApp BSP approval and utility templates (1-4 weeks).
  - SMS sender IDs.
  - Legal ruling on health data.

**Resources** [A09; reconciled]

| Period | Headcount |
|---|---|
| M1-4 | 3 FTE (GIVEN) |
| M5 (Mar 2027) | Add a bilingual onboarding/support specialist (about 3k USD/month). Required even for Base |
| M7 (May 2027) | Add an Arabic-speaking commissioned seller (about 5k USD/month), only if 40 or more paid at M6 **and** a bridge is committed |
| Assumed throughout | One engineer remote or offshore (about −4k USD/month). If that is not possible, runway drops to about 7 months |

**Change management** [A10]
- The daily user is the receptionist, not the owner who signs.
- Required practices: a 14-day parallel run, a front-desk champion in each clinic, and a bilingual training kit.
- Onboarding: 3 h + 1 h at launch, falling to 1 h by M6 through a self-serve target of 30 minutes or less [A23].

---

### Section III: Structural Financial Projections & Runway (Agents 11-15 Summary)

All figures ASSUMED unless marked GIVEN. Reconciled figures override the directorate briefs.

| Metric | Value | Source |
|---|---|---|
| Seed | 250,000 USD (GIVEN) | brief |
| CapEx (launch) | **35,000 USD** (24-50k), plus a 25k KSA-entity contingency held outside runway | [A11; reconciled] |
| Fixed burn | 23k (M1-4), 26k (M5-6), 27.6k (M7-12). **Average about 28k USD/month**. 32.6k/month with the M7 seller | [A12, A09; reconciled] |
| Compliance cost | 25-55k USD in year 1. Planned at 2.5-3.3k USD/month | [A18; reconciled] |
| Messaging COGS | **16.50 USD/clinic/month** (600 appts × 1 reminder × 0.025 USD, plus a 10% SMS cap) | [A12, A25; reconciled] |
| Variable cost, all-in | about 25 USD/clinic (messaging, payments 2.5, hosting 2, support 4) | [A13, A25; reconciled] |
| Contribution at 79 USD | **about 55 USD/clinic/month** | [A13, A29; reconciled] |
| **Break-even at 79 USD flat** | **about 510 clinics** | derived, [A13] |
| **Break-even at 99 USD + metered messaging** | **about 330 clinics** (contribution about 85) | [A13, A14, A29; reconciled] |
| Runway | **7.5-8.5 months**. Cash-out about Jul 2027 (M9). The 3-month cash floor (about 85k) is hit around M6 | [A12, A20; reconciled] |
| Base case at M12 | 150 clinics × 55 = 8.3k contribution against 28k burn: **about −20k/month** | derived |
| Follow-on raise | **about 500k USD**. Start M4 (Feb 2027), close M8 (Jun 2027). Minimum bridge 250k, decided by M6 | [A15, A12; reconciled] |
| NPV (40% discount, 3x ARR terminal) | Plan +0.93M, Base +0.25M, Downside −0.31M USD. **Negative in every case without terminal value.** These used a 25k burn, so about −36k Y1 FCF from the higher reconciled burn | [A15] |

**Monetization** [A14]
- Reject freemium and per-booking fees.
- The recommended structure is tiers by number of dentists: Solo 59, Clinic 99 and Clinic Plus 149 USD, each with a reminder allowance and metered overage. Blended ARPA is about 94 USD.
- Add a 150 USD onboarding fee.
- Annual prepay at 10x monthly (A30 targets a 30-40% mix), which brings in about +60-90k of year-1 cash [A29].
- Price in AED/SAR. KSA's 15% VAT makes the counter price about 12% higher than in the UAE [A14].

**Hidden cost:** messaging. Two reminders per appointment by default would push COGS to about 31.50 USD and contribution below 50 USD [A25; reconciled]. A second reminder must be a paid add-on.

---

### Section IV: Defensibility, Compliance, & Risk Matrix (Agents 16-20 Summary)

**Top 5 fatal vulnerabilities**

| # | Risk | P | Impact | Mitigation | Source |
|---|---|---|---|---|---|
| 1 | Sales capacity: one founder caps out at 12-20 adds/month, so the 300 goal is missed | ~80% | High | Plan 150. Specialist hire at M5. Gated seller at M7. Distributor bounty (100-150 USD or a 12-month capped share). Referral loop | [A16, A17, A19, A27] |
| 2 | Runway ends before the follow-on raise | ~55% | Fatal | Start the raise M4. Annual prepay. Cut burn 20% if under 40 clinics at M6. Cash floor about 85k | [A17, A20; reconciled] |
| 3 | Health-data non-compliance (UAE Law 2/2019, KSA PDPL; fines up to SAR 5M, above the seed) | Medium | Fatal | Consent and opt-in logs, audit log, coded visit reason with no free text, 24-month retention, in-country hosting, 72h breach runbook, all in the MVP. Legal opinion by M2 | [A18; reconciled] |
| 4 | Meta/WhatsApp dependency: account suspension, template reclassification to "marketing" (ASSUMED +50-70% cost), price changes, sender-tier throttling at about 7,500 sends/day | Medium | High | Lock templates to the utility category. A pool of 3-5 sender numbers. SMS fallback within 1h, capped at 10%. A provider-agnostic `MessageChannel` | [A19, A24, A25] |
| 5 | Receptionist non-adoption and churn above 4%/month (receptionist turnover drives 30-40% of churn) | ~45% | High | 14-day activation standard (80% or more). Morning WhatsApp summary. Monthly ROI report to the owner. Multi-user seats | [A10, A17, A30] |

Also tracked:
- PMS incumbents bundling free scheduling (P 40%) [A17].
- 79 USD price resistance for scheduling alone (P 35%) [A17].
- Bus factor of 1 per engineer, a single payment gateway (a KYC freeze stops 100% of collections), and founder-held root credentials [A19, A20].

**Compliance parameters** [A18, A20; reconciled]
- Treat appointment data as health data (ASSUMED, pending counsel).
- UAE-region hosting from day 1. RTO 4h / RPO 15 min, multi-AZ in-country with no cross-border DR.
- KSA-law DPA, CST sender ID and Arabic UI are gates for the KSA launch.
- The KSA entity (15-30k USD) waits for one of three triggers: a legal ruling, 50 KSA clinics, or a buyer requirement [A11; reconciled].

**Plan B triggers** [A16, A20, A29; reconciled]

| Point | Condition | Action |
|---|---|---|
| M6 (Apr 2027) | Fewer than 40 paid clinics, or MRR under 3k USD | Cut burn about 20%. Freeze KSA. No seller hire |
| M6 | CAC above 900 USD, churn above 4%/month, or contribution under 75 USD (repriced) | Cut the target to about 200 (stretch) or about 120 (base) and re-price |
| M6 | Bridge not committed | Seller and the 300 stretch are both off |
| M9 (Jul 2027) | Fewer than 90 clinics, or churn above 5% | Pivot to B2B2B through PMS vendors or distributors, or re-price to 129-149 USD |
| Any time | Cash floor of about 85k (3 months of burn) | Open wind-down or acqui-hire talks |

---

### Section V: Architectural Stability & Product Scope (Agents 21-25 Summary)

**MVP in scope** (29.5 eng-weeks, pilot about 18 Jan 2027) [A21, A23; reconciled]
- Chair and dentist calendar.
- Minimal patient record with no free-text notes.
- CSV patient import.
- WhatsApp utility reminders with confirm, cancel and reschedule-request buttons, plus per-appointment status.
- Arabic/English patient messages and RTL-ready components.
- Sign-up and roles.
- **Compliance block** (6 eng-weeks): consent and opt-in logs, append-only audit log, coded visit reason, 24-month auto-purge, UAE hosting, breach alerting.
- Billing ships weeks 12-13.

**Out of scope or deferred:**

| Item | Status |
|---|---|
| PMS/EHR integration | Deferred. Revisit only if 30% or more of lost deals cite it [A08] |
| Insurance, NPHIES, charting, native apps, multi-branch | Deferred |
| Public booking link | Weeks 13-15 |
| Arabic staff UI | Gate for the KSA launch |
| KSA production cell | At the gate (about M7) |

**Architecture and dependencies** [A22, A25]
- Portable modular monolith: containers, PostgreSQL with row-level security, and a queue.
- One cell per country. A global control plane holds no patient data.
- `clinic_id`→cell routing and IaC from week 1.
- Webhook idempotency, a 15-minute reconciliation job and a dead-letter queue are part of the definition of done. A missed cancellation costs the clinic's trust.
- Critical vendors: a Meta BSP, an SMS aggregator, and payment gateways (Stripe for the UAE; KSA needs a mada-capable regional gateway).

**Scalability** [A24]

| Scale | Infra cost | Note |
|---|---|---|
| 300 clinics | 400-800 USD/month | About 7,500 WhatsApp + 750 SMS sends/day |
| 10x | 2-4k USD/month | |
| 100x (30,000 clinics) | 15-30k USD/month | Exceeds the whole UAE+KSA independent pool, so growth past about 10k clinics means new regions and residency regimes |

Support load is 50-100 h/month at 300 clinics. Without the M5 support hire, engineering velocity falls to about 50-60% by M9 [A23, A24].

---

### Section VI: Commercialization & GTM Channels (Agents 26-30 Summary)

**ICP** [A26]
- Independent clinics in Dubai and Sharjah with 2-5 chairs and 1-4 dentists.
- 25-60 appointments a day, booked by phone and WhatsApp, with no patient-facing booking tool.
- Self-pay-heavy clinics are preferred [A04].
- Buyer: the owner-dentist. Champion and daily user: the receptionist.
- Demo only leads with 3 or more of the 4 behavioural markers. Clinics without a usable digital scheduler are an ASSUMED 40-60% of the market [A22].

**Positioning** [A28]
- "WhatsApp-first no-show prevention for dental clinics, Arabic and English. One saved appointment pays for the month."
- Against marketplaces: no per-booking commission.
- Against PMS suites: works alongside the existing PMS.

**Channels, in priority order** [A27; reconciled]

| # | Channel | Plan role |
|---|---|---|
| 1 | Founder field sales + WhatsApp outbound to a list of about 1,500 UAE clinics | Base: 90-140 gross |
| 2 | Referral loop from M4 | Base: 15-35 clinics [A30] |
| 3 | AEEDC Feb 2027 co-exhibit | Base: about 15 closes, low confidence because of timing |
| 4 | Dental-distributor partner from M5 | Stretch: 30-80 gross. 100-150 USD bounty or a 12-month capped share, never a perpetual 25% |
| 5 | Commissioned Arabic-speaking seller from M7 | Stretch: 35-55 gross. Gated |
| 6 | Paid digital | Capped at 1k USD/month until demo-to-close reaches 30% or more |

Kill rule: any channel with fewer than 3 closes in 60 days is cut.

**CAC/LTV boundaries** [A29; reconciled]

| Metric | 79 USD flat | 99 USD + metered messaging |
|---|---|---|
| Contribution/clinic/month | ~55 | ~85 |
| Churn | 3% | 3% |
| LTV | ~1,830 | ~2,830 |
| Blended CAC | ~650 | ~650 |
| LTV:CAC | **2.8x (fails)** | **4.4x (passes)** |
| Payback | ~12 months | ~7.6 months |

- Incremental GTM cash: 90k planned, 120k hard cap. Founder time is costed in the salary line, not here [A29].
- If CAC goes above 900 USD, LTV:CAC drops below 3x even at 99 USD.

**Retention** [A30]
- Clinics that activate are ASSUMED to churn at about 1.5%/month, against 4% or more for those that don't.
- The 7-day activation rate is the leading indicator. Target: 60% or more of trials activated, and the first reminder sent in under 24h [A23].
- Dunning (automatic payment retries and reminders) is in scope.

---

### Section VII: Contradiction Audit Log

| # | Cross check | Agents | Status | Reconciled resolution |
|---|---|---|---|---|
| 1 | Operational Roadmap vs OpEx Runway (mandatory) | A06, A09, A12, A15, A20 | **Conflict: high, resolved** | Phased burn of 23k → 27.6k (average about 28k) including compliance and the M5 hire. Runway about 8.5 months, cash-out about M9. Fundraise starts M4 and closes M8. Seller at M7 only if both gates are met |
| 2 | Scale parameters vs CapEx (mandatory) | A11, A24 | **Conflict: medium, resolved** | CapEx 35k including KSA cell setup. 25k KSA-entity contingency held outside runway, released on a trigger. Production KSA cell timing set by check 7 (staging M5-6, production at the gate) |
| 3 | Tech vendor choices vs OpEx burn (mandatory) | A12, A22, A25 | **Conflict: high, resolved** | Messaging 16.50 USD/clinic (1 utility reminder × 600 appts × 0.025), variable cost 21 USD, contribution about 58 (55 with support). A second reminder becomes a paid add-on. Templates locked to utility |
| 4 | CAC/LTV vs break-even volume (mandatory) | A13, A16, A29 | **Conflict: critical, resolved** | 79 USD flat is NO-GO: LTV:CAC 2.8x, break-even about 510. 99 USD with metered messaging is a conditional GO: 4.4x, break-even about 330. A16's 300-340 figure holds only under repricing |
| 5 | Compliance vs MVP scope (mandatory) | A18, A21 | **Conflict: high, resolved** | A 6 eng-week compliance block is added to the MVP. Booking link moves to weeks 13-15. Billing is split out of pilot scope. Pilot moves to week 11 (about 18 Jan 2027). KSA plane stays out of the MVP |
| 6 | 12-month clinic volume base case | A06, A09, A16, A27 | **Conflict: medium, resolved** | Base 150, stretch 230 (with the rep and distributor). 300 is the stated but unplanned goal. Raise sized on base |
| 7 | KSA entry gate and timing | A01, A18, A22, A26 | **Conflict: medium, resolved** | Gate is 60 paying UAE clinics plus 4 preconditions (restore-tested cell, KSA DPA, CST and templates, Arabic UI), expected about M7 (May 2027). Cell-ready IaC in the MVP, staging M5-6 |
| 8 | Monthly churn assumption | A06, A13, A17, A29 | Consistent (low) | Overlapping ranges. Base 2.5-3%. 4% or more is a trip-wire |
| 9 | MVP / pilot date | A08, A21 | Consistent (low) | Jan 2027 pilot in both. It now becomes week 11 under check 5 |

Orchestrator harmonisation: the reconcilers used slightly different shared inputs. The burn, messaging, break-even, runway and KSA-cell figures in this blueprint come from the harmonisation table at the end of `reconciliations.md`.

---

### Section VIII: Next 30 Days Command Plan (4 Nov – 4 Dec 2026)

| # | Action | Owner | Deadline | Done when |
|---|---|---|---|---|
| 1 | Run 25 owner and receptionist interviews in Dubai and Sharjah. Measure the no-show rate, appointments per month and willingness to pay at 79 vs 99 USD with a message allowance | Founder | 25 Nov | 25 logged interviews. Measured median appointments/month and no-show rate. Price-preference split recorded |
| 2 | Sign design partners at full price, starting at pilot (A16: re-price if more than 50% refuse) | Founder | 4 Dec | 10 signed LOIs with price and start date |
| 3 | Commission UAE and KSA counsel on four questions: is appointment data health data, does KSA need an entity or ZATCA/VAT registration, the DPA template, and WhatsApp consent rules | Founder | Engaged by 15 Nov, written opinion by 31 Dec | Engagement letter signed, questions sent, opinion date confirmed |
| 4 | Apply for a WhatsApp BSP. Submit utility reminder templates in AR and EN. Register UAE SMS sender IDs. Get 2 BSP rate quotes | Engineer 2 | 20 Nov | BSP account active, at least 3 templates approved, 2 written quotes. Messaging COGS re-checked against 16.50 USD |
| 5 | Build the cell-ready foundation: IaC, UAE region, Postgres RLS, `clinic_id`→cell routing, `MessageChannel` interface, CI/CD | Engineer 1 | 30 Nov | Staging deployed from IaC in under 1 hour from a clean account |
| 6 | Sprints 1-2: scheduling core (chair/dentist calendar), consent capture and audit-log schema | Engineers 1 + 2 | 4 Dec | Demo of booking, moving and cancelling an appointment in under 30s, with an audit-log entry |
| 7 | Lock the pricing structure: core about 99 USD with a 600-message allowance and metered overage, a Solo tier, annual prepay, onboarding fee | Founder | 1 Dec | Price sheet in AED/SAR published to design partners. Decision backed by the results of #1 |
| 8 | Build the ICP target list | Founder | 20 Nov | At least 1,500 Dubai and Sharjah independent clinics in the CRM, each scored on the 4 ICP markers |
| 9 | Hold distributor and AEEDC meetings | Founder | 4 Dec | Meetings with 3 dental distributors held. AEEDC co-exhibit go/no-go decided |
| 10 | Set up continuity basics: break-glass credential escrow, a second payment gateway pre-qualified, a 72h breach runbook drafted | Founder + Engineer 2 | 30 Nov | Escrow tested by a second person. Gateway KYC submitted. Runbook v1 filed |
| 11 | Prepare the fundraise (the raise starts M4, Feb 2027) | Founder | 4 Dec | List of 30 GCC angels and strategics. Data-room skeleton. KPI dashboard defined (paid clinics, activation, churn, CAC, contribution) |
