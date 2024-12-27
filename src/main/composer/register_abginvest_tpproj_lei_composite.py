from src.data.register_abginvest_tpproj_lei import RegisterAbginvestTpprojLei
from src.infra.repo import AbginvestTpprojLeiRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterAbginvestTpprojLeiController


def register_abginvest_tpproj_lei_composer() -> RouteInterface:
    """Composing Register AbginvestTpprojLei Route
    :param  -   None
    :return -   Object with Register AbginvestTpprojLei Route
    """

    repository = AbginvestTpprojLeiRepository()
    use_case = RegisterAbginvestTpprojLei(repository)
    register_abginvest_tpproj_lei_route = RegisterAbginvestTpprojLeiController(use_case)

    return register_abginvest_tpproj_lei_route
