from faker import Faker
from src.infra.test import RelationshipCategoryCounterpartsRepositorySpy
from .register import RegisterRelationshipCategoryCounterparts

faker = Faker()


def test_register():
    """Testing register method"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    register_relationship_category_counterparts = RegisterRelationshipCategoryCounterparts(
        relationship_category_counterparts_repo=relationship_category_counterparts_repo
    )

    attributes = {
        "categoria_id": faker.random_number(digits=5),
        "contrapartida_id": faker.random_number(digits=5),
    }

    response = register_relationship_category_counterparts.register(
        categoria_id=attributes["categoria_id"],
        contrapartida_id=attributes["contrapartida_id"],
    )

    # Testing inputs
    assert (
        relationship_category_counterparts_repo.insert_relationship_category_counterparts_params[
            "categoria_id"
        ]
        == attributes["categoria_id"]
    )
    assert (
        relationship_category_counterparts_repo.insert_relationship_category_counterparts_params[
            "contrapartida_id"
        ]
        == attributes["contrapartida_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing register method in fail"""

    relationship_category_counterparts_repo = (
        RelationshipCategoryCounterpartsRepositorySpy()
    )
    register_relationship_category_counterparts = (
        RegisterRelationshipCategoryCounterparts(
            relationship_category_counterparts_repo
        )
    )

    attributes = {
        "categoria_id": faker.word(),
        "contrapartida_id": faker.random_number(digits=5),
    }

    response = register_relationship_category_counterparts.register(
        categoria_id=attributes["categoria_id"],
        contrapartida_id=attributes["contrapartida_id"],
    )

    # Testing inputs
    assert (
        relationship_category_counterparts_repo.insert_relationship_category_counterparts_params
        == {}
    )

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
