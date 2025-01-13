from src.data.register_proponent import RegisterProponent
from src.infra.repo import ProponentRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProponentController


def register_proponent_composer() -> RouteInterface:
    """Composing Register Proponent Route
    :param  -   None
    :return -   Object with Register Proponent Route
    """

    repository = ProponentRepository()
    use_case = RegisterProponent(repository)
    register_proponent_route = RegisterProponentController(use_case)

    return register_proponent_route
