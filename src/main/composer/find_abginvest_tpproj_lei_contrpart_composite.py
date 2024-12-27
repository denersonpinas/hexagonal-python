from src.data.find_abginvest_tpproj_lei_contrpart import FindAbginvestTpprojLeiContrpart
from src.infra.repo import AbginvestTpprojLeiContrpartRepository
from src.presenters.controllers import FindAbginvestTpprojLeiContrpartController


def find_abginvest_tpproj_lei_contrpart_composer() -> (
    FindAbginvestTpprojLeiContrpartController
):
    """Composing Find AbginvestTpprojLeiContrpart Route
    :param  - None
    :return - Object with Find AbginvestTpprojLeiContrpart Route
    """

    repository = AbginvestTpprojLeiContrpartRepository()
    use_case = FindAbginvestTpprojLeiContrpart(repository)
    find_abginvest_tpproj_lei_contrpart_route = (
        FindAbginvestTpprojLeiContrpartController(use_case)
    )

    return find_abginvest_tpproj_lei_contrpart_route
