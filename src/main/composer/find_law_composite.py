from src.data.find_law import FindLaw
from src.infra.repo import LawRepository
from src.presenters.controllers import FindLawController


def find_law_composer() -> FindLawController:
    """Composing Find Law Route
    :param  - None
    :return - Object with Find Law Route
    """

    repository = LawRepository()
    use_case = FindLaw(repository)
    find_law_route = FindLawController(use_case)

    return find_law_route
