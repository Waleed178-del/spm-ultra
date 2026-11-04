"""SPM Ultra: hierarchical 30 agent Strategic Planning Manager."""

from .orchestrator import ClaudeLLM, MasterOrchestrator, MockLLM, RunResult
from .registry import DIRECTORATES, all_agents

__all__ = ["ClaudeLLM", "MasterOrchestrator", "MockLLM", "RunResult", "DIRECTORATES", "all_agents"]
__version__ = "0.2.0"
