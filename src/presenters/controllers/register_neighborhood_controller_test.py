from faker import Faker
from src.data.test import RegisterNeighborhoodSpy
from src.infra.test import NeighborhoodRepositorySpy
from src.presenters.controllers import RegisterNeighborhoodController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterNeighborhood"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    attributes = {
        "name": faker.city_suffix()[:100],
        "city_id": faker.random_int(min=1, max=5000),
    }

    response = register_neighborhood_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_neighborhood_use_case.register_param["name"] == attributes["name"]
    assert (
        register_neighborhood_use_case.register_param["city_id"]
        == attributes["city_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_city_id():
    """Testing route method with invalid city_id"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    attributes = {"name": faker.city_suffix()[:100], "city_id": "invalid_id"}

    response = register_neighborhood_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_neighborhood_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    attributes = {
        "name": faker.city_suffix()[:100]
        # Missing city_id
    }

    response = register_neighborhood_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_neighborhood_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    response = register_neighborhood_route.route(HttpRequest())

    # Testing input
    assert register_neighborhood_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    response = register_neighborhood_route.route(HttpRequest(body={}))

    # Testing input
    assert register_neighborhood_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_zero_city_id():
    """Testing route with city_id equal to zero"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    attributes = {"name": faker.city_suffix()[:100], "city_id": 0}

    response = register_neighborhood_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_neighborhood_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_negative_city_id():
    """Testing route with negative city_id"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    attributes = {"name": faker.city_suffix()[:100], "city_id": -1}

    response = register_neighborhood_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_neighborhood_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_empty_name():
    """Testing route with empty name parameter"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    attributes = {"name": "", "city_id": faker.random_int(min=1, max=5000)}

    response = register_neighborhood_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_neighborhood_use_case.register_param["name"] == attributes["name"]
    assert (
        register_neighborhood_use_case.register_param["city_id"]
        == attributes["city_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in name"""

    register_neighborhood_use_case = RegisterNeighborhoodSpy(
        NeighborhoodRepositorySpy()
    )
    register_neighborhood_route = RegisterNeighborhoodController(
        register_neighborhood_use_case=register_neighborhood_use_case
    )

    attributes = {
        "name": "Neighborhood@#$%",
        "city_id": faker.random_int(min=1, max=5000),
    }

    response = register_neighborhood_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_neighborhood_use_case.register_param["name"] == attributes["name"]
    assert (
        register_neighborhood_use_case.register_param["city_id"]
        == attributes["city_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body
