from faker import Faker
import uuid
from src.data.test import RegisterProposalExecutionLocationSpy
from src.infra.test import ProposalExecutionLocationRepositorySpy
from src.presenters.controllers import RegisterProposalExecutionLocationController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalExecutionLocation"""

    register_use_case = RegisterProposalExecutionLocationSpy(
        ProposalExecutionLocationRepositorySpy()
    )
    register_route = RegisterProposalExecutionLocationController(
        register_proposal_execution_location_use_case=register_use_case
    )

    attributes = {
        "city_id": faker.random_int(min=1, max=5000),
        "proposal_id": uuid.uuid4(),
    }

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param["city_id"] == attributes["city_id"]
    assert register_use_case.register_param["proposal_id"] == attributes["proposal_id"]

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_uuid():
    """Testing route method with invalid UUID"""

    register_use_case = RegisterProposalExecutionLocationSpy(
        ProposalExecutionLocationRepositorySpy()
    )
    register_route = RegisterProposalExecutionLocationController(
        register_proposal_execution_location_use_case=register_use_case
    )

    attributes = {
        "city_id": faker.random_int(min=1, max=5000),
        "proposal_id": "invalid_uuid",
    }

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_city_id():
    """Testing route method with invalid city_id"""

    register_use_case = RegisterProposalExecutionLocationSpy(
        ProposalExecutionLocationRepositorySpy()
    )
    register_route = RegisterProposalExecutionLocationController(
        register_proposal_execution_location_use_case=register_use_case
    )

    attributes = {"city_id": "invalid_id", "proposal_id": str(uuid.uuid4())}

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_use_case = RegisterProposalExecutionLocationSpy(
        ProposalExecutionLocationRepositorySpy()
    )
    register_route = RegisterProposalExecutionLocationController(
        register_proposal_execution_location_use_case=register_use_case
    )

    attributes = {
        "city_id": faker.random_int(min=1, max=5000)
        # Missing proposal_id
    }

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_use_case = RegisterProposalExecutionLocationSpy(
        ProposalExecutionLocationRepositorySpy()
    )
    register_route = RegisterProposalExecutionLocationController(
        register_proposal_execution_location_use_case=register_use_case
    )

    response = register_route.route(HttpRequest())

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_use_case = RegisterProposalExecutionLocationSpy(
        ProposalExecutionLocationRepositorySpy()
    )
    register_route = RegisterProposalExecutionLocationController(
        register_proposal_execution_location_use_case=register_use_case
    )

    response = register_route.route(HttpRequest(body={}))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_zero_city_id():
    """Testing route with city_id equal to zero"""

    register_use_case = RegisterProposalExecutionLocationSpy(
        ProposalExecutionLocationRepositorySpy()
    )
    register_route = RegisterProposalExecutionLocationController(
        register_proposal_execution_location_use_case=register_use_case
    )

    attributes = {"city_id": 0, "proposal_id": str(uuid.uuid4())}

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_negative_city_id():
    """Testing route with negative city_id"""

    register_use_case = RegisterProposalExecutionLocationSpy(
        ProposalExecutionLocationRepositorySpy()
    )
    register_route = RegisterProposalExecutionLocationController(
        register_proposal_execution_location_use_case=register_use_case
    )

    attributes = {"city_id": -1, "proposal_id": str(uuid.uuid4())}

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
