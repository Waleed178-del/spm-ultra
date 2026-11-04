### A11: CapEx Estimator

**Key Findings** (bulleted, quantified)
- Total one-off launch investment is modest: **~33,000 USD base case (range 22,000-48,000 USD), ASSUMED**, i.e. ~13% of the 250,000 USD GIVEN seed. CapEx does not kill this business. Recurring burn does, and that belongs to [A12]. Confidence: Medium.
- Breakdown (all ASSUMED, base / range):
  - Hardware (3 laptops, test phones/tablets for iOS/Android booking flows): **7,000 USD** (4,000-9,000). This is the only true IAS 16 PP&E item. Straight-line depreciation over 3 years gives ~195 USD/month. If the team already owns laptops this falls to ~2,000 USD.
  - Legal entity setup: one UAE free-zone licence plus establishment card, first year: **9,000 USD** (6,000-15,000). Basis: typical free-zone package pricing, to be confirmed against current DMCC/IFZA/Meydan fee sheets. A Saudi entity (MISA licence plus CR) would add **15,000-30,000 USD** and is excluded from the base case. I assume KSA clinics are served cross-border from the UAE entity in year 1.
  - Legal documents (ToS, DPA, patient-data processing terms aligned with UAE PDPL and KSA PDPL), trademark filing in UAE and KSA: **6,000 USD** (4,000-9,000).
  - Pre-launch security review and penetration test, needed because the product stores patient names, phone numbers and appointment reasons: **5,000 USD** (3,000-8,000).
  - Arabic localisation (professional translation of UI and templates, RTL QA): **3,000 USD** (2,000-5,000).
  - Messaging setup (WhatsApp Business API provider onboarding, SMS sender-ID registration in UAE/KSA): **1,000 USD** (500-2,000).
  - Brand, website, sales collateral (Arabic and English): **2,000 USD** (1,500-4,000).
- Internally built software is excluded from PP&E. Under IAS 38 development cost may be capitalised only once technical feasibility is shown. At pre-MVP stage engineer salaries should be expensed and treated as OpEx [A12]. Capitalising them would flatter EBITDA without changing cash. Confidence: High.
- Timing: ~75% of CapEx (~25,000 USD) falls in months 1-2, before revenue. Confidence: Medium.

**Critical Assumptions** (bulleted, GIVEN vs ASSUMED)
- GIVEN: 250,000 USD seed; team of 2 engineers plus 1 founder; markets UAE and KSA; start Nov 2026.
- ASSUMED: product is pre-MVP; cloud hosted (no servers bought); no on-premise install at clinics (no tablets or kiosks supplied to clinics).
- ASSUMED: a single UAE entity in year 1. Confirm through KSA Ministry of Investment (MISA) guidance and a local tax adviser whether cross-border B2B SaaS sales to Saudi clinics trigger KSA VAT registration (15%) or ZATCA e-invoicing obligations.
- ASSUMED: no hardware is given to clinics. If clinics expect a front-desk tablet, add **~300 USD per clinic**, or ~90,000 USD at 300 clinics. That would break the model.

**Recommendations** (numbered, actionable)
1. Cap CapEx at **35,000 USD**. Defer the KSA entity until KSA reaches 50 or more paying clinics or legal advice requires one.
2. Do not supply hardware to clinics. Design the product to run in a browser or on the clinic's existing phone or PC.
3. Book the pen test for MVP month 3-4, not before code is stable. Budget a re-test (~2,000 USD) in month 10.
4. Expense all engineering salaries until MVP is live with paying clinics. Revisit IAS 38 capitalisation only for audited accounts at Series A.

**Cross-Dependencies** (each line starts with a peer tag, e.g. [A12])
- [A12] Needs from me: ~33,000 USD one-off spend in months 1-2, which reduces the cash available for runway to ~217,000 USD. Depreciation is ~195 USD/month (non-cash).
- [A13] Fixed-cost base for break-even should exclude CapEx except depreciation.
- [A15] Year-0/Year-1 outflow of 33,000 USD (range 22,000-48,000).
- [A22] I need confirmation that the architecture is cloud-only, with no on-premise PMS connectors that need hardware.
- [A24] Hosting is in OpEx. Any data-residency requirement (KSA data kept in-Kingdom) may force a second cloud region. I need that decision from them.
- [A25] I need vendor quotes for the WhatsApp BSP and free-zone licence.
- CROSS-DEPENDENCY (Risk and Compliance directorate): whether a KSA entity and in-Kingdom hosting are mandatory. Either adds 15,000-30,000 USD CapEx.

**References** (frameworks applied and any external sources)
- IAS 16 Property, Plant and Equipment (recognition and depreciation of hardware); IAS 38 Intangible Assets (development-cost capitalisation test).
- No external sources (WEB MODE OFF). All prices ASSUMED. Confirm via free-zone fee schedules, MISA, and WhatsApp BSP price lists.
