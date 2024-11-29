from faker import Faker
from src.infra.test import TypeProjectRepositorySpy
from .register import RegisterTypeProject

faker = Faker()


def test_register():
    """Testing registry method"""

    type_project_repo = TypeProjectRepositorySpy()
    register_type_project = RegisterTypeProject(type_project_repo)

    attributes = {
        "name": faker.text(max_nb_chars=100),
        "description": faker.text(max_nb_chars=250),
    }

    response = register_type_project.registry(
        nome=attributes["name"], descricao=attributes["description"]
    )

    # Testing inputs
    assert (
        type_project_repo.insert_type_project_params["descricao"]
        == attributes["description"]
    )
    assert type_project_repo.insert_type_project_params["nome"] == attributes["name"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_max_len_description():
    """Testing registry with long description method"""

    type_project_repo = TypeProjectRepositorySpy()
    register_type_project = RegisterTypeProject(type_project_repo)

    attributes = {
        "name": faker.text(max_nb_chars=1000),
        "description": faker.text(max_nb_chars=2500),
    }

    response = register_type_project.registry(
        nome=attributes["name"], descricao=attributes["description"]
    )

    # Testing inputs
    assert type_project_repo.insert_type_project_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing registry method fail"""

    type_project_repo = TypeProjectRepositorySpy()
    register_type_project = RegisterTypeProject(type_project_repo)

    attributes = {
        "name": faker.boolean(),
        "description": faker.boolean(),
    }

    response = register_type_project.registry(
        nome=attributes["name"], descricao=attributes["description"]
    )

    # Testing inputs
    assert type_project_repo.insert_type_project_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
