"""Static topology of the SPM Ultra cluster: 6 directorates x 5 specialist agents."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Agent:
    id: int
    name: str
    mandate: str


@dataclass(frozen=True)
class Directorate:
    id: int
    key: str
    name: str
    section_title: str
    agents: tuple[Agent, ...] = field(default_factory=tuple)

    @property
    def agent_range(self) -> str:
        return f"Agents {self.agents[0].id}-{self.agents[-1].id}"


DIRECTORATES: tuple[Directorate, ...] = (
    Directorate(
        1, "strategy", "Strategic & Market Intelligence",
        "Section I: Strategic Position & Market Forces",
        (
            Agent(1, "SWOT Matrix Specialist",
                  "Map internal Strengths and Weaknesses against external Opportunities and Threats."),
            Agent(2, "PESTLE Macro Analyst",
                  "Assess Political, Economic, Social, Technological, Legal and Environmental headwinds."),
            Agent(3, "Porter's Five Forces Specialist",
                  "Evaluate competitive rivalry, supplier power, buyer power, substitutes and barriers to entry."),
            Agent(4, "Blue Ocean Strategist",
                  "Identify uncontested market space and value innovation moves that break away from competition."),
            Agent(5, "Trend & Horizon Forecaster",
                  "Evaluate long term viability against the industrial shifts expected over the next 3 to 5 years."),
        ),
    ),
    Directorate(
        2, "operations", "Operational Roadmap & Target Mapping",
        "Section II: Operational Milestones & Tracking Roadmap",
        (
            Agent(6, "SMART Taxonomy Engine",
                  "Re-engineer vague goals into Specific, Measurable, Achievable, Relevant, Time-bound targets."),
            Agent(7, "OKR Cascader",
                  "Translate strategic objectives into departmental Key Results and progress metrics."),
            Agent(8, "Agile Sprint & WBS Architect",
                  "Build the Work Breakdown Structure with explicit dependencies and task hierarchies."),
            Agent(9, "Resource Allocation Modeler",
                  "Map headcount, hours and skillsets per milestone phase and flag burnout risk."),
            Agent(10, "Change Management Planner",
                  "Identify adoption friction and design the training and change roadmap."),
        ),
    ),
    Directorate(
        3, "finance", "Financial Feasibility & Economic Modeling",
        "Section III: Structural Financial Projections & Runway",
        (
            Agent(11, "CapEx Estimator",
                  "Model initial launch investment: hardware, licences, tooling and setup costs."),
            Agent(12, "OpEx Runway Modeler",
                  "Calculate recurring costs, infrastructure overhead, retainers and monthly burn."),
            Agent(13, "Break-Even & Yield Analyst",
                  "Pinpoint the unit volume or subscription count needed to reach net profitability."),
            Agent(14, "Monetization Architect",
                  "Stress test revenue models: freemium, tiered SaaS, transactional, licensing."),
            Agent(15, "NPV & ROI Calculator",
                  "Evaluate Net Present Value, Internal Rate of Return and payback window."),
        ),
    ),
    Directorate(
        4, "risk", "Risk, Compliance & Adversarial Stress-Testing",
        "Section IV: Defensibility, Compliance, & Risk Matrix",
        (
            Agent(16, "Project Pre-Mortem Lead",
                  "Assume total failure 12 months out and extract the exact causes."),
            Agent(17, "Probability/Impact Matrix Specialist",
                  "Rank structural risks into low, medium and catastrophic tiers with probability and impact."),
            Agent(18, "Regulatory & Compliance Watchdog",
                  "Verify regional data privacy law, industry standards and international regulation exposure."),
            Agent(19, "Single Point of Failure Auditor",
                  "Probe for single dependencies: one API, one person, one supplier, one channel."),
            Agent(20, "Disaster Recovery & Continuity Planner",
                  "Map fallback strategies, hot swap procedures and emergency pivot criteria."),
        ),
    ),
    Directorate(
        5, "tech", "Product, Tech Stack & Technical Architecture",
        "Section V: Architectural Stability & Product Scope",
        (
            Agent(21, "MVP Scope Rationalizer",
                  "Cut feature creep and define the leanest version that still delivers core value."),
            Agent(22, "Architectural Dependency Mapper",
                  "Examine system integration, data flow pipelines and infrastructure durability."),
            Agent(23, "UX/User Journey Flow Auditor",
                  "Review friction points, onboarding flow and accessibility benchmarks."),
            Agent(24, "Scalability & Tech-Debt Estimator",
                  "Project stability and cost issues at 10x and 100x scale."),
            Agent(25, "Procurement & Vendor Evaluator",
                  "Assess third party dependencies, cost to performance tiers and platform lock in."),
        ),
    ),
    Directorate(
        6, "gtm", "Commercialization & GTM Execution",
        "Section VI: Commercialization & GTM Channels",
        (
            Agent(26, "ICP & Persona Profiler",
                  "Define the ideal customer profile with explicit psychographic and behavioral metrics."),
            Agent(27, "GTM Channels Strategist",
                  "Identify high converting distribution channels, organic or partnership based."),
            Agent(28, "Positioning & Messaging Architect",
                  "Draft differentiated value propositions and messaging, no generic copy."),
            Agent(29, "CAC vs LTV Modeler",
                  "Test whether customer acquisition cost stays structurally below lifetime value."),
            Agent(30, "Scale & Retention Strategist",
                  "Design engagement loops, referral mechanics and stickiness levers to minimize churn."),
        ),
    ),
)

# Mandatory cross-functional checks run by the Master Orchestrator (agent id groups).
MANDATORY_CROSS_CHECKS: tuple[tuple[str, tuple[int, ...], tuple[int, ...]], ...] = (
    ("Operational Roadmap vs OpEx Runway", (6, 7, 8, 9, 10), (12,)),
    ("Scale parameters vs CapEx estimate", (24,), (11,)),
    ("Tech stack vendor choices vs OpEx burn", (22, 25), (12,)),
    ("CAC/LTV assumptions vs break-even volume", (29,), (13,)),
    ("Compliance requirements vs MVP scope", (18,), (21,)),
)


def all_agents() -> list[Agent]:
    return [a for d in DIRECTORATES for a in d.agents]


def agent_by_id(agent_id: int) -> Agent:
    for a in all_agents():
        if a.id == agent_id:
            return a
    raise KeyError(agent_id)


def directorate_of(agent_id: int) -> Directorate:
    for d in DIRECTORATES:
        if any(a.id == agent_id for a in d.agents):
            return d
    raise KeyError(agent_id)
