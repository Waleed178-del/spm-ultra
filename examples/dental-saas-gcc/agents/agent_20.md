### A20: Disaster Recovery & Continuity Planner

Method: ISO 22301 business impact analysis (MTPD/RTO/RPO), with NIST SP 800-34 contingency tiers covering technical, people and financial continuity. Includes emergency pivot criteria.

**Key Findings**
- **Technical tolerance is low (High confidence).** A clinic that cannot see today's bookings stops front-desk operations within ~1-2 hours (ASSUMED). The proposed targets are **RTO 4h and RPO 15 min** for the booking database, and **RTO 24h** for analytics and admin. This is achievable with managed Postgres, point-in-time recovery and multi-AZ inside one in-country region. The added cost is ASSUMED at ~300-800 USD/month per country stack.
- **Backups must stay in-country (Medium confidence).** Standard cross-region DR (for example, UAE to EU) likely conflicts with health-data localisation. DR must therefore be multi-AZ plus encrypted in-country backups, plus a daily export to a second in-country store. If no second in-country location exists, accept the residual risk and document it.
- **Reminder continuity:** if the messaging channel fails, no-show prevention stops. Required fallback: automatic switch from WhatsApp to SMS within 1 hour. Required manual fallback: a daily schedule PDF/CSV emailed to each clinic at 06:00 local, so the front desk can call patients.
- **Financial continuity is the most probable disaster (High confidence).** ASSUMED burn of ~24k USD/month (3 FTE plus infra plus messaging plus travel) against 250k (GIVEN) gives ~10.4 months of runway with zero revenue. A fundraise takes 4-6 months (ASSUMED), so it must start by **month 5-6** at the latest.
- **People continuity:** with 3 people (GIVEN), losing any one is a Tier-1 continuity event. The founder holds the bank, cloud-root and domain credentials. Without a break-glass procedure, losing the founder could lock the company out of its own infrastructure.

**Critical Assumptions**
- GIVEN: 250k USD, 3-person team, 12-month horizon, 2 countries.
- ASSUMED: managed cloud with in-country regions; burn ~24k USD/month; fundraising lead time 4-6 months; clinics book same-day, so tolerance is measured in hours.
- ASSUMED: no revenue before month 4.

**Recommendations**
1. Technical DR: multi-AZ managed DB, PITR at 15 min, encrypted daily snapshots retained 35 days in-country, and quarterly restore drills (target restore within 2h). Document the RTO/RPO in clinic contracts as 99.5% monthly uptime (ASSUMED).
2. Hot swap: abstract messaging and payments so a provider switch is a config change. Pre-sign a backup SMS aggregator in each country.
3. Break-glass: hardware security keys plus a sealed credential escrow (lawyer or board member). Give at least 2 people root access to cloud, domain, bank and app stores by month 1.
4. Runway trip-wires and emergency pivots:
   - **Month 6 check:** fewer than 40 paying clinics, or MRR under 3k USD. Freeze KSA, go UAE-only, and cut burn ~20% (one engineer to 0.5 FTE or contract).
   - **Runway under 6 months** with no term sheet in progress: start a bridge from angels and dental-distributor strategics.
   - **Month 9 check:** fewer than 90 paying clinics, or logo churn above 5%/month. Pivot the offer to bundled no-show/recall automation sold through PMS vendors or distributors (B2B2B). Alternatively re-price to 129-149 USD (ASSUMED) for fewer, larger multi-chair clinics.
   - **Hard floor:** cash of 3 months of burn (~72k USD) triggers wind-down or acqui-hire talks, preserving customer data return obligations.
5. Customer exit continuity: a one-click export of all appointments (CSV/ICS) per clinic, so a shutdown does not strand clinics. This also reduces regulatory exposure.

**Cross-Dependencies**
- [A12] CROSS-DEPENDENCY: needs the confirmed monthly burn and runway curve. The trip-wire dates assume ~10 months of runway.
- [A19] Uses the SPOF list. Founder and messaging channel are the two top continuity events.
- [A22] CROSS-DEPENDENCY: in-country multi-AZ topology and provider-abstraction layers must be in the MVP architecture, not retrofitted.
- [A17] Hand-off: outage risk at P ~10% / I=4 is mitigated to I=2 once RTO 4h is proven by drill. Financial runway risk remains top.

**References**
- ISO 22301:2019 Business continuity management systems (BIA, RTO/RPO, MTPD).
- NIST SP 800-34 Rev.1 Contingency Planning Guide for Federal Information Systems.
- WEB MODE OFF: cloud costs and fundraising lead times are ASSUMED. Confirm with provider pricing calculators and MENA VC data (e.g., MAGNiTT).
