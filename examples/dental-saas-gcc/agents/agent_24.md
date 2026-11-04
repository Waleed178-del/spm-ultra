### A24: Scalability & Tech-Debt Estimator

**Key Findings**
- **Load baseline (ASSUMED: 25 appointments per clinic per day, 24 working days a month, 2 reminders per appointment).**

| Scale | Clinics | Appts/day | Outbound msgs/month | DB growth/yr | Infra USD/mo (ASSUMED) |
|---|---|---|---|---|---|
| 1x (goal) | 300 (GIVEN) | 7,500 | ~360k | ~8 GB | 400-800 (2 cells) |
| 10x | 3,000 | 75,000 | ~3.6M | ~80 GB | 2,000-4,000 |
| 100x | 30,000 | 750,000 | ~36M | ~800 GB | 15,000-30,000 |

  The basis for DB growth is about 3 KB per appointment, covering the appointment row plus message-event logs. Compute and database are trivial at 1x and modest at 10x. **High confidence.**
- **Messaging is the cost that scales, not infrastructure.** Each clinic sends about 1,200 messages a month. At an ASSUMED Meta utility-template rate of 0.01-0.02 USD per message, that is **12-24 USD per clinic per month, or 15-30% of the 79 USD price (GIVEN)**. Across 300 clinics it is about 3,600-7,200 USD a month, against infrastructure of about 600 USD. If the fallback is SMS at an ASSUMED 0.03-0.06 USD per message, the cost reaches 36-72 USD per clinic, or 46-91% of the price. The fallback rate must be capped. **High confidence on structure, Low on rates.** To confirm the rates, check the current Meta WhatsApp pricing page for the AE and SA markets.
- **Meta sender limits are the first scaling wall, and they hit at 1x, not at 100x.** A newly registered WhatsApp sender number starts at a low business-initiated messaging tier (ASSUMED 250-1,000 unique users per 24 h). It steps up only with message volume and quality rating. One shared sender number serving 300 clinics needs about 7,500 unique patients a day, so it must reach the 10k tier. That takes weeks of ramp, and a quality-rating drop from patients blocking messages throttles every clinic at once. **Medium confidence.**
- **Peak dispatch.** Reminders cluster around 09:00-10:00 local time. At 10x that is about 150k messages a day, or about 40 per second if spread over an hour. At 100x it is about 400 per second, which exceeds ASSUMED default per-number throughput (about 80 msgs/s). That calls for sharding across multiple sender numbers and rate-limited queues. **Medium confidence.**
- **100x is beyond the stated market.** ASSUMED: the UAE and KSA have about 8,000-12,000 independent dental clinics combined. To confirm, use DHA/DOH/MOHAP and Saudi MOH licensing registries. 30,000 clinics therefore requires moving into other GCC/MENA countries or other verticals, which means more cells and more data-residency regimes. **Medium confidence.**
- **Tech-debt and support drag on 2 engineers (GIVEN).** ASSUMED 1-2 support tickets per clinic per month at about 10 minutes each. At 300 clinics that is 50-100 h a month, or 0.3-0.6 FTE. Add about 15-20% of capacity for MVP-shortcut debt by month 9. Feature velocity then falls to about 50-60% of month 1-3 capacity unless support is staffed. **Medium confidence.**
- **Debt items that are expensive to fix later:** missing tenant isolation (row-level security), a retrofit of 3-5 eng-weeks; no i18n/RTL layer, 4-8 eng-weeks; single-cell assumptions hard-coded, 3-6 eng-weeks; and storing local time instead of UTC (ASSUMED estimates).

**Critical Assumptions**
- GIVEN: 300 clinics, 79 USD/month, 2 engineers.
- ASSUMED: 25 appointments a day per clinic; 2 reminders per appointment; Meta utility rate 0.01-0.02 USD. These rates are direct Meta pricing and exclude any BSP markup.
- ASSUMED: managed Postgres and a container platform, priced like a mid-tier hyperscaler.

**Recommendations**
1. Default to **one reminder per appointment (24 h before)**, with a second only as a paid option or for unconfirmed bookings. This cuts messaging to about 6-12 USD per clinic per month.
2. Handle confirm/cancel replies inside the customer-service window opened by the patient's reply. Follow-ups sent within that window cost nothing extra (ASSUMED under Meta's current pricing model).
3. Cap SMS fallback at 10% of a clinic's messages per month, or pass SMS cost through to the clinic.
4. Plan the sender-number strategy now: either each clinic has its own number (spreads limits and quality risk, adds onboarding friction) or a pool of 3-5 shared numbers with gradual ramp. Do not use a single shared number.
5. Monthly partitioning of message-event tables is needed only at 10x. Do not build it now.
6. Budget for one support/onboarding hire once the company has 120-150 clinics, to protect engineering capacity.

**Cross-Dependencies**
- [A11]/[A12] CROSS-DEPENDENCY: messaging at 6-24 USD per clinic per month is the dominant cost of goods sold (COGS). It caps gross margin at about 70-85% before support, versus a typical 80%+ SaaS assumption.
- [A22] Cell topology holds to 10x without change. 100x adds more cells for new countries.
- [A05] Growth beyond about 10,000 clinics depends on regional expansion, not UAE and KSA alone.
- [A25] I need BSP-loaded per-message rates and throughput tiers to firm up these figures.

**References**
- Abbott & Fisher, The Art of Scalability (2009): AKF scale cube (Y-axis split by function, Z-axis split by country cell).
- No external sources (web mode off). All rates are ASSUMED.
