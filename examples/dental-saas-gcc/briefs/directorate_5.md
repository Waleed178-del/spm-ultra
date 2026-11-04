## Directorate 5 Brief: Product, Tech Stack & Technical Architecture (Agents 21-25)

**Directorate Verdict**
Two engineers (GIVEN) can build the product. A modular monolith runs comfortably at 300 clinics (GIVEN) and at 10x, and infrastructure costs about 400-800 USD a month. The real constraints are elsewhere:
- **Time to a sellable MVP:** about 10-12 weeks.
- **Unit economics:** WhatsApp messaging is the dominant variable cost, about 9-18 USD per clinic per month, or 11-23% of the 79 USD price (GIVEN).
- **Data residency:** probably one hosting cell per country.
- **Founder time:** onboarding and support consume it unless onboarding is self-serve.

The technical side is feasible, but it leaves the sales motion about 7.5 effective selling months, which requires about 40 net new clinics a month. **Confidence: Medium.**

**Consolidated Findings**
1. **MVP scope** is a chair/dentist calendar, a minimal patient record, a CSV patient import, WhatsApp reminders with confirm/cancel/reschedule buttons and per-appointment status, Arabic/English patient messages with RTL-ready UI components, and clinic sign-up plus billing. Deferred: PMS/EHR integration, insurance and claims (including NPHIES, the Saudi insurance platform), charting, native apps, analytics, multi-branch, and the public self-booking page (moved to month 4) [A21][A23]. **High.**
2. **Architecture** is a portable modular monolith (containers + PostgreSQL + queue), shared-schema multi-tenancy with row-level security, and one cell per country. A global control plane holds billing and routing and stores no patient data. Webhook idempotency, a 15-minute reconciliation job and a dead-letter queue are part of the MVP definition of done, because missed cancellations destroy staff trust [A22]. **High.**
3. **Data residency.** Appointment data linking a named patient to a dental clinic is probably health data. Under UAE Federal Law No. 2 of 2019 and KSA PDPL plus health-sector rules, this probably requires in-country hosting. This reading is ASSUMED and needs legal confirmation [A22]. **Medium.**
4. **Messaging is COGS and a scaling wall.** About 600 appointments per clinic per month (ASSUMED) at a loaded rate of 0.015-0.03 USD per message (ASSUMED) gives 9-18 USD per clinic at 1 reminder per appointment, or 18-36 USD at 2. SMS fallback at 0.03-0.06 USD per message must be capped. A new WhatsApp sender number starts at a low business-initiated tier (ASSUMED 250-1k unique users a day). 300 clinics need about 7,500 a day, so one shared number fails at 1x [A24][A25]. **Medium (structure High, rates Low).**
5. **Vendor risk.** Meta/WhatsApp is a strategic single-source supplier. Account suspension or template reclassification to "marketing" (ASSUMED 50-70% costlier) disables the core feature. The KSA region and a mada-capable gateway are bottleneck items. Stripe works for the UAE; KSA needs a regional gateway [A25]. **Medium.**
6. **Onboarding and support load.** Assisted 2-hour setups would take about 600 founder-hours. A self-serve target of 30 minutes or less brings that to 75-150 h. Support at 300 clinics is ASSUMED 50-100 h a month (0.3-0.6 FTE), and by month 9 it lowers engineering velocity to about 50-60% [A23][A24]. **Medium.**
7. **Scale ceiling.** 100x (30,000 clinics) exceeds the ASSUMED 8,000-12,000 independent dental clinics in the UAE and KSA combined. That level requires geographic or vertical expansion, meaning more cells and more residency regimes [A24]. **Medium.**

**Key Numbers**

