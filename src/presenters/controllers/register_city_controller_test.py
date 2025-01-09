from faker import Faker
from src.data.test import RegisterCitySpy
from src.infra.test import CityRepositorySpy
from src.presenters.controllers import RegisterCityController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterCity"""

    register_city_use_case = RegisterCitySpy(CityRepositorySpy())
    register_city_route = RegisterCityController(
        register_city_use_case=register_city_use_case
    )

    attributes = {"name": faker.city(), "state": faker.state_abbr()}

    response = register_city_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_city_use_case.register_param["name"] == attributes["name"]
    assert register_city_use_case.register_param["state"] == attributes["state"]

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_params():
    """Testing route method with invalid parameters"""

    register_city_use_case = RegisterCitySpy(CityRepositorySpy())
    register_city_route = RegisterCityController(
        register_city_use_case=register_city_use_case
    )

    attributes = {"name": faker.random_number(), "state": faker.random_number()}

    response = register_city_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_city_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_city_use_case = RegisterCitySpy(CityRepositorySpy())
    register_city_route = RegisterCityController(
        register_city_use_case=register_city_use_case
    )

    attributes = {
        "name": faker.city()
        # Missing state
    }

    response = register_city_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_city_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_city_use_case = RegisterCitySpy(CityRepositorySpy())
    register_city_route = RegisterCityController(
        register_city_use_case=register_city_use_case
    )

    response = register_city_route.route(HttpRequest())

    # Testing input
    assert register_city_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_city_use_case = RegisterCitySpy(CityRepositorySpy())
    register_city_route = RegisterCityController(
        register_city_use_case=register_city_use_case
    )

    response = register_city_route.route(HttpRequest(body={}))

    # Testing input
    assert register_city_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_params():
    """Testing route with empty parameters"""

    register_city_use_case = RegisterCitySpy(CityRepositorySpy())
    register_city_route = RegisterCityController(
        register_city_use_case=register_city_use_case
    )

    attributes = {"name": "", "state": ""}

    response = register_city_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_city_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_spaces():
    """Testing route with space-only parameters"""

    register_city_use_case = RegisterCitySpy(CityRepositorySpy())
    register_city_route = RegisterCityController(
        register_city_use_case=register_city_use_case
    )

    attributes = {"name": "   ", "state": "   "}

    response = register_city_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_city_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in parameters"""

    register_city_use_case = RegisterCitySpy(CityRepositorySpy())
    register_city_route = RegisterCityController(
        register_city_use_case=register_city_use_case
    )

    attributes = {"name": "City@#$%", "state": "ST@#$%"}

    response = register_city_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_city_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
