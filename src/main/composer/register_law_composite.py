from src.data.register_law import RegisterLaw
from src.infra.repo import LawRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterLawController


def register_law_composer() -> RouteInterface:
    """Composing Register Law Route
    :param  -   None
    :return -   Object with Register Law Route
    """

    repository = LawRepository()
    use_case = RegisterLaw(repository)
    register_law_route = RegisterLawController(use_case)

    return register_law_route
