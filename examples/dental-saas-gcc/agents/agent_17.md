### A17: Probability/Impact Matrix Specialist

Method: ISO 31000 risk identification, analysis and evaluation. Probability (P) is the 12-month likelihood. Impact (I) is on a 1-5 scale, where 5 = the company cannot reach its goal or survive. Score = P x I, with P as a fraction. Tiers: **Catastrophic** = score >=2.5 or I=5 with P>=40%; **Medium** = 1.0-2.5; **Low** = <1.0.

**Key Findings**

| # | Risk | P (ASSUMED) | I | Score | Tier |
|---|---|---|---|---|---|
| R1 | Goal miss: fewer than 300 paying clinics at month 12 | 80% | 4 | 3.2 | Catastrophic |
| R2 | Runway exhausted before Series A / break-even | 55% | 5 | 2.75 | Catastrophic |
| R3 | Founder unavailable or burnt out (sole seller) | 25% | 5 | 1.25 | Medium (watch: impact 5) |
| R4 | Monthly logo churn >4% | 45% | 4 | 1.8 | Medium |
| R5 | Health-data residency / PDPL non-compliance blocks sales in a market | 30% | 4 | 1.2 | Medium |
| R6 | WhatsApp/SMS reminder channel blocked or price-shocked | 30% | 3 | 0.9 | Low-Medium |
| R7 | Incumbent PMS vendor bundles free scheduling | 40% | 3 | 1.2 | Medium |
| R8 | Payment collection failure in KSA (cards, local gateway) | 35% | 2 | 0.7 | Low |
| R9 | Engineer attrition (1 of 2 leaves) | 25% | 4 | 1.0 | Medium |
| R10 | Major outage / data loss >24h | 10% | 4 | 0.4 | Low |
| R11 | Price resistance: 79 USD > willingness to pay for scheduling alone | 35% | 3 | 1.05 | Medium |

- Two catastrophic risks (R1, R2) are linked. A goal shortfall lowers revenue, and lower revenue shortens runway. Combined probability that at least one materialises: **~85%** (ASSUMED, correlated). Confidence: High that R1 is the top risk; Medium on exact probabilities.
- The 300 target implies ~25 net adds a month (GIVEN arithmetic). Base-rate for founder-led SMB SaaS from zero is ~8-15 net adds a month in year 1 (ASSUMED). That base-rate is the basis for R1 at 80%.
- R2 basis: ASSUMED burn of ~25k USD a month against 250k (GIVEN) gives ~10 months of runway with no revenue offset. Revenue at the realistic pace adds only ~1-1.5 months.
- The expected-loss concentration is heavy. R1 + R2 = **~45% of total matrix score** (5.95 of ~13.4).

**Critical Assumptions**
- GIVEN: target, budget, team size, price.
- ASSUMED: every probability above is analyst judgment from SMB vertical-SaaS base rates. None is market-verified (WEB MODE OFF).
- ASSUMED: the impact scale is anchored on "% of 300-clinic goal or runway lost". I=5 means >50% loss.

**Recommendations**
1. Treat R1 and R2 as one compound risk and track them on one dashboard: net paid clinics vs. a plan of 0/0/0/10/25/45/65/90/115/140/165/190 (ASSUMED re-baselined curve), plus months of runway left.
2. Set trip-wires. Fewer than 40 paid clinics at month 6, or runway under 5 months, triggers the contingency plan [A20].
3. Mitigate R3 and R9 cheaply: key-person insurance (ASSUMED ~1-2k USD a year), documented sales playbook, code ownership shared across both engineers.
4. Validate R11 by month 2 with 10 pilots at the full 79 USD and no discount. If more than 50% refuse, re-price or bundle reminders plus patient recall.
5. Re-score the matrix monthly. Any risk crossing into Catastrophic needs a named owner and a 14-day mitigation plan.

**Cross-Dependencies**
- [A16] Hand-off: R1 and R2 are the quantified forms of the premortem's Causes 1 and 2. A16 can use these probabilities.
- [A18] Needs confirmation of R5 probability: are dental appointment records "health data" under UAE Federal Law 2/2019 and the KSA PDPL?
- [A19] Needs the SPOF list to validate R3, R6 and R9 impact scores.
- [A20] Needs the trip-wire thresholds and the pivot options that are activated at them.
- [A10] CROSS-DEPENDENCY: clinic staff adoption (receptionists abandoning WhatsApp/phone booking) drives R4. The Change Management Planner must supply an onboarding success rate.

**References**
- ISO 31000:2018 Risk management, Guidelines (risk analysis and evaluation clauses 6.4.3-6.4.4).
- WEB MODE OFF: no external sources. Probabilities would be confirmed by GCC SaaS churn and conversion benchmarks (e.g., MAGNiTT, OpenView) and customer interviews.
