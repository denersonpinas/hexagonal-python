from src.data.register_abginvest_tpproj_lei_contrpart import (
    RegisterAbginvestTpprojLeiContrpart,
)
from src.infra.repo import AbginvestTpprojLeiContrpartRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterAbginvestTpprojLeiContrpartController


def register_abginvest_tpproj_lei_contrpart_composer() -> RouteInterface:
    """Composing Register AbginvestTpprojLeiContrpart Route
    :param  -   None
    :return -   Object with Register AbginvestTpprojLeiContrpart Route
    """

    repository = AbginvestTpprojLeiContrpartRepository()
    use_case = RegisterAbginvestTpprojLeiContrpart(repository)
    register_abginvest_tpproj_lei_contrpart_route = (
        RegisterAbginvestTpprojLeiContrpartController(use_case)
    )

    return register_abginvest_tpproj_lei_contrpart_route
