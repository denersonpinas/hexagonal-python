from faker import Faker
from src.data.test import RegisterStreetSpy
from src.infra.test import StreetRepositorySpy
from src.presenters.controllers import RegisterStreetController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterStreet"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    attributes = {
        "name": faker.street_name(),
        "neighborhood_id": faker.random_int(min=1, max=5000),
    }

    response = register_street_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_street_use_case.register_param["name"] == attributes["name"]
    assert (
        register_street_use_case.register_param["neighborhood_id"]
        == attributes["neighborhood_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_neighborhood_id():
    """Testing route method with invalid neighborhood_id"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    attributes = {"name": faker.street_name(), "neighborhood_id": "invalid_id"}

    response = register_street_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_street_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    attributes = {
        "name": faker.street_name()
        # Missing neighborhood_id
    }

    response = register_street_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_street_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    response = register_street_route.route(HttpRequest())

    # Testing input
    assert register_street_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    response = register_street_route.route(HttpRequest(body={}))

    # Testing input
    assert register_street_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_zero_neighborhood_id():
    """Testing route with neighborhood_id equal to zero"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    attributes = {"name": faker.street_name(), "neighborhood_id": 0}

    response = register_street_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_street_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_negative_neighborhood_id():
    """Testing route with negative neighborhood_id"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    attributes = {"name": faker.street_name(), "neighborhood_id": -1}

    response = register_street_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_street_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_empty_name():
    """Testing route with empty name parameter"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    attributes = {"name": "", "neighborhood_id": faker.random_int(min=1, max=5000)}

    response = register_street_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_street_use_case.register_param["name"] == attributes["name"]
    assert (
        register_street_use_case.register_param["neighborhood_id"]
        == attributes["neighborhood_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in name"""

    register_street_use_case = RegisterStreetSpy(StreetRepositorySpy())
    register_street_route = RegisterStreetController(
        register_street_use_case=register_street_use_case
    )

    attributes = {
        "name": "Street@#$%",
        "neighborhood_id": faker.random_int(min=1, max=5000),
    }

    response = register_street_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_street_use_case.register_param["name"] == attributes["name"]
    assert (
        register_street_use_case.register_param["neighborhood_id"]
        == attributes["neighborhood_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body
