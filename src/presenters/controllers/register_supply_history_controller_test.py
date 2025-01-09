from faker import Faker
from src.data.test import RegisterSupplyHistorySpy
from src.infra.test import SupplyHistoryRepositorySpy
from src.presenters.controllers import RegisterSupplyHistoryController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterSupplyHistory"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {
        "service_provided": faker.text(max_nb_chars=200),
        "hiring_manager": faker.name(),
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_supply_history_use_case.register_param["service_provided"]
        == attributes["service_provided"]
    )
    assert (
        register_supply_history_use_case.register_param["hiring_manager"]
        == attributes["hiring_manager"]
    )
    assert (
        register_supply_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {
        "service_provided": faker.text(),
        # Missing hiring_manager and proposal_id
    }

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_supply_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    response = register_supply_history_route.route(HttpRequest())

    # Testing input
    assert register_supply_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    response = register_supply_history_route.route(HttpRequest(body={}))

    # Testing input
    assert register_supply_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_params():
    """Testing route with empty parameters"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {"service_provided": "", "hiring_manager": "", "proposal_id": ""}

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_supply_history_use_case.register_param["service_provided"]
        == attributes["service_provided"]
    )
    assert (
        register_supply_history_use_case.register_param["hiring_manager"]
        == attributes["hiring_manager"]
    )
    assert (
        register_supply_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in text fields"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {
        "service_provided": "Service@#$%",
        "hiring_manager": "Manager@#$%",
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_supply_history_use_case.register_param["service_provided"]
        == attributes["service_provided"]
    )
    assert (
        register_supply_history_use_case.register_param["hiring_manager"]
        == attributes["hiring_manager"]
    )
    assert (
        register_supply_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_long_text():
    """Testing route with very long text in fields"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {
        "service_provided": faker.text(max_nb_chars=10000),
        "hiring_manager": faker.text(max_nb_chars=5000),
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_supply_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_numeric_values():
    """Testing route with numeric values in text fields"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {
        "service_provided": "12345",
        "hiring_manager": "67890",
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_supply_history_use_case.register_param["service_provided"]
        == attributes["service_provided"]
    )
    assert (
        register_supply_history_use_case.register_param["hiring_manager"]
        == attributes["hiring_manager"]
    )
    assert (
        register_supply_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_whitespace_only():
    """Testing route with whitespace-only values"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {
        "service_provided": "    ",
        "hiring_manager": "    ",
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_supply_history_use_case.register_param["service_provided"]
        == attributes["service_provided"]
    )
    assert (
        register_supply_history_use_case.register_param["hiring_manager"]
        == attributes["hiring_manager"]
    )
    assert (
        register_supply_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_invalid_proposal_id():
    """Testing route with invalid proposal_id"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {
        "service_provided": faker.text(),
        "hiring_manager": faker.name(),
        "proposal_id": -1,
    }

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_supply_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_html_content():
    """Testing route with HTML content in text fields"""

    register_supply_history_use_case = RegisterSupplyHistorySpy(
        SupplyHistoryRepositorySpy()
    )
    register_supply_history_route = RegisterSupplyHistoryController(
        register_supply_history_use_case=register_supply_history_use_case
    )

    attributes = {
        "service_provided": "<p>Test HTML content</p>",
        "hiring_manager": "<strong>Manager Name</strong>",
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_supply_history_use_case.register_param["service_provided"]
        == attributes["service_provided"]
    )
    assert (
        register_supply_history_use_case.register_param["hiring_manager"]
        == attributes["hiring_manager"]
    )
    assert (
        register_supply_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body
