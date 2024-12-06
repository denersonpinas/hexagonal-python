from faker import Faker

from src.data.test import RegisterBenefitCategorizationTypeSpy
from src.infra.test import BenefitCategorizationTypeRepositorySpy
from src.presenters.controllers import RegisterBenefitCategorizationTypeController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterBenefitCategorizationTypeRoute"""

    register_categorization_type_use_case = RegisterBenefitCategorizationTypeSpy(
        BenefitCategorizationTypeRepositorySpy()
    )
    register_categorization_type_route = RegisterBenefitCategorizationTypeController(
        register_categorization_type_use_case=register_categorization_type_use_case
    )

    attributer = {
        "description": faker.text(max_nb_chars=50),
        "info": faker.text(max_nb_chars=150),
    }

    response = register_categorization_type_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_categorization_type_use_case.register_param["description"]
        == attributer["description"]
    )
    assert (
        register_categorization_type_use_case.register_param["info"]
        == attributer["info"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_categorization_type_use_case = RegisterBenefitCategorizationTypeSpy(
        BenefitCategorizationTypeRepositorySpy()
    )
    register_categorization_type_route = RegisterBenefitCategorizationTypeController(
        register_categorization_type_use_case=register_categorization_type_use_case
    )

    attributer = {
        "description": faker.boolean(),
        "info": faker.boolean(),
    }

    response = register_categorization_type_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_categorization_type_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_categorization_type_use_case = RegisterBenefitCategorizationTypeSpy(
        BenefitCategorizationTypeRepositorySpy()
    )
    register_categorization_type_route = RegisterBenefitCategorizationTypeController(
        register_categorization_type_use_case=register_categorization_type_use_case
    )

    response = register_categorization_type_route.route(HttpRequest())

    # Testing input
    assert register_categorization_type_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
