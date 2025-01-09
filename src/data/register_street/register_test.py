from faker import Faker
from src.infra.test import StreetRepositorySpy
from .register import RegisterStreet

faker = Faker("pt_BR")


def test_register():
    """Testing register method"""

    street_repository = StreetRepositorySpy()
    register_street = RegisterStreet(street_repository)

    attributes = {
        "name": faker.street_name()[:100],
        "neighborhood_id": faker.random_int(min=1),
    }

    response = register_street.register(**attributes)

    # Testing inputs
    assert street_repository.insert_street_params["name"] == attributes["name"]
    assert (
        street_repository.insert_street_params["neighborhood_id"]
        == attributes["neighborhood_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_name_length():
    """Testing register with invalid name length"""

    street_repository = StreetRepositorySpy()
    register_street = RegisterStreet(street_repository)

    attributes = {
        "name": faker.text(max_nb_chars=1500),
        "neighborhood_id": faker.random_int(min=1),
    }

    response = register_street.register(**attributes)

    # Testing inputs
    assert street_repository.insert_street_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_neighborhood_id():
    """Testing register with invalid neighborhood id"""

    street_repository = StreetRepositorySpy()
    register_street = RegisterStreet(street_repository)

    attributes = {"name": faker.street_name()[:100], "neighborhood_id": 0}

    response = register_street.register(**attributes)

    # Testing inputs
    assert street_repository.insert_street_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    street_repository = StreetRepositorySpy()
    register_street = RegisterStreet(street_repository)

    attributes = {"name": faker.random_number(), "neighborhood_id": faker.name()}

    response = register_street.register(**attributes)

    # Testing inputs
    assert street_repository.insert_street_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
