from faker import Faker
import uuid
from src.data.test import RegisterProposalInvestmentTypeLawSpy
from src.infra.test import ProposalInvestmentTypeLawRepositorySpy
from src.presenters.controllers import RegisterProposalInvestmentTypeLawController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalInvestmentTypeLaw"""

    register_proposal_investment_type_law_use_case = (
        RegisterProposalInvestmentTypeLawSpy(ProposalInvestmentTypeLawRepositorySpy())
    )
    register_proposal_investment_type_law_route = RegisterProposalInvestmentTypeLawController(
        register_proposal_investment_type_law_use_case=register_proposal_investment_type_law_use_case
    )

    attributes = {
        "investment_type_law_id": faker.random_int(min=1, max=100),
        "proposal_id": uuid.uuid4(),
    }

    response = register_proposal_investment_type_law_route.route(
        HttpRequest(body=attributes)
    )

    # Testing input
    assert (
        register_proposal_investment_type_law_use_case.register_param[
            "investment_type_law_id"
        ]
        == attributes["investment_type_law_id"]
    )
    assert (
        register_proposal_investment_type_law_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_investment_type_law_id():
    """Testing route with invalid investment_type_law_id"""

    register_proposal_investment_type_law_use_case = (
        RegisterProposalInvestmentTypeLawSpy(ProposalInvestmentTypeLawRepositorySpy())
    )
    register_proposal_investment_type_law_route = RegisterProposalInvestmentTypeLawController(
        register_proposal_investment_type_law_use_case=register_proposal_investment_type_law_use_case
    )

    attributes = {
        "investment_type_law_id": "invalid_id",
        "proposal_id": str(uuid.uuid4()),
    }

    response = register_proposal_investment_type_law_route.route(
        HttpRequest(body=attributes)
    )

    # Testing input
    assert register_proposal_investment_type_law_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_proposal_id():
    """Testing route with invalid proposal_id"""

    register_proposal_investment_type_law_use_case = (
        RegisterProposalInvestmentTypeLawSpy(ProposalInvestmentTypeLawRepositorySpy())
    )
    register_proposal_investment_type_law_route = RegisterProposalInvestmentTypeLawController(
        register_proposal_investment_type_law_use_case=register_proposal_investment_type_law_use_case
    )

    attributes = {
        "investment_type_law_id": faker.random_int(min=1, max=100),
        "proposal_id": "invalid_uuid",
    }

    response = register_proposal_investment_type_law_route.route(
        HttpRequest(body=attributes)
    )

    # Testing input
    assert register_proposal_investment_type_law_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_proposal_investment_type_law_use_case = (
        RegisterProposalInvestmentTypeLawSpy(ProposalInvestmentTypeLawRepositorySpy())
    )
    register_proposal_investment_type_law_route = RegisterProposalInvestmentTypeLawController(
        register_proposal_investment_type_law_use_case=register_proposal_investment_type_law_use_case
    )

    attributes = {
        "investment_type_law_id": faker.random_int(min=1, max=100)
        # Missing proposal_id
    }

    response = register_proposal_investment_type_law_route.route(
        HttpRequest(body=attributes)
    )

    # Testing input
    assert register_proposal_investment_type_law_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_investment_type_law_use_case = (
        RegisterProposalInvestmentTypeLawSpy(ProposalInvestmentTypeLawRepositorySpy())
    )
    register_proposal_investment_type_law_route = RegisterProposalInvestmentTypeLawController(
        register_proposal_investment_type_law_use_case=register_proposal_investment_type_law_use_case
    )

    response = register_proposal_investment_type_law_route.route(HttpRequest())

    # Testing input
    assert register_proposal_investment_type_law_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_proposal_investment_type_law_use_case = (
        RegisterProposalInvestmentTypeLawSpy(ProposalInvestmentTypeLawRepositorySpy())
    )
    register_proposal_investment_type_law_route = RegisterProposalInvestmentTypeLawController(
        register_proposal_investment_type_law_use_case=register_proposal_investment_type_law_use_case
    )

    response = register_proposal_investment_type_law_route.route(HttpRequest(body={}))

    # Testing input
    assert register_proposal_investment_type_law_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_negative_id():
    """Testing route with negative investment_type_law_id"""

    register_proposal_investment_type_law_use_case = (
        RegisterProposalInvestmentTypeLawSpy(ProposalInvestmentTypeLawRepositorySpy())
    )
    register_proposal_investment_type_law_route = RegisterProposalInvestmentTypeLawController(
        register_proposal_investment_type_law_use_case=register_proposal_investment_type_law_use_case
    )

    attributes = {"investment_type_law_id": -1, "proposal_id": str(uuid.uuid4())}

    response = register_proposal_investment_type_law_route.route(
        HttpRequest(body=attributes)
    )

    # Testing input
    assert register_proposal_investment_type_law_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
