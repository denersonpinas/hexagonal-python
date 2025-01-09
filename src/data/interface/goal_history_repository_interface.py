from abc import ABC, abstractmethod

from src.domain.models import GoalHistory


class GoalHistoryRepositoryInterface(ABC):
    """Interface to GoalHistory Repository"""

    @abstractmethod
    def insert_goal_history(
        cls, expected: str, achieved: str, project_history_id: int
    ) -> GoalHistory:
        """abstractmethod"""
        raise Exception("Method not implemented")
