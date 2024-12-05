from faker import Faker

from src.data.test import RegisterCategoryCounterpartSpy
from src.infra.test import CategoryCounterpartRepositorySpy
from src.presenters.controllers import RegisterCategoryCounterpartController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterCategoryCounterpartRoute"""

    register_category_counterpart_use_case = RegisterCategoryCounterpartSpy(
        CategoryCounterpartRepositorySpy()
    )
    register_counterpart_route = RegisterCategoryCounterpartController(
        register_category_counterpart_use_case=register_category_counterpart_use_case
    )

    attributer = {
        "name": faker.text(max_nb_chars=120),
        "description": faker.text(max_nb_chars=500),
        "subcategory_id": faker.random_number(digits=5),
    }

    response = register_counterpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_category_counterpart_use_case.register_param["descricao"]
        == attributer["description"]
    )
    assert (
        register_category_counterpart_use_case.register_param["nome"]
        == attributer["name"]
    )
    assert (
        register_category_counterpart_use_case.register_param["subcategoria_id"]
        == attributer["subcategory_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_category_counterpart_use_case = RegisterCategoryCounterpartSpy(
        CategoryCounterpartRepositorySpy()
    )
    register_counterpart_route = RegisterCategoryCounterpartController(
        register_category_counterpart_use_case=register_category_counterpart_use_case
    )

    attributer = {
        "name": faker.random_number(digits=5),
        "description": faker.random_number(digits=5),
        "subcategory_id": faker.random_number(digits=5),
    }

    response = register_counterpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_category_counterpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_category_counterpart_use_case = RegisterCategoryCounterpartSpy(
        CategoryCounterpartRepositorySpy()
    )
    register_counterpart_route = RegisterCategoryCounterpartController(
        register_category_counterpart_use_case=register_category_counterpart_use_case
    )

    response = register_counterpart_route.route(HttpRequest())

    # Testing input
    assert register_category_counterpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
