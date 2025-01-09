from faker import Faker
import uuid
from src.data.test import RegisterProposalCounterpartSpy
from src.infra.test import ProposalCounterpartRepositorySpy
from src.presenters.controllers import RegisterProposalCounterpartController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalCounterpart"""

    register_proposal_counterpart_use_case = RegisterProposalCounterpartSpy(
        ProposalCounterpartRepositorySpy()
    )
    register_proposal_counterpart_route = RegisterProposalCounterpartController(
        register_proposal_counterpart_use_case=register_proposal_counterpart_use_case
    )

    attributes = {
        "description": faker.text(),
        "quantity": faker.random_int(min=1, max=100),
        "investment_type_law_counterpart_id": faker.random_int(min=1, max=100),
        "proposal_investment_type_law_id": str(uuid.uuid4()),
        "expected": faker.random_int(min=1, max=100),
    }

    response = register_proposal_counterpart_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_counterpart_use_case.register_param["description"]
        == attributes["description"]
    )
    assert (
        register_proposal_counterpart_use_case.register_param["quantity"]
        == attributes["quantity"]
    )
    assert (
        register_proposal_counterpart_use_case.register_param[
            "investment_type_law_counterpart_id"
        ]
        == attributes["investment_type_law_counterpart_id"]
    )
    assert register_proposal_counterpart_use_case.register_param[
        "proposal_investment_type_law_id"
    ] == uuid.UUID(attributes["proposal_investment_type_law_id"])
    assert (
        register_proposal_counterpart_use_case.register_param["expected"]
        == attributes["expected"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_without_expected():
    """Testing route without optional expected parameter"""

    register_proposal_counterpart_use_case = RegisterProposalCounterpartSpy(
        ProposalCounterpartRepositorySpy()
    )
    register_proposal_counterpart_route = RegisterProposalCounterpartController(
        register_proposal_counterpart_use_case=register_proposal_counterpart_use_case
    )

    attributes = {
        "description": faker.text(),
        "quantity": faker.random_int(min=1, max=100),
        "investment_type_law_counterpart_id": faker.random_int(min=1, max=100),
        "proposal_investment_type_law_id": str(uuid.uuid4()),
    }

    response = register_proposal_counterpart_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_counterpart_use_case.register_param["description"]
        == attributes["description"]
    )
    assert (
        register_proposal_counterpart_use_case.register_param["quantity"]
        == attributes["quantity"]
    )
    assert (
        register_proposal_counterpart_use_case.register_param[
            "investment_type_law_counterpart_id"
        ]
        == attributes["investment_type_law_counterpart_id"]
    )
    assert register_proposal_counterpart_use_case.register_param[
        "proposal_investment_type_law_id"
    ] == uuid.UUID(attributes["proposal_investment_type_law_id"])
    assert register_proposal_counterpart_use_case.register_param["expected"] is None

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_numbers():
    """Testing route with invalid numeric values"""

    register_proposal_counterpart_use_case = RegisterProposalCounterpartSpy(
        ProposalCounterpartRepositorySpy()
    )
    register_proposal_counterpart_route = RegisterProposalCounterpartController(
        register_proposal_counterpart_use_case=register_proposal_counterpart_use_case
    )

    attributes = {
        "description": faker.text(),
        "quantity": "invalid_number",
        "investment_type_law_counterpart_id": "invalid_number",
        "proposal_investment_type_law_id": str(uuid.uuid4()),
        "expected": "invalid_number",
    }

    response = register_proposal_counterpart_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_counterpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_uuid():
    """Testing route with invalid UUID"""

    register_proposal_counterpart_use_case = RegisterProposalCounterpartSpy(
        ProposalCounterpartRepositorySpy()
    )
    register_proposal_counterpart_route = RegisterProposalCounterpartController(
        register_proposal_counterpart_use_case=register_proposal_counterpart_use_case
    )

    attributes = {
        "description": faker.text(),
        "quantity": faker.random_int(min=1, max=100),
        "investment_type_law_counterpart_id": faker.random_int(min=1, max=100),
        "proposal_investment_type_law_id": "invalid_uuid",
        "expected": faker.random_int(min=1, max=100),
    }

    response = register_proposal_counterpart_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_counterpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_proposal_counterpart_use_case = RegisterProposalCounterpartSpy(
        ProposalCounterpartRepositorySpy()
    )
    register_proposal_counterpart_route = RegisterProposalCounterpartController(
        register_proposal_counterpart_use_case=register_proposal_counterpart_use_case
    )

    attributes = {
        "description": faker.text(),
        "quantity": faker.random_int(min=1, max=100),
        # Missing other required parameters
    }

    response = register_proposal_counterpart_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_counterpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_counterpart_use_case = RegisterProposalCounterpartSpy(
        ProposalCounterpartRepositorySpy()
    )
    register_proposal_counterpart_route = RegisterProposalCounterpartController(
        register_proposal_counterpart_use_case=register_proposal_counterpart_use_case
    )

    response = register_proposal_counterpart_route.route(HttpRequest())

    # Testing input
    assert register_proposal_counterpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
