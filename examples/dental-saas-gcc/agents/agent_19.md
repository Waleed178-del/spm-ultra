### A19: Single Point of Failure Auditor

Method: SRE-style dependency audit (Beyer et al.). For each single dependency: the share of the business it carries, the redundancy that exists, the time to replace it, and the blast radius if it fails.

**Key Findings**
- **SPOF-1: the founder is 100% of sales, partnerships and fundraising (Critical, High confidence).** The founder is the only seller (GIVEN), so revenue pipeline depends on one person at 100%. Time to replace is ASSUMED at 3-6 months (hire and ramp a GCC SaaS seller, Arabic-speaking for KSA). Blast radius: new-clinic adds fall to ~0. A 4-week absence at the planned pace costs ~25-30 clinics (GIVEN pace: 25/month).
- **SPOF-2: two engineers, each likely owning separate components (High, Medium confidence).** The team is two engineers (GIVEN). Bus factor is ASSUMED at 1 per subsystem (backend vs. frontend/mobile). Losing one cuts delivery capacity by 50%, and backfill takes 2-4 months in the UAE (ASSUMED). There is no on-call rotation: one person is effectively on call 50% of the time, every week, all year.
- **SPOF-3: the messaging channel (High, Medium confidence).** Reminders are the core value of scheduling. If WhatsApp Business via a single BSP is the only reminder channel, then a Meta policy change, template rejection, number ban or per-conversation price increase (ASSUMED 20-50% risk of a material price change in 12 months) hits 100% of clinics. The same applies to a single SMS aggregator per country.
- **SPOF-4: a single cloud region per country (Medium).** Data residency forces in-country hosting [see compliance view]. With one region per country there may be only 2-3 availability zones and no in-country failover region. ASSUMED regional outage probability is <5% a year, but recovery depends on a single provider.
- **SPOF-5: a single payment processor (Medium).** Card recurring billing through one gateway. KSA card and mada coverage may require a local gateway (ASSUMED). Gateway suspension (a common KYC event for new merchants) freezes 100% of collections, which is up to 23.7k USD MRR (GIVEN arithmetic at 300 clinics).
- **SPOF-6: one acquisition channel (High).** If all leads come from founder outbound and walk-ins, there is no compounding channel. A 50% drop in founder availability halves pipeline.
- **SPOF-7: a single PMS integration, if built (Medium).** Betting the integration on one dominant regional PMS ties retention to that vendor's API terms. A revoked partnership could strand an ASSUMED 30-60% of users.

**Critical Assumptions**
- GIVEN: 1 founder-seller, 2 engineers, no other staff.
- ASSUMED: no co-founder with operating authority; no contractors; a single cloud provider; WhatsApp as the primary reminder channel (dominant consumer messaging app in the GCC, ASSUMED).
- ASSUMED replacement times come from GCC hiring norms. Confirm via local recruiters.

**Recommendations**
1. SPOF-1: write a repeatable demo script and a CRM-logged pipeline by month 2. Add a commission-heavy part-time seller or a distributor partnership by month 4. Target: founder at no more than 60% of pipeline by month 6.
2. SPOF-2: mandatory code review across both engineers, shared on-call (1 week on, 1 week off), infra-as-code, and runbooks. Target bus factor of 2 on every production component by month 3.
3. SPOF-3: dual channel. WhatsApp primary with SMS fallback per country, through two aggregators where possible. Abstract the messaging layer so swapping a provider takes 1-2 weeks.
4. SPOF-5: pre-qualify a second gateway (one UAE-friendly, one KSA-local). Hold 2 months of opex in a second bank account.
5. SPOF-7: if a PMS integration is built, make it an adapter layer and support CSV/ICS import as the generic fallback.

**Cross-Dependencies**
- [A09] Needs the resource allocation split of founder hours: sales vs. fundraising vs. support. SPOF-1 assumes at least 70% on sales.
- [A22] CROSS-DEPENDENCY: architecture must expose provider-agnostic interfaces for messaging, payments and PMS.
- [A25] Needs the vendor shortlist for BSP, SMS aggregators and payment gateways in both countries, with contract exit terms.
- [A20] Hand-off: SPOF-1 through SPOF-5 with replacement times, to be used as RTO inputs.
- [A16]/[A17] Hand-off: founder-loss impact is 5 of 5, and engineer loss halves delivery capacity.

**References**
- Beyer, Jones, Petoff, Murphy, Site Reliability Engineering (O'Reilly, 2016): chapters on eliminating toil, on-call and dependency management.
- WEB MODE OFF: replacement times and price-change odds are ASSUMED. Confirm via recruiter quotes and BSP contract terms.
