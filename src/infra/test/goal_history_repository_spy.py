from src.data.interface import GoalHistoryRepositoryInterface
from src.domain.models import GoalHistory
from src.domain.test import mock_goal_history


class GoalHistoryRepositorySpy(GoalHistoryRepositoryInterface):
    """Spy to GoalHistory Repository"""

    def __init__(self):
        self.insert_goal_history_params = {}

    def insert_goal_history(
        self, expected: str, achieved: str, project_history_id: int
    ) -> GoalHistory:
        """Spy to all the attributes"""

        self.insert_goal_history_params["expected"] = expected
        self.insert_goal_history_params["achieved"] = achieved
        self.insert_goal_history_params["project_history_id"] = project_history_id

        return mock_goal_history()