| Metric | Value | GIVEN/ASSUMED | Source |
|---|---|---|---|
| Engineers | 2 | GIVEN | brief |
| Price | 79 USD/clinic/month | GIVEN | brief |
| MVP effort (resolved) | 30-36 eng-weeks | ASSUMED | [A21][A22][A23] |
| MVP to pilots | week 10-12 (mid/late Jan 2027) | ASSUMED | [A21] |
| Required sales pace after pilot gate | ~40 net clinics/month | ASSUMED (derived) | [A21] |
| Appointments/day at 300 clinics | ~7,500 | ASSUMED (25/clinic/day) | [A22][A24] |
| Messaging cost/clinic/month (1 reminder) | 9-18 USD (11-23% of price) | ASSUMED | [A25] |
| Infra, 2 cells, at 300 clinics | 400-800 USD/month | ASSUMED | [A24][A25] |
| Total vendor run-rate at 300 clinics | 4.2-8.4k USD/month (18-35% of MRR) | ASSUMED | [A25] |
| Implied gross margin before support | ~65-82% | ASSUMED (derived) | [A25] |
| Infra at 10x / 100x | 2-4k / 15-30k USD/month | ASSUMED | [A24] |
| RPO / RTO / availability | 15 min / 4 h / 99.5% | ASSUMED | [A22] |
| Founder onboarding hours (300 clinics) | 75-150 h self-serve vs ~600 h assisted | ASSUMED | [A23] |
| Support load at 300 clinics | 50-100 h/month | ASSUMED | [A24] |
| Activation target | ≥60% of trials activated in 7 days; first reminder <24 h | ASSUMED | [A23] |

**Internal Conflicts Resolved**
1. **Message rate.** [A24] used direct Meta rates (0.01-0.02 USD) with 2 reminders per appointment, giving 12-24 USD per clinic. [A25] used BSP-loaded rates (0.015-0.03 USD). **[A25]'s loaded rate wins,** because the recommended start is a BSP. Combined with [A24]'s 1-reminder default, the result is **9-18 USD per clinic per month**.
2. **MVP size versus the date.** [A21] scoped 30-34 eng-weeks. [A23] added CSV import and status visibility (2-3 weeks) and [A22] added infrastructure as code plus idempotency (3-4 weeks), for 35-41 weeks against about 36 available by month 3. **Resolution:** the public self-booking page (5 weeks) moves to month 4. The "Reschedule" button notifies reception instead. Resolved scope is 30-36 eng-weeks, with a week 10-12 pilot date.
3. **One country or two cells.** [A21] recommends a UAE-first launch. [A22] designs two cells. **Resolution:** build cell-ready infrastructure as code from week 1, but deploy the KSA cell only when the KSA launch happens (months 4-5) or when the first KSA contract is signed.
4. **Sender-number strategy.** [A25] favours per-clinic numbers through embedded signup. [A23]'s 30-minute self-serve target conflicts with per-clinic Meta business verification. **Resolution:** default to a pool of 3-5 platform numbers ramped during the pilot, with per-clinic numbers as an opt-in [A24].
5. **Arabic scope.** [A21] puts Arabic in the patient flow at launch. [A23] requires RTL-aware components from sprint 1. Both stand. The Arabic staff UI is a precondition for the KSA launch, not for the MVP.

**Cross-Dependencies for Other Directorates**
- **CROSS-DEPENDENCY (D3 Finance, [A11][A12]):** model messaging as variable COGS of 9-18 USD per clinic per month (36 at 2 reminders). The vendor run-rate is 4.2-8.4k USD a month at 300 clinics, and infrastructure is negligible. Budget a support/onboarding hire at 120-150 clinics.
- **CROSS-DEPENDENCY (D4 Risk/Compliance, [A18][A19][A20]):** a legal ruling is needed on whether appointment data is health data in the UAE and KSA. It decides between 1 and 2 cells. Meta account suspension is the main single point of failure. Two engineers with no on-call rota is a people single point of failure. ZATCA e-invoicing and VAT handling for KSA billing also need a ruling.
- **CROSS-DEPENDENCY (D6 GTM, [A26][A30]):** the ideal customer is clinics without a usable digital scheduler (ASSUMED 40-60%), because there is no PMS integration. The effective selling window is about 7.5 months at about 40 clinics a month. The 7-day activation rate is the retention leading indicator.
- **CROSS-DEPENDENCY (D2 Operations, [A08][A10]):** the sprint plan must protect week 10-12. Receptionist training is needed to move them off paper diaries.
- **CROSS-DEPENDENCY (D1 Strategy, [A03][A05]):** Meta holds high supplier power. Growth beyond about 10,000 clinics requires regional expansion.
