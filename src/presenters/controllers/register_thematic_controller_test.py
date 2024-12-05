from faker import Faker

from src.data.test import RegisterThematicSpy
from src.infra.test import ThematicRepositorySpy
from src.presenters.controllers import RegisterThematicController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterThematicRoute"""

    register_thematic_use_case = RegisterThematicSpy(ThematicRepositorySpy())
    register_thematic_route = RegisterThematicController(
        register_thematic_use_case=register_thematic_use_case
    )

    attributer = {"description": faker.text(max_nb_chars=50)}

    response = register_thematic_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_thematic_use_case.register_param["description"]
        == attributer["description"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_thematic_use_case = RegisterThematicSpy(ThematicRepositorySpy())
    register_thematic_route = RegisterThematicController(
        register_thematic_use_case=register_thematic_use_case
    )

    attributer = {"description": faker.random_number()}

    response = register_thematic_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_thematic_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_thematic_use_case = RegisterThematicSpy(ThematicRepositorySpy())
    register_thematic_route = RegisterThematicController(
        register_thematic_use_case=register_thematic_use_case
    )

    response = register_thematic_route.route(HttpRequest())

    # Testing input
    assert register_thematic_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
