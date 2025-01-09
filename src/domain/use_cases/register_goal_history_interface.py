from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import GoalHistory


class RegisterGoalHistoryInterface(ABC):
    """Interface to Register GoalHistory use case"""

    @abstractmethod
    def register(
        self, expected: str, achieved: str, project_history_id: int
    ) -> Dict[bool, GoalHistory]:
        """Use Case"""

        raise Exception("Should implement method: register")
