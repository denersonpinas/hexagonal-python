from faker import Faker

from src.data.test import RegisterTypeFileSpy
from src.infra.test import TypeFileRepositorySpy
from src.presenters.controllers import RegisterTypeFileController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterAbginvestTpprojLeiRoute"""

    register_type_file_use_case = RegisterTypeFileSpy(TypeFileRepositorySpy())
    register_type_file_route = RegisterTypeFileController(
        register_type_file_use_case=register_type_file_use_case
    )

    attributer = {
        "context": faker.text(max_nb_chars=32),
        "description": faker.text(max_nb_chars=120),
        "info": faker.text(max_nb_chars=1000),
    }

    response = register_type_file_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_type_file_use_case.register_param["context"] == attributer["context"]
    )
    assert (
        register_type_file_use_case.register_param["description"]
        == attributer["description"]
    )
    assert register_type_file_use_case.register_param["info"] == attributer["info"]

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_type_file_use_case = RegisterTypeFileSpy(TypeFileRepositorySpy())
    register_type_file_route = RegisterTypeFileController(
        register_type_file_use_case=register_type_file_use_case
    )

    attributer = {
        "context": faker.random_number(),
        "description": faker.random_number(),
        "info": faker.random_number(),
    }

    response = register_type_file_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_type_file_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_type_file_use_case = RegisterTypeFileSpy(TypeFileRepositorySpy())
    register_type_file_route = RegisterTypeFileController(
        register_type_file_use_case=register_type_file_use_case
    )

    response = register_type_file_route.route(HttpRequest())

    # Testing input
    assert register_type_file_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
