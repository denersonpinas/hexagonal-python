from src.data.register_project_history import RegisterProjectHistory
from src.infra.repo import ProjectHistoryRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProjectHistoryController


def register_project_history_composer() -> RouteInterface:
    """Composing Register ProjectHistory Route
    :param  -   None
    :return -   Object with Register ProjectHistory Route
    """

    repository = ProjectHistoryRepository()
    use_case = RegisterProjectHistory(repository)
    register_project_history_route = RegisterProjectHistoryController(use_case)

    return register_project_history_route
