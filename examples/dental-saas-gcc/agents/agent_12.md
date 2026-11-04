### A12: OpEx Runway Modeler

**Key Findings** (bulleted, quantified)
- Fixed monthly burn: **~24,500 USD/month in months 1-6, rising to ~27,500 USD/month in months 7-12**, averaging **~26,000 USD/month (range 19,000-32,000), ASSUMED**. Confidence: Medium.
- Base burn breakdown, months 1-6 (all ASSUMED):
  - 2 engineers, fully loaded (salary, UAE visa, health insurance, end-of-service gratuity accrual): **14,000 USD** (2 x 7,000). Basis: mid-level Gulf-based engineer cost. Offshore or remote hiring could cut this to ~8,000 USD.
  - Founder salary: **3,000 USD** (subsistence level).
  - Cloud hosting, monitoring, backups: **600 USD**, rising to ~1,200 USD by month 12.
  - Sales travel UAE to KSA (Riyadh, Jeddah, Dammam), roughly 1 trip per month: **1,500 USD**.
  - Marketing (paid search/social in Arabic, dental-association events): **3,000 USD**.
  - SaaS tools (CRM, dev tools, email, design): **500 USD**.
  - Accounting, legal retainer, VAT filing: **800 USD**.
  - Co-working or flexi-desk (often needed for the free-zone licence), visas, bank fees: **1,100 USD**.
- From month 7: add a part-time Arabic-speaking onboarding and support contractor (**1,500 USD**), higher hosting, and higher marketing (+1,000 USD). Total becomes ~27,500 USD.
- Variable cost per clinic, which scales with customers: WhatsApp/SMS reminders **~24 USD/clinic/month**, payment processing ~2.40 USD, incremental hosting ~2 USD, for **~28-29 USD/clinic/month, ASSUMED**. Basis: ~400 appointments per clinic per month x 2 messages x ~0.03 USD per message. Confirm against the Meta WhatsApp conversation-pricing sheet for UAE/KSA and local SMS gateway rates. This is **~36% of the 79 USD price** and the biggest hidden cost in the model. Confidence: Medium-Low.
- Runway with zero revenue: (250,000 GIVEN - ~33,000 CapEx ASSUMED from launch-cost estimate) / ~26,000 = **~8.3 months**. Cash runs out around **July 2027**. Confidence: Medium.
- Runway is longer if revenue ramps, but only by 1-3 months unless the ramp comes early (see downstream peers). The seed does not reliably fund 12 months of operations at this cost base. Confidence: Medium.

**Critical Assumptions** (bulleted, GIVEN vs ASSUMED)
- GIVEN: 2 engineers plus founder; 250,000 USD seed; 12-month horizon from Nov 2026.
- ASSUMED: team is UAE-based on employment visas. Gulf labour law requires end-of-service gratuity accrual (~6% of base).
- ASSUMED: no salaried salesperson. The founder alone does sales across 2 countries.
- ASSUMED: prices excluding VAT. VAT collected (5% UAE / 15% KSA) is pass-through and not revenue.
- ASSUMED: messaging cost is absorbed in the 79 USD price, not billed separately.

**Recommendations** (numbered, actionable)
1. Set a hard burn ceiling of **25,000 USD/month** fixed. Every new hire or retainer above it must be funded by MRR.
2. Locate at least one engineer in a lower-cost location (Egypt, Jordan, Pakistan or remote). This saves ~3,000-5,000 USD/month and adds ~2-3 months of runway.
3. Cap reminders per clinic (e.g. 600 messages included per month) or move messaging to a metered pass-through. This protects contribution.
4. Start follow-on fundraising (bridge or seed extension of ~250,000-400,000 USD) **by month 6 (May 2027)** while ~90,000 USD of cash remains.
5. Track three numbers monthly: net burn, months of runway, and variable cost per clinic.

**Cross-Dependencies** (each line starts with a peer tag, e.g. [A12])
- [A09] Fully loaded engineer cost of 7,000 USD/month is my assumption. Their resource plan should confirm headcount stays at 3 until month 7.
- [A13] Fixed cost ~26,000 USD/month average; variable ~28.50 USD/clinic/month.
- [A15] Monthly outflow series: 24,500 USD (M1-6), 27,500 USD (M7-12).
- [A20] Hosting budget of 600-1,200 USD/month covers a single region plus backups only, not hot standby.
- [A25] Need WhatsApp BSP and SMS gateway quotes for UAE and KSA. This is the most sensitive input.
- [A27] Marketing budget of 3,000-4,000 USD/month. They must confirm their channel plan fits it.
- CROSS-DEPENDENCY (Go-to-Market directorate): the founder is the only seller and also handles KSA travel. Sales capacity, not cash, may be the binding constraint.

**References** (frameworks applied and any external sources)
- Damodaran, Investment Valuation (operating-cost build-up, cash-burn framing).
- No external sources (WEB MODE OFF). Salary, messaging and licence costs are ASSUMED. Confirm via Gulf salary surveys (e.g. recruiter salary guides), Meta WhatsApp pricing and gateway quotes.
