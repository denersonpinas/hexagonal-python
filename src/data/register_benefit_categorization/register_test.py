from faker import Faker
from src.infra.test import BenefitCategorizationRepositorySpy
from .register import RegisterBenefitCategorization

faker = Faker()


def test_register():
    """Testing register method"""

    categorization_repo = BenefitCategorizationRepositorySpy()
    register_categorization = RegisterBenefitCategorization(
        categorization_repo=categorization_repo
    )

    attributes = {
        "value": faker.text(max_nb_chars=64),
        "type_id": faker.text(max_nb_chars=32),
    }

    response = register_categorization.register(
        value=attributes["value"], type_id=attributes["type_id"]
    )

    # Testing inputs
    assert (
        categorization_repo.insert_categorization_params["valor"] == attributes["value"]
    )
    assert (
        categorization_repo.insert_categorization_params["tipo_id"]
        == attributes["type_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing register method in fail"""

    categorization_repo = BenefitCategorizationRepositorySpy()
    register_categorization = RegisterBenefitCategorization(
        categorization_repo=categorization_repo
    )

    attributes = {"value": faker.boolean(), "type_id": faker.random_number()}

    response = register_categorization.register(
        value=attributes["value"], type_id=attributes["type_id"]
    )

    # Testing inputs
    assert categorization_repo.insert_categorization_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
