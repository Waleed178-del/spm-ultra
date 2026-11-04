### A22: Architectural Dependency Mapper

**Key Findings**
- **C4 context level.** The system has four outside dependencies: (1) the WhatsApp Business Platform through Meta or a Business Solution Provider (BSP), (2) an SMS gateway as fallback, (3) a subscription payment gateway, and (4) a cloud host. No PMS or EHR integration is in the MVP. Each dependency is a separate failure domain. WhatsApp is the one the value proposition rests on. **High confidence.**
- **Container level.** A modular monolith is right for 2 engineers (GIVEN): one web app (staff UI plus patient booking page), one API, one PostgreSQL database, and one background worker with a job queue for reminders and webhook handling. Microservices would add about 20-30% ops overhead (ASSUMED) with no benefit at 300 clinics. **High confidence.**
- **Data residency drives the topology.** UAE Federal Law No. 2 of 2019 on ICT in health fields restricts storing health data outside the UAE. KSA PDPL, in force since Sep 2024, and health-sector rules restrict cross-border transfer (ASSUMED reading; legal counsel must confirm). Appointment records that link a named patient to a dental clinic are probably health data. Treat as ASSUMED until [A18] confirms. One region serving both countries is therefore probably non-compliant for at least one of them. **Medium confidence.**
- **Recommended topology: two "cells".** Each cell is one identical stack deployed per country: a UAE cell and a KSA cell. A small global control plane holds only clinic account, billing and tenant routing, with no patient data. Tenancy is shared-schema multi-tenant with a `clinic_id` on every row plus Postgres row-level security. A second cell costs about 300-600 USD a month extra at this scale (ASSUMED) plus about 1-2 engineer-days a month of ops.
- **Reminder pipeline data flow.** Appointment is created, then a scheduled job fires (for example 24 h before), the outbound template goes to the BSP, delivery and read webhooks come back, and the patient's reply ("Confirm"/"Cancel") arrives by inbound webhook and updates the appointment state. Webhooks must be idempotent with deduplication keys, because BSPs retry and duplicate (Kleppmann, ch. 11). Missed webhooks need a reconciliation job every 15 minutes or so. Without it, cancelled slots stay booked and staff stop trusting the product. **High confidence.**
- **Time handling.** UAE is UTC+4 and KSA is UTC+3, and neither uses daylight saving. Store UTC and render in the clinic's time zone. This is low risk but must be built in from the start.
- **Durability targets (ASSUMED):** RPO 15 min (managed Postgres point-in-time recovery), RTO 4 h, 99.5% monthly availability, which is about 3.6 h of downtime a month. That is acceptable for B2B scheduling at this stage if reminders are queued and replayed after an outage.

**Critical Assumptions**
- GIVEN: 2 engineers, UAE and KSA markets, 300 clinics in 12 months.
- ASSUMED: appointment data is regulated health data in both countries (conservative position).
- ASSUMED: a hyperscaler or local provider has a live region in each country by Nov 2026. Candidates must be checked against current regional status pages.
- ASSUMED: about 25 appointments per clinic per day, which is about 7,500 appointments a day and about 15,000 outbound messages a day at 300 clinics, with peaks around 08:00-10:00 local time.

**Recommendations**
1. Build a modular monolith on portable components (containers + PostgreSQL + Redis or a Postgres-backed queue). Avoid provider-proprietary serverless so a KSA cell can run on a different provider than the UAE cell if needed.
2. Parameterise all infrastructure as code (Terraform or similar) from week 1, so a second cell can be stood up in 2-3 days.
3. Put every messaging provider behind one internal `MessageChannel` interface (WhatsApp primary, SMS fallback), so a BSP can be swapped in about 1-2 weeks rather than months.
4. Keep the global control plane free of patient data. Routing is by `clinic_id` to cell.
5. Add webhook idempotency, a reconciliation job and a dead-letter queue to the MVP definition of done. They are not optional hardening.

**Cross-Dependencies**
- [A18] CROSS-DEPENDENCY: I need a legal ruling on whether appointment data is health data in the UAE and KSA. It decides between one cell and two.
- [A19] CROSS-DEPENDENCY: the WhatsApp BSP is the main single point of failure, and two engineers with no on-call rota is a people single point of failure.
- [A20] RPO 15 min and RTO 4 h per cell. Reminder jobs must be replayable after recovery.
- [A11]/[A12] CROSS-DEPENDENCY: a second cell adds about 300-600 USD a month plus engineer time.
- [A24] Load figures above are the baseline for 10x and 100x projections.
- [A25] Vendor choice must support in-country hosting and the `MessageChannel` abstraction.
- [A08] Infrastructure as code and the idempotency work, about 3-4 eng-weeks, must be in the MVP sprint plan.

**References**
- Brown, C4 Model (context and container views).
- Kleppmann, Designing Data-Intensive Applications (2017): idempotency, exactly-once effects, reconciliation.
- Cell-based architecture pattern.
- UAE Federal Law No. 2 of 2019; KSA PDPL. Both cited from prior knowledge, not verified (web mode off).
