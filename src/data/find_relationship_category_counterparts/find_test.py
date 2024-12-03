from faker import Faker

from .find import FindRelationshipCategoryCounterparts
from src.infra.test import RelationshipCategoryCounterpartsRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    find_category_counterpart = FindRelationshipCategoryCounterparts(
        relationship_category_counterparts_repo=relationship_category_counterparts_repo
    )

    attributes = {"id": faker.random_number(digits=5)}
    response = find_category_counterpart.by_id(id=attributes["id"])

    # Testing inputs
    assert (
        relationship_category_counterparts_repo.select_relationship_category_counterparts_params[
            "id"
        ]
        == attributes["id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method fail"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    find_category_counterpart = FindRelationshipCategoryCounterparts(
        relationship_category_counterparts_repo=relationship_category_counterparts_repo
    )

    attributes = {"id": faker.word()}
    response = find_category_counterpart.by_id(id=attributes["id"])

    # Testing inputs
    assert (
        relationship_category_counterparts_repo.select_relationship_category_counterparts_params
        == {}
    )

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_category():
    """Testing by_category method"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    find_category_counterpart = FindRelationshipCategoryCounterparts(
        relationship_category_counterparts_repo=relationship_category_counterparts_repo
    )

    attributes = {"category_id": faker.random_number(digits=2)}
    response = find_category_counterpart.by_category(
        category_id=attributes["category_id"]
    )

    # Testing inputs
    assert (
        relationship_category_counterparts_repo.select_relationship_category_counterparts_params[
            "categoria_id"
        ]
        == attributes["category_id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_category_fail():
    """Testing by_category method fail"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    find_category_counterpart = FindRelationshipCategoryCounterparts(
        relationship_category_counterparts_repo=relationship_category_counterparts_repo
    )

    attributes = {"category_id": faker.word()}
    response = find_category_counterpart.by_category(
        category_id=attributes["category_id"]
    )

    # Testing inputs
    assert (
        relationship_category_counterparts_repo.select_relationship_category_counterparts_params
        == {}
    )

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_counterpart():
    """Testing by_counterpart method"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    find_category_counterpart = FindRelationshipCategoryCounterparts(
        relationship_category_counterparts_repo=relationship_category_counterparts_repo
    )

    attributes = {"counterpart_id": faker.random_number(digits=2)}
    response = find_category_counterpart.by_counterpart(
        counterpart_id=attributes["counterpart_id"]
    )

    # Testing inputs
    assert (
        relationship_category_counterparts_repo.select_relationship_category_counterparts_params[
            "contrapartida_id"
        ]
        == attributes["counterpart_id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_counterpart_fail():
    """Testing by_counterpart method fail"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    find_category_counterpart = FindRelationshipCategoryCounterparts(
        relationship_category_counterparts_repo=relationship_category_counterparts_repo
    )

    attributes = {"counterpart_id": faker.word()}
    response = find_category_counterpart.by_counterpart(
        counterpart_id=attributes["counterpart_id"]
    )

    # Testing inputs
    assert (
        relationship_category_counterparts_repo.select_relationship_category_counterparts_params
        == {}
    )

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_all():
    """Testing by_default method"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    find_category_counterpart = FindRelationshipCategoryCounterparts(
        relationship_category_counterparts_repo=relationship_category_counterparts_repo
    )

    response = find_category_counterpart.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
