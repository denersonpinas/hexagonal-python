from faker import Faker
from src.data.test import FindLawSpy
from src.infra.test import LawRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_law_controller import FindLawController

faker = Faker()


def test_route_all():
    """Testing Route method"""

    find_law_use_case = FindLawSpy(LawRepositorySpy())
    find_law_controller = FindLawController(find_law_use_case=find_law_use_case)
    http_request = HttpRequest()

    response = find_law_controller.route(http_request=http_request)

    # Testing Output
    assert response.status_code == 200
    assert response.body
