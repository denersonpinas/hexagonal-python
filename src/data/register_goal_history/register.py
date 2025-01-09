from typing import Dict, Type
from src.data.interface.goal_history_repository_interface import (
    GoalHistoryRepositoryInterface,
)
from src.domain.use_cases.register_goal_history_interface import (
    RegisterGoalHistoryInterface,
)
from src.domain.models import GoalHistory


class RegisterGoalHistory(RegisterGoalHistoryInterface):
    """Class to define goal history case: Register Goal History"""

    def __init__(self, goal_history_repository: Type[GoalHistoryRepositoryInterface]):
        self._goal_history_repository = goal_history_repository

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
            response = self._goal_history_repository.insert_goal_history(
                expected=expected,
                achieved=achieved,
                project_history_id=project_history_id,
            )

        return {"Success": validate_entry, "Data": response}
