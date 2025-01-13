from src.data.register_project_contact_point import RegisterProjectContactPoint
from src.infra.repo import ProjectContactPointRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProjectContactPointController


def register_project_contact_point_composer() -> RouteInterface:
    """Composing Register ProjectContactPoint Route
    :param  -   None
    :return -   Object with Register ProjectContactPoint Route
    """

    repository = ProjectContactPointRepository()
    use_case = RegisterProjectContactPoint(repository)
    register_project_contact_point_route = RegisterProjectContactPointController(
        use_case
    )

    return register_project_contact_point_route
