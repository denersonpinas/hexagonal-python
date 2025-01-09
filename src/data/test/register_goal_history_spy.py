from typing import Dict, Type

from src.data.interface import ProjectHistoryRepositoryInterface
from src.domain.models import GoalHistory
from src.domain.test import mock_goal_history
from src.domain.use_cases import RegisterGoalHistoryInterface


class RegisterGoalHistorySpy(RegisterGoalHistoryInterface):
    "Class te define use case: Register GoalHistory"

    def __init__(
        self, project_history_repository: Type[ProjectHistoryRepositoryInterface]
    ):
        self._project_history_repository = project_history_repository
        self.register_param = {}

    def register(
        self, expected: str, achieved: str, project_history_id: int
    ) -> Dict[bool, GoalHistory]:
        """Register goal history use case
        :param  -   expected: expected goal
                -   achieved: achieved goal
                -   project_history_id: foreign key to project history
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(expected, str)
            and isinstance(achieved, str)
            and isinstance(project_history_id, int)
            and len(expected) <= 500
            and len(achieved) <= 500
            and project_history_id > 0
        )

        if validate_entry:
            self.register_param["expected"] = expected
            self.register_param["achieved"] = achieved
            self.register_param["project_history_id"] = project_history_id

            response = mock_goal_history()

        return {"Success": validate_entry, "Data": response}
