from src.data.register_type_project import RegisterTypeProject
from src.infra.repo import TypeProjectRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterTypeProjectController


def register_type_project_composer() -> RouteInterface:
    """Composing Register TypeProject Route
    :param  -   None
    :return -   Object with Register TypeProject Route
    """

    repository = TypeProjectRepository()
    use_case = RegisterTypeProject(repository)
    register_type_project_route = RegisterTypeProjectController(use_case)

    return register_type_project_route
