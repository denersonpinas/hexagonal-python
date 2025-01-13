from faker import Faker
from src.infra.test import TypeFileRepositorySpy
from .register import RegisterTypeFile

faker = Faker()


def test_register():
    """Testing register method"""

    type_file_repo = TypeFileRepositorySpy()
    register_abginvest_tpproj_lei = RegisterTypeFile(type_file_repo=type_file_repo)

    attributes = {
        "id": faker.text(max_nb_chars=32),
        "context": faker.text(max_nb_chars=32),
        "dexcription": faker.text(max_nb_chars=120),
        "info": faker.text(max_nb_chars=1000),
    }

    response = register_abginvest_tpproj_lei.register(
        id=attributes["id"],
        context=attributes["context"],
        description=attributes["dexcription"],
        info=attributes["info"],
    )

    # Testing inputs
    assert type_file_repo.insert_type_file_params["contexto"] == attributes["context"]
    assert type_file_repo.insert_type_file_params["info"] == attributes["info"]
    assert (
        type_file_repo.insert_type_file_params["descricao"] == attributes["dexcription"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail_max_char():
    """Testing register method fail"""

    type_file_repo = TypeFileRepositorySpy()
    register_abginvest_tpproj_lei = RegisterTypeFile(type_file_repo=type_file_repo)

    attributes = {
        "id": faker.text(max_nb_chars=320),
        "context": faker.text(max_nb_chars=320),
        "dexcription": faker.text(max_nb_chars=1200),
        "info": faker.text(max_nb_chars=10000),
    }

    response = register_abginvest_tpproj_lei.register(
        id=attributes["id"],
        context=attributes["context"],
        description=attributes["dexcription"],
        info=attributes["info"],
    )

    # Testing inputs
    assert type_file_repo.insert_type_file_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method in fail"""

    type_file_repo = TypeFileRepositorySpy()
    register_abginvest_tpproj_lei = RegisterTypeFile(type_file_repo=type_file_repo)

    attributes = {
        "id": faker.boolean(),
        "context": faker.boolean(),
        "dexcription": faker.boolean(),
        "info": faker.random_number(),
    }

    response = register_abginvest_tpproj_lei.register(
        id=attributes["id"],
        context=attributes["context"],
        description=attributes["dexcription"],
        info=attributes["info"],
    )

    # Testing inputs
    assert type_file_repo.insert_type_file_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
