from src.data.register_thematic import RegisterThematic
from src.infra.repo import ThematicRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterThematicController


def register_thematic_composer() -> RouteInterface:
    """Composing Register Thematic Route
    :param  -   None
    :return -   Object with Register Thematic Route
    """

    repository = ThematicRepository()
    use_case = RegisterThematic(repository)
    register_thematic_route = RegisterThematicController(use_case)

    return register_thematic_route
