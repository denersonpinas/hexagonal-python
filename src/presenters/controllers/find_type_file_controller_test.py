from faker import Faker
from src.data.test import FindTypeFileSpy
from src.infra.test import TypeFileRepositorySpy
from src.presenters.helpers import HttpRequest
from src.presenters.controllers import FindTypeFileController

faker = Faker()


def test_route_by_id():
    """Testing Route by id method"""

    find_type_file_use_case = FindTypeFileSpy(TypeFileRepositorySpy())
    find_type_file_controller = FindTypeFileController(
        find_type_file_use_case=find_type_file_use_case
    )
    http_request = HttpRequest(
        query={
            "id": faker.random_number(digits=5),
        }
    )

    response = find_type_file_controller.route(http_request=http_request)

    # Testing Inputs
    assert find_type_file_use_case.by_id_param["id"] == http_request.query["id"]

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_all():
    """Testing Route by id and default method"""

    find_type_file_use_case = FindTypeFileSpy(TypeFileRepositorySpy())
    find_type_file_controller = FindTypeFileController(
        find_type_file_use_case=find_type_file_use_case
    )
    http_request = HttpRequest(query={})

    response = find_type_file_controller.route(http_request=http_request)

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing Route method fail"""

    find_type_file_use_case = FindTypeFileSpy(TypeFileRepositorySpy())
    find_type_file_controller = FindTypeFileController(
        find_type_file_use_case=find_type_file_use_case
    )
    http_request = HttpRequest(query={"other_query": faker.word()})

    response = find_type_file_controller.route(http_request=http_request)

    # Testing Inputs
    assert find_type_file_use_case.by_id_param == {}

    # Testing Output
    assert response.status_code == 422
    assert response.body
