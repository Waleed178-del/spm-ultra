### A08: Agile Sprint & WBS Architect

**Key Findings**
- Engineering capacity (ASSUMED): 2 engineers (GIVEN) x ~30 focused hours/week = ~120 focused hours per 2-week sprint, ~26 sprints in 12 months, ~3,100 hours total. Confidence: Medium.
- Level-1 WBS for a scheduling MVP sized at ~720 hours (ASSUMED, bottom-up estimates), i.e. 6 sprints (12 weeks) with zero buffer, 7 sprints with a 15% buffer (Feb 2027 launch):
  - 1.0 Foundations (80 h): multi-tenant data model, auth/roles (owner, dentist, receptionist), hosting setup.
  - 2.0 Scheduling core (200 h): multi-chair/multi-dentist calendar, appointment types and durations, conflict detection, recurring slots.
  - 3.0 Patient comms (120 h): WhatsApp Business API + SMS reminders, confirm/cancel links.
  - 4.0 Localisation (90 h): Arabic RTL UI, Hijri/Gregorian date display, bilingual templates.
  - 5.0 Online booking widget (80 h): public booking page, embeddable link.
  - 6.0 Billing and subscription (70 h): 79 USD plan (GIVEN), invoicing, VAT handling (UAE 5%, KSA 15%: ASSUMED current rates).
  - 7.0 Onboarding/import (50 h): CSV/Excel patient import.
  - 8.0 Ops (30 h): monitoring, backups, logging.
- Critical path: 1.0 -> 2.0 -> 3.0 -> pilot release. WhatsApp Business API approval is an external dependency (ASSUMED lead time 1-4 weeks) and must start in Sprint 1. KSA data hosting (if in-country residency is required) is a second external dependency that can force re-platforming of 1.0. Confidence: Medium.
- Post-MVP (sprints 8-26, ~2,300 h) is consumed by: bug/support load (ASSUMED 20-30% of capacity once 100+ clinics live), PMS integrations (if required, 150-300 h each), reporting, and no-show analytics. Integrations are the largest scope risk.

**Critical Assumptions**
- GIVEN: 2 engineers, 12-month horizon, 79 USD pricing.
- ASSUMED: greenfield build (no existing code); engineers are full-stack; no dedicated QA/design; 2-week Scrum sprints; estimates carry +/-30% error.
- ASSUMED: no PMS integration is in MVP; clinics either use paper/Excel or tolerate double-entry for the pilot.

**Recommendations**
1. Freeze MVP scope to WBS 1.0-4.0 plus 6.0 for the Jan 2027 pilot release (~560 h, ~5 sprints); ship 5.0 and 7.0 in Sprints 6-7 before paid launch.
2. Sprint 1 (Nov 2026) must include: WhatsApp Business API application, hosting-region decision for KSA, and the tenant data model; these three unblock everything else.
3. Reserve a fixed 25% support/bug allocation per sprint from Sprint 8 onward rather than absorbing it ad hoc.
4. Gate any PMS integration behind evidence: only build one if 30%+ of lost deals cite it, and choose the single most-cited system.
5. Release cadence: pilot build every sprint to 10 pilot clinics from Sprint 4; definition of done includes Arabic strings and RTL QA.

**Cross-Dependencies**
- [A09] Supplies my capacity (120 h/sprint); I hand back the 720 h MVP estimate and the 25% support reserve for load modelling.
- [A21] CROSS-DEPENDENCY: MVP scope boundary (no PMS integration, no EMR) must be ratified by the MVP Scope Rationalizer.
- [A22] CROSS-DEPENDENCY: critical-path dependencies on WhatsApp API and KSA data residency need architecture confirmation.
- D4 (Risk & Compliance) CROSS-DEPENDENCY: whether patient appointment data counts as health data under KSA PDPL / UAE health-data rules determines hosting location for WBS 1.0.

**References**
- PMI, Practice Standard for Work Breakdown Structures (100% rule, deliverable-oriented decomposition).
- Schwaber & Sutherland, The Scrum Guide (2020).
- No external sources (web mode off); VAT rates and API lead times ASSUMED, confirm via UAE FTA, ZATCA and Meta documentation.
