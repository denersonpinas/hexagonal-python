from faker import Faker
from src.infra.test import CityRepositorySpy
from .register import RegisterCity

faker = Faker("pt_BR")


def get_random_state():
    """Helper para gerar sigla de estado aleatória"""
    estados = [
        "AC",
        "AL",
        "AP",
        "AM",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MT",
        "MS",
        "MG",
        "PA",
        "PB",
        "PR",
        "PE",
        "PI",
        "RJ",
        "RN",
        "RS",
        "RO",
        "RR",
        "SC",
        "SP",
        "SE",
        "TO",
    ]
    return faker.random_element(elements=estados)


def test_register():
    """Testing register method"""

    city_repository = CityRepositorySpy()
    register_city = RegisterCity(city_repository)

    attributes = {"name": faker.city()[:100], "state": get_random_state()}

    response = register_city.register(**attributes)

    # Testing inputs
    assert city_repository.insert_city_params["name"] == attributes["name"]
    assert city_repository.insert_city_params["state"] == attributes["state"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_name_length():
    """Testing register with invalid name length"""

    city_repository = CityRepositorySpy()
    register_city = RegisterCity(city_repository)

    attributes = {"name": faker.text(max_nb_chars=1500), "state": get_random_state()}

    response = register_city.register(**attributes)

    # Testing inputs
    assert city_repository.insert_city_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_state_length():
    """Testing register with invalid state length"""

    city_repository = CityRepositorySpy()
    register_city = RegisterCity(city_repository)

    attributes = {"name": faker.city()[:100], "state": faker.estado()}

    response = register_city.register(**attributes)

    # Testing inputs
    assert city_repository.insert_city_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    city_repository = CityRepositorySpy()
    register_city = RegisterCity(city_repository)

    attributes = {"name": faker.random_number(), "state": faker.random_number()}

    response = register_city.register(**attributes)

    # Testing inputs
    assert city_repository.insert_city_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
