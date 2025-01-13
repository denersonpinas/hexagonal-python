from faker import Faker
import uuid
from src.data.test import RegisterProjectHistorySpy
from src.infra.test import ProjectHistoryRepositorySpy
from src.presenters.controllers import RegisterProjectHistoryController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProjectHistory"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": faker.sentence(),
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_history_use_case.register_param["investment_year"]
        == attributes["investment_year"]
    )
    assert (
        register_project_history_use_case.register_param["title"] == attributes["title"]
    )
    assert (
        register_project_history_use_case.register_param["investment_type"]
        == attributes["investment_type"]
    )
    assert (
        register_project_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_year():
    """Testing route with invalid investment_year"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": "invalid_year",
        "title": faker.sentence(),
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_proposal_id():
    """Testing route with invalid proposal_id"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": faker.sentence(),
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": "invalid_uuid",
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": faker.sentence(),
        # Missing investment_type and proposal_id
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    response = register_project_history_route.route(HttpRequest())

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    response = register_project_history_route.route(HttpRequest(body={}))

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_future_year():
    """Testing route with future investment_year"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": 2050,
        "title": faker.sentence(),
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_history_use_case.register_param["investment_year"]
        == attributes["investment_year"]
    )
    assert (
        register_project_history_use_case.register_param["title"] == attributes["title"]
    )
    assert (
        register_project_history_use_case.register_param["investment_type"]
        == attributes["investment_type"]
    )
    assert (
        register_project_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_past_year():
    """Testing route with very old investment_year"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": 1900,
        "title": faker.sentence(),
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_invalid_investment_type():
    """Testing route with invalid investment_type"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": faker.sentence(),
        "investment_type": "INVALID_TYPE",
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_history_use_case.register_param["investment_year"]
        == attributes["investment_year"]
    )
    assert (
        register_project_history_use_case.register_param["title"] == attributes["title"]
    )
    assert (
        register_project_history_use_case.register_param["investment_type"]
        == attributes["investment_type"]
    )
    assert (
        register_project_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_empty_title():
    """Testing route with empty title"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": "",
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_history_use_case.register_param["investment_year"]
        == attributes["investment_year"]
    )
    assert (
        register_project_history_use_case.register_param["title"] == attributes["title"]
    )
    assert (
        register_project_history_use_case.register_param["investment_type"]
        == attributes["investment_type"]
    )
    assert (
        register_project_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in title"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": "Project@#$%Title&*()!",
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_history_use_case.register_param["investment_year"]
        == attributes["investment_year"]
    )
    assert (
        register_project_history_use_case.register_param["title"] == attributes["title"]
    )
    assert (
        register_project_history_use_case.register_param["investment_type"]
        == attributes["investment_type"]
    )
    assert (
        register_project_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_long_title():
    """Testing route with very long title"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": faker.text(max_nb_chars=1000),
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_negative_year():
    """Testing route with negative investment_year"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": -2000,
        "title": faker.sentence(),
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_html_content():
    """Testing route with HTML content in title"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": "<p>HTML Title</p><script>alert('test')</script>",
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_history_use_case.register_param["investment_year"]
        == attributes["investment_year"]
    )
    assert (
        register_project_history_use_case.register_param["title"] == attributes["title"]
    )
    assert (
        register_project_history_use_case.register_param["investment_type"]
        == attributes["investment_type"]
    )
    assert (
        register_project_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_zero_year():
    """Testing route with investment_year equal to zero"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": 0,
        "title": faker.sentence(),
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_whitespace_title():
    """Testing route with whitespace-only title"""

    register_project_history_use_case = RegisterProjectHistorySpy(
        ProjectHistoryRepositorySpy()
    )
    register_project_history_route = RegisterProjectHistoryController(
        register_project_history_use_case=register_project_history_use_case
    )

    attributes = {
        "investment_year": faker.random_int(min=2000, max=2023),
        "title": "    ",
        "investment_type": faker.random_element(elements=("DIRECT", "INDIRECT")),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_history_use_case.register_param["investment_year"]
        == attributes["investment_year"]
    )
    assert (
        register_project_history_use_case.register_param["title"] == attributes["title"]
    )
    assert (
        register_project_history_use_case.register_param["investment_type"]
        == attributes["investment_type"]
    )
    assert (
        register_project_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body
