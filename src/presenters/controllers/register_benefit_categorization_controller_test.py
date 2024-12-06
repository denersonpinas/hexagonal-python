from faker import Faker

from src.data.test import RegisterBenefitCategorizationSpy
from src.infra.test import BenefitCategorizationRepositorySpy
from src.presenters.controllers import RegisterBenefitCategorizationController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterBenefitCategorizationRoute"""

    register_categorization_use_case = RegisterBenefitCategorizationSpy(
        BenefitCategorizationRepositorySpy()
    )
    register_categorization_route = RegisterBenefitCategorizationController(
        register_categorization_use_case=register_categorization_use_case
    )

    attributer = {
        "value": faker.text(max_nb_chars=64),
        "type_id": faker.text(max_nb_chars=32),
    }

    response = register_categorization_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_categorization_use_case.register_param["value"] == attributer["value"]
    )
    assert (
        register_categorization_use_case.register_param["type_id"]
        == attributer["type_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_categorization_use_case = RegisterBenefitCategorizationSpy(
        BenefitCategorizationRepositorySpy()
    )
    register_categorization_route = RegisterBenefitCategorizationController(
        register_categorization_use_case=register_categorization_use_case
    )

    attributer = {
        "value": faker.boolean(),
        "type_id": faker.boolean(),
    }

    response = register_categorization_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_categorization_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_categorization_use_case = RegisterBenefitCategorizationSpy(
        BenefitCategorizationRepositorySpy()
    )
    register_categorization_route = RegisterBenefitCategorizationController(
        register_categorization_use_case=register_categorization_use_case
    )

    response = register_categorization_route.route(HttpRequest())

    # Testing input
    assert register_categorization_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
