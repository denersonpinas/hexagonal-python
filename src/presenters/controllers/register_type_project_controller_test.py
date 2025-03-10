from faker import Faker

from src.data.test import RegisterTypeProjectSpy
from src.infra.test import TypeProjectRepositorySpy
from src.presenters.controllers import RegisterTypeProjectController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterLaw"""

    register_type_project_use_case = RegisterTypeProjectSpy(TypeProjectRepositorySpy())
    register_law_route = RegisterTypeProjectController(
        register_type_project_use_case=register_type_project_use_case
    )

    attributer = {
        "name": faker.text(max_nb_chars=100),
        "description": faker.text(max_nb_chars=250),
    }

    response = register_law_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_type_project_use_case.register_param["descricao"]
        == attributer["description"]
    )
    assert register_type_project_use_case.register_param["nome"] == attributer["name"]

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_type_project_use_case = RegisterTypeProjectSpy(TypeProjectRepositorySpy())
    register_law_route = RegisterTypeProjectController(
        register_type_project_use_case=register_type_project_use_case
    )

    attributer = {
        "name": faker.boolean(),
        "description": faker.boolean(),
    }

    response = register_law_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_type_project_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_type_project_use_case = RegisterTypeProjectSpy(TypeProjectRepositorySpy())
    register_law_route = RegisterTypeProjectController(
        register_type_project_use_case=register_type_project_use_case
    )

    response = register_law_route.route(HttpRequest())

    # Testing input
    assert register_type_project_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
