from src.data.register_type_file import RegisterTypeFile
from src.infra.repo import TypeFileRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterTypeFileController


def register_type_file_composer() -> RouteInterface:
    """Composing Register TypeFile Route
    :param  -   None
    :return -   Object with Register TypeFile Route
    """

    repository = TypeFileRepository()
    use_case = RegisterTypeFile(repository)
    register_type_file_route = RegisterTypeFileController(use_case)

    return register_type_file_route
