from faker import Faker
from src.infra.test import LawRepositorySpy
from .register import RegisterLaw

faker = Faker()


def test_register():
    """Testing registry method"""

    law_repository = LawRepositorySpy()
    register_law = RegisterLaw(law_repository)

    attributes = {
        "name": faker.text(max_nb_chars=100),
        "description": faker.text(max_nb_chars=250),
    }

    response = register_law.registry(
        nome=attributes["name"], descricao=attributes["description"]
    )

    # Testing inputs
    assert law_repository.insert_law_params["descricao"] == attributes["description"]
    assert law_repository.insert_law_params["nome"] == attributes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_max_len_description():
    """Testing registry with long description method"""

    law_repository = LawRepositorySpy()
    register_law = RegisterLaw(law_repository)

    attributes = {
        "name": faker.text(max_nb_chars=1000),
        "description": faker.text(max_nb_chars=2500),
    }

    response = register_law.registry(
        nome=attributes["name"], descricao=attributes["description"]
    )

    # Testing inputs
    assert law_repository.insert_law_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing registry method fail"""

    law_repository = LawRepositorySpy()
    register_law = RegisterLaw(law_repository)

    attributes = {
        "name": faker.boolean(),
        "description": faker.boolean(),
    }

    response = register_law.registry(
        nome=attributes["name"], descricao=attributes["description"]
    )

    # Testing inputs
    assert law_repository.insert_law_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
