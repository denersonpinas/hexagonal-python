from src.data.find_abginvest_tpproj_lei import FindAbginvestTpprojLei
from src.infra.repo import AbginvestTpprojLeiRepository
from src.presenters.controllers import FindAbginvestTpprojLeiController


def find_abginvest_tpproj_lei_composer() -> FindAbginvestTpprojLeiController:
    """Composing Find AbginvestTpprojLei Route
    :param  - None
    :return - Object with Find AbginvestTpprojLei Route
    """

    repository = AbginvestTpprojLeiRepository()
    use_case = FindAbginvestTpprojLei(repository)
    find_abginvest_tpproj_lei_route = FindAbginvestTpprojLeiController(use_case)

    return find_abginvest_tpproj_lei_route
