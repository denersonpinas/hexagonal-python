from src.data.find_type_project import FindTypeProject
from src.infra.repo import TypeProjectRepository
from src.presenters.controllers import FindTypeProjectController


def find_type_project_composer() -> FindTypeProjectController:
    """Composing Find Type_project Route
    :param  - None
    :return - Object with Find Type_project Route
    """

    repository = TypeProjectRepository()
    use_case = FindTypeProject(repository)
    find_type_project_route = FindTypeProjectController(use_case)

    return find_type_project_route
