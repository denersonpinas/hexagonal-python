from src.data.find_type_file import FindTypeFile
from src.infra.repo import TypeFileRepository
from src.presenters.controllers import FindTypeFileController


def find_type_file_composer() -> FindTypeFileController:
    """Composing FindTypeFile Route
    :param  - None
    :return - Object with FindTypeFile Route
    """

    repository = TypeFileRepository()
    use_case = FindTypeFile(repository)
    find_type_file_route = FindTypeFileController(use_case)

    return find_type_file_route
