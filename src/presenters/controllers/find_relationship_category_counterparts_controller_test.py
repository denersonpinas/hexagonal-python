from faker import Faker
from src.data.test import FindRelationshipCategoryCounterpartsSpy
from src.infra.test import RelationshipCategoryCounterpartsRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_relationship_category_counterparts_controller import (
    FindRelationshipCategoryCounterpartsController,
)

faker = Faker()


def test_route_by_id():
    """Testing Route by id method"""

    find_relationship_category_counterparts_use_case = (
        FindRelationshipCategoryCounterpartsSpy(
            RelationshipCategoryCounterpartsRepositorySpy()
        )
    )
    find_relationship_category_counterpart_controller = FindRelationshipCategoryCounterpartsController(
        find_relationship_category_counterparts_use_case=find_relationship_category_counterparts_use_case
    )
    http_request = HttpRequest(
        query={
            "id": faker.random_number(digits=5),
        }
    )

    response = find_relationship_category_counterpart_controller.route(
        http_request=http_request
    )

    # Testing Inputs
    assert (
        find_relationship_category_counterparts_use_case.by_id_param["id"]
        == http_request.query["id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_by_category():
    """Testing Route by id category method"""

    find_relationship_category_counterparts_use_case = (
        FindRelationshipCategoryCounterpartsSpy(
            RelationshipCategoryCounterpartsRepositorySpy()
        )
    )
    find_relationship_category_counterpart_controller = FindRelationshipCategoryCounterpartsController(
        find_relationship_category_counterparts_use_case=find_relationship_category_counterparts_use_case
    )
    http_request = HttpRequest(
        query={
            "category_id": faker.random_number(digits=5),
        }
    )

    response = find_relationship_category_counterpart_controller.route(
        http_request=http_request
    )

    # Testing Inputs
    assert (
        find_relationship_category_counterparts_use_case.by_category_param[
            "category_id"
        ]
        == http_request.query["category_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_by_counterpart():
    """Testing Route by id counterpart method"""

    find_relationship_category_counterparts_use_case = (
        FindRelationshipCategoryCounterpartsSpy(
            RelationshipCategoryCounterpartsRepositorySpy()
        )
    )
    find_relationship_category_counterpart_controller = FindRelationshipCategoryCounterpartsController(
        find_relationship_category_counterparts_use_case=find_relationship_category_counterparts_use_case
    )
    http_request = HttpRequest(
        query={
            "counterpart_id": faker.random_number(digits=5),
        }
    )

    response = find_relationship_category_counterpart_controller.route(
        http_request=http_request
    )

    # Testing Inputs
    assert (
        find_relationship_category_counterparts_use_case.by_counterpart_param[
            "counterpart_id"
        ]
        == http_request.query["counterpart_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_all():
    """Testing Route by id and default method"""

    find_relationship_category_counterparts_use_case = (
        FindRelationshipCategoryCounterpartsSpy(
            RelationshipCategoryCounterpartsRepositorySpy()
        )
    )
    find_relationship_category_counterpart_controller = FindRelationshipCategoryCounterpartsController(
        find_relationship_category_counterparts_use_case=find_relationship_category_counterparts_use_case
    )
    http_request = HttpRequest(query={})

    response = find_relationship_category_counterpart_controller.route(
        http_request=http_request
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing Route method fail"""

    find_relationship_category_counterparts_use_case = (
        FindRelationshipCategoryCounterpartsSpy(
            RelationshipCategoryCounterpartsRepositorySpy()
        )
    )
    find_relationship_category_counterpart_controller = FindRelationshipCategoryCounterpartsController(
        find_relationship_category_counterparts_use_case=find_relationship_category_counterparts_use_case
    )
    http_request = HttpRequest(query={"other_query": faker.word()})

    response = find_relationship_category_counterpart_controller.route(
        http_request=http_request
    )

    # Testing Inputs
    assert find_relationship_category_counterparts_use_case.by_id_param == {}
    assert find_relationship_category_counterparts_use_case.by_category_param == {}
    assert find_relationship_category_counterparts_use_case.by_counterpart_param == {}

    # Testing Output
    assert response.status_code == 422
    assert response.body
