from faker import Faker
from src.data.test import FindTypeProjectSpy
from src.infra.test import TypeProjectRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_type_project_controller import FindTypeProjectController

faker = Faker()


def test_route_all():
    """Testing Route method"""

    find_type_project_use_case = FindTypeProjectSpy(TypeProjectRepositorySpy())
    find_type_project_controller = FindTypeProjectController(
        find_type_project_use_case=find_type_project_use_case
    )
    http_request = HttpRequest()

    response = find_type_project_controller.route(http_request=http_request)

    # Testing Output
    assert response.status_code == 200
    assert response.body
