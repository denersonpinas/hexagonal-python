from faker import Faker
from src.infra.test import NeighborhoodRepositorySpy
from .register import RegisterNeighborhood

faker = Faker("pt_BR")


def test_register():
    """Testing register method"""

    neighborhood_repository = NeighborhoodRepositorySpy()
    register_neighborhood = RegisterNeighborhood(neighborhood_repository)

    attributes = {"name": faker.city_suffix()[:100], "city_id": faker.random_int(min=1)}

    response = register_neighborhood.register(**attributes)

    # Testing inputs
    assert (
        neighborhood_repository.insert_neighborhood_params["name"] == attributes["name"]
    )
    assert (
        neighborhood_repository.insert_neighborhood_params["city_id"]
        == attributes["city_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_name_length():
    """Testing register with invalid name length"""

    neighborhood_repository = NeighborhoodRepositorySpy()
    register_neighborhood = RegisterNeighborhood(neighborhood_repository)

    attributes = {
        "name": faker.text(max_nb_chars=1500),
        "city_id": faker.random_int(min=1),
    }

    response = register_neighborhood.register(**attributes)

    # Testing inputs
    assert neighborhood_repository.insert_neighborhood_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_city_id():
    """Testing register with invalid city id"""

    neighborhood_repository = NeighborhoodRepositorySpy()
    register_neighborhood = RegisterNeighborhood(neighborhood_repository)

    attributes = {"name": faker.city_suffix()[:100], "city_id": 0}

    response = register_neighborhood.register(**attributes)

    # Testing inputs
    assert neighborhood_repository.insert_neighborhood_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    neighborhood_repository = NeighborhoodRepositorySpy()
    register_neighborhood = RegisterNeighborhood(neighborhood_repository)

    attributes = {"name": faker.random_number(), "city_id": faker.name()}

    response = register_neighborhood.register(**attributes)

    # Testing inputs
    assert neighborhood_repository.insert_neighborhood_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
