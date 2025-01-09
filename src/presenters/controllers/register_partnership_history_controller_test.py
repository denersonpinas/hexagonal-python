from faker import Faker
from src.data.test import RegisterPartnershipHistorySpy
from src.infra.test import PartnershipHistoryRepositorySpy
from src.presenters.controllers import RegisterPartnershipHistoryController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterPartnershipHistory"""

    register_partnership_history_use_case = RegisterPartnershipHistorySpy(
        PartnershipHistoryRepositorySpy()
    )
    register_partnership_history_route = RegisterPartnershipHistoryController(
        register_partnership_history_use_case=register_partnership_history_use_case
    )

    attributes = {
        "sponsors_number": faker.random_int(min=1, max=100),
        "renewal_number": faker.random_int(min=0, max=10),
        "proposal_id": faker.uuid4(),
        "additional_info": faker.text(),
    }

    response = register_partnership_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_partnership_history_use_case.register_param["sponsors_number"]
        == attributes["sponsors_number"]
    )
    assert (
        register_partnership_history_use_case.register_param["renewal_number"]
        == attributes["renewal_number"]
    )
    assert (
        register_partnership_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_partnership_history_use_case.register_param["additional_info"]
        == attributes["additional_info"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_without_additional_info():
    """Testing route without optional additional_info"""

    register_partnership_history_use_case = RegisterPartnershipHistorySpy(
        PartnershipHistoryRepositorySpy()
    )
    register_partnership_history_route = RegisterPartnershipHistoryController(
        register_partnership_history_use_case=register_partnership_history_use_case
    )

    attributes = {
        "sponsors_number": faker.random_int(min=1, max=100),
        "renewal_number": faker.random_int(min=0, max=10),
        "proposal_id": faker.uuid4(),
    }

    response = register_partnership_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_partnership_history_use_case.register_param["sponsors_number"]
        == attributes["sponsors_number"]
    )
    assert (
        register_partnership_history_use_case.register_param["renewal_number"]
        == attributes["renewal_number"]
    )
    assert (
        register_partnership_history_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_partnership_history_use_case.register_param["additional_info"] is None
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_numbers():
    """Testing route with invalid numbers"""

    register_partnership_history_use_case = RegisterPartnershipHistorySpy(
        PartnershipHistoryRepositorySpy()
    )
    register_partnership_history_route = RegisterPartnershipHistoryController(
        register_partnership_history_use_case=register_partnership_history_use_case
    )

    attributes = {
        "sponsors_number": "invalid_number",
        "renewal_number": "invalid_number",
        "proposal_id": faker.uuid4(),
    }

    response = register_partnership_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_partnership_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_negative_numbers():
    """Testing route with negative numbers"""

    register_partnership_history_use_case = RegisterPartnershipHistorySpy(
        PartnershipHistoryRepositorySpy()
    )
    register_partnership_history_route = RegisterPartnershipHistoryController(
        register_partnership_history_use_case=register_partnership_history_use_case
    )

    attributes = {
        "sponsors_number": -5,
        "renewal_number": -3,
        "proposal_id": faker.uuid4(),
    }

    response = register_partnership_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_partnership_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_partnership_history_use_case = RegisterPartnershipHistorySpy(
        PartnershipHistoryRepositorySpy()
    )
    register_partnership_history_route = RegisterPartnershipHistoryController(
        register_partnership_history_use_case=register_partnership_history_use_case
    )

    attributes = {
        "sponsors_number": faker.random_int(min=1, max=100),
        # Missing renewal_number and proposal_id
        "additional_info": faker.text(),
    }

    response = register_partnership_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_partnership_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_partnership_history_use_case = RegisterPartnershipHistorySpy(
        PartnershipHistoryRepositorySpy()
    )
    register_partnership_history_route = RegisterPartnershipHistoryController(
        register_partnership_history_use_case=register_partnership_history_use_case
    )

    response = register_partnership_history_route.route(HttpRequest())

    # Testing input
    assert register_partnership_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_partnership_history_use_case = RegisterPartnershipHistorySpy(
        PartnershipHistoryRepositorySpy()
    )
    register_partnership_history_route = RegisterPartnershipHistoryController(
        register_partnership_history_use_case=register_partnership_history_use_case
    )

    response = register_partnership_history_route.route(HttpRequest(body={}))

    # Testing input
    assert register_partnership_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
