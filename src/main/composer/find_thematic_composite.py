from src.data.find_thematic import FindThematic
from src.infra.repo import ThematicRepository
from src.presenters.controllers import FindThematicController


def find_thematic_composer() -> FindThematicController:
    """Composing Find Thematic Route
    :param  - None
    :return - Object with Find Thematic Route
    """

    repository = ThematicRepository()
    use_case = FindThematic(repository)
    find_thematic_route = FindThematicController(use_case)

    return find_thematic_route
