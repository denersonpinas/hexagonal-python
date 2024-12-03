from faker import Faker

from src.data.test import RegisterRelationshipCategoryCounterpartsSpy
from src.infra.test import RelationshipCategoryCounterpartsRepositorySpy
from src.presenters.controllers import (
    RegisterRelationshipCategoryCounterpartsController,
)
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterRelationshipCategoryCounterpartsRoute"""

    register_relationship_category_counterparts_use_case = (
        RegisterRelationshipCategoryCounterpartsSpy(
            RelationshipCategoryCounterpartsRepositorySpy()
        )
    )
    register_counterpart_route = RegisterRelationshipCategoryCounterpartsController(
        register_relationship_category_counterparts_use_case=register_relationship_category_counterparts_use_case
    )

    attributer = {
        "category_id": faker.random_number(digits=5),
        "counterpart_id": faker.random_number(digits=5),
    }

    response = register_counterpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_relationship_category_counterparts_use_case.registry_param[
            "categoria_id"
        ]
        == attributer["category_id"]
    )
    assert (
        register_relationship_category_counterparts_use_case.registry_param[
            "contrapartida_id"
        ]
        == attributer["counterpart_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_relationship_category_counterparts_use_case = (
        RegisterRelationshipCategoryCounterpartsSpy(
            RelationshipCategoryCounterpartsRepositorySpy()
        )
    )
    register_counterpart_route = RegisterRelationshipCategoryCounterpartsController(
        register_relationship_category_counterparts_use_case=register_relationship_category_counterparts_use_case
    )

    attributer = {
        "category_id": faker.word(),
        "counterpart_id": faker.random_number(digits=5),
    }

    response = register_counterpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_relationship_category_counterparts_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_relationship_category_counterparts_use_case = (
        RegisterRelationshipCategoryCounterpartsSpy(
            RelationshipCategoryCounterpartsRepositorySpy()
        )
    )
    register_counterpart_route = RegisterRelationshipCategoryCounterpartsController(
        register_relationship_category_counterparts_use_case=register_relationship_category_counterparts_use_case
    )

    response = register_counterpart_route.route(HttpRequest())

    # Testing input
    assert register_relationship_category_counterparts_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
