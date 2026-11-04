### A25: Procurement & Vendor Evaluator

**Key Findings**
- **Kraljic classification of the vendor stack:**
  - *Strategic* (high impact, few suppliers): the **WhatsApp Business Platform**. Meta is the only source. BSPs only resell access and add tooling. Lock-in sits with the channel itself, not the BSP. **High confidence.**
  - *Bottleneck* (lower spend, hard to substitute): **in-country cloud hosting** in KSA, and a **KSA payment gateway** that supports mada, the Saudi debit-card network. Both have few suppliers and residency constraints.
  - *Leverage* (many suppliers): SMS gateways, transactional email, monitoring, error tracking.
  - *Non-critical*: source control, CI, design tools, CRM.
- **WhatsApp delivery options.** (a) Meta Cloud API directly: no markup, but the team builds template management, webhooks and onboarding itself. (b) A BSP (global or regional; candidates to evaluate include Twilio, 360dialog, Infobip, Gupshup and regional resellers): ASSUMED markup of 0.002-0.01 USD per message or a 50-500 USD monthly platform fee. **Loaded cost ASSUMED at 0.015-0.03 USD per utility message.** At 1 reminder per appointment that is about 9-18 USD per clinic per month. At 2 reminders it is about 18-36 USD. BSPs with "embedded signup" let each clinic connect its own number in about 10-20 min, which matters for the sender-number strategy. **Medium confidence.**
- **Hosting.** Hyperscaler region status changes often. ASSUMED as of Nov 2026: UAE regions are live on AWS, Azure and Oracle. KSA in-country options include Oracle and Google Cloud (Dammam), plus local providers such as STC Cloud. AWS and Azure KSA regions were announced, and whether they are live must be verified. No single provider may offer production-grade regions in both countries. This is why a portable stack matters ([A22]). Lock-in from a portable container + Postgres stack: about 2-4 eng-weeks to migrate a cell. Lock-in if serverless-proprietary: about 8-12 eng-weeks.
- **Payments (collecting 79 USD a month from clinics).** In the UAE, Stripe is available (ASSUMED). In KSA, Stripe availability for local merchants is limited (ASSUMED). Regional gateways (for example Tap, Moyasar, HyperPay, Checkout.com) support mada. ASSUMED fees: about 2.5-3.5% + about 0.25 USD per card transaction, or about 2-3 USD per clinic per month. Many clinics will prefer annual invoice plus bank transfer. That needs a manual reconciliation process the founder has to run. **Medium confidence.**
- **Tooling stack at 300 clinics (ASSUMED USD/month).**

| Item | USD/mo |
|---|---|
| Hosting, 2 cells | 400-800 |
| WhatsApp, loaded, 1 reminder/appt | 2,700-5,400 |
| SMS fallback (capped 10%) | 300-700 |
| Email, monitoring, error tracking, logging | 100-250 |
| Payment fees | 600-900 |
| Helpdesk + CRM + misc SaaS | 100-300 |
| **Total** | **~4,200-8,350** |

  That is about 18-35% of the 23,700 USD MRR (GIVEN). **Medium confidence.**
- **Vendor concentration risk.** Meta can suspend a WhatsApp Business account for quality or policy breaches, such as reminder templates reclassified as marketing. With no alternate channel that means 100% loss of the core feature. Template category matters: utility-classified templates are ASSUMED to cost about 50-70% less than marketing templates.

**Critical Assumptions**
- GIVEN: 250k USD seed, 79 USD/month, UAE + KSA.
- ASSUMED: all per-message, hosting and payment rates above. To confirm, use the Meta pricing page, BSP rate cards, cloud region pages and gateway merchant agreements.
- ASSUMED: the legal entity sits in one country, which affects gateway eligibility in the other.

**Recommendations**
1. Start on a BSP with embedded signup and no long contract (month-to-month, under 500 USD/month platform fee). Re-evaluate Meta Cloud API direct at about 1M messages a month, around 10x.
2. Keep SMS as a contractual second channel through a separate vendor. Test failover monthly.
3. Choose hosting per cell after checking the region is live. Contract no reserved instances or commitments before month 6.
4. Use two payment rails: card subscriptions (Stripe for the UAE, a mada-capable gateway for KSA) and annual prepay by bank transfer, offered at a discount of about 10-15% to cut payment fees and churn.
5. Lock reminder templates to the utility category and avoid promotional wording, so they are not reclassified.

**Cross-Dependencies**
- [A12] CROSS-DEPENDENCY: vendor run-rate is about 4.2-8.4k USD a month at 300 clinics, of which about 70% is messaging (WhatsApp + SMS). This must sit in the OpEx model as variable cost per clinic.
- [A11] No meaningful CapEx. Everything is OpEx/SaaS.
- [A19] CROSS-DEPENDENCY: Meta/WhatsApp is a strategic single-source dependency. Account suspension is a single point of failure for the core feature.
- [A22] Hosting may differ per cell. The architecture must stay portable.
- [A03] Meta's control over price and access is a strong supplier power.

**References**
- Kraljic, Purchasing Must Become Supply Management, HBR (1983).
- No external sources (web mode off). All vendor prices are ASSUMED.
