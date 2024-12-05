from faker import Faker

from src.data.test import RegisterCounterpartSpy
from src.infra.test import CounterpartRepositorySpy
from src.presenters.controllers import RegisterCounterpartController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterCounterpartRoute"""

    register_counterpart_use_case = RegisterCounterpartSpy(CounterpartRepositorySpy())
    register_counterpart_route = RegisterCounterpartController(
        register_counterpart_use_case=register_counterpart_use_case
    )

    attributer = {
        "description": faker.word(),
        "example_aplicability": faker.word(),
        "required": faker.boolean(),
    }

    response = register_counterpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_counterpart_use_case.register_param["descricao"]
        == attributer["description"]
    )
    assert (
        register_counterpart_use_case.register_param["exemplo_aplicabilidade"]
        == attributer["example_aplicability"]
    )
    assert (
        register_counterpart_use_case.register_param["obrigatoria"]
        == attributer["required"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_counterpart_use_case = RegisterCounterpartSpy(CounterpartRepositorySpy())
    register_counterpart_route = RegisterCounterpartController(
        register_counterpart_use_case=register_counterpart_use_case
    )

    attributer = {
        "example_aplicability": faker.word(),
        "required": faker.boolean(),
    }

    response = register_counterpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_counterpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_counterpart_use_case = RegisterCounterpartSpy(CounterpartRepositorySpy())
    register_counterpart_route = RegisterCounterpartController(
        register_counterpart_use_case=register_counterpart_use_case
    )

    response = register_counterpart_route.route(HttpRequest())

    # Testing input
    assert register_counterpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
