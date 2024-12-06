from faker import Faker
from src.infra.test import BenefitCategorizationTypeRepositorySpy
from .register import RegisterBenefitCategorizationType

faker = Faker()


def test_register():
    """Testing register method"""

    categorization_type_repo = BenefitCategorizationTypeRepositorySpy()
    register_categorization_type = RegisterBenefitCategorizationType(
        categorization_type_repo=categorization_type_repo
    )

    attributes = {
        "description": faker.text(max_nb_chars=50),
        "info": faker.text(max_nb_chars=150),
    }

    response = register_categorization_type.register(
        description=attributes["description"], info=attributes["info"]
    )

    # Testing inputs
    assert (
        categorization_type_repo.insert_categorization_type_params["descricao"]
        == attributes["description"]
    )
    assert (
        categorization_type_repo.insert_categorization_type_params["info"]
        == attributes["info"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing register method in fail"""

    categorization_type_repo = BenefitCategorizationTypeRepositorySpy()
    register_categorization_type = RegisterBenefitCategorizationType(
        categorization_type_repo=categorization_type_repo
    )

    attributes = {"description": faker.boolean(), "info": faker.random_number()}

    response = register_categorization_type.register(
        description=attributes["description"], info=attributes["info"]
    )

    # Testing inputs
    assert categorization_type_repo.insert_categorization_type_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
