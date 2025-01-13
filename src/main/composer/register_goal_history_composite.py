from src.data.register_goal_history import RegisterGoalHistory
from src.infra.repo import GoalHistoryRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterGoalHistoryController


def register_goal_history_composer() -> RouteInterface:
    """Composing Register GoalHistory Route
    :param  -   None
    :return -   Object with Register GoalHistory Route
    """

    repository = GoalHistoryRepository()
    use_case = RegisterGoalHistory(repository)
    register_goal_history_route = RegisterGoalHistoryController(use_case)

    return register_goal_history_route
