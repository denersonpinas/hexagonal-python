from faker import Faker
import uuid
from src.data.test import RegisterProposalBeneficiarySpy
from src.infra.test import ProposalBeneficiaryRepositorySpy
from src.presenters.controllers import RegisterProposalBeneficiaryController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalBeneficiary"""

    register_proposal_beneficiary_use_case = RegisterProposalBeneficiarySpy(
        ProposalBeneficiaryRepositorySpy()
    )
    register_proposal_beneficiary_route = RegisterProposalBeneficiaryController(
        register_proposal_beneficiary_use_case=register_proposal_beneficiary_use_case
    )

    attributes = {
        "quantidade": faker.random_int(min=1, max=100),
        "proposta_id": uuid.uuid4(),
    }

    response = register_proposal_beneficiary_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_beneficiary_use_case.register_param["quantidade"]
        == attributes["quantidade"]
    )
    assert (
        register_proposal_beneficiary_use_case.register_param["proposta_id"]
        == attributes["proposta_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_uuid():
    """Testing route method with invalid UUID"""

    register_proposal_beneficiary_use_case = RegisterProposalBeneficiarySpy(
        ProposalBeneficiaryRepositorySpy()
    )
    register_proposal_beneficiary_route = RegisterProposalBeneficiaryController(
        register_proposal_beneficiary_use_case=register_proposal_beneficiary_use_case
    )

    attributes = {
        "quantidade": faker.random_int(min=1, max=100),
        "proposta_id": "invalid_uuid",
    }

    response = register_proposal_beneficiary_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_beneficiary_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_quantidade():
    """Testing route method with invalid quantidade"""

    register_proposal_beneficiary_use_case = RegisterProposalBeneficiarySpy(
        ProposalBeneficiaryRepositorySpy()
    )
    register_proposal_beneficiary_route = RegisterProposalBeneficiaryController(
        register_proposal_beneficiary_use_case=register_proposal_beneficiary_use_case
    )

    attributes = {"quantidade": "invalid_number", "proposta_id": str(uuid.uuid4())}

    response = register_proposal_beneficiary_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_beneficiary_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_proposal_beneficiary_use_case = RegisterProposalBeneficiarySpy(
        ProposalBeneficiaryRepositorySpy()
    )
    register_proposal_beneficiary_route = RegisterProposalBeneficiaryController(
        register_proposal_beneficiary_use_case=register_proposal_beneficiary_use_case
    )

    attributes = {
        "quantidade": faker.random_int(min=1, max=100)
        # Missing proposta_id
    }

    response = register_proposal_beneficiary_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_beneficiary_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_beneficiary_use_case = RegisterProposalBeneficiarySpy(
        ProposalBeneficiaryRepositorySpy()
    )
    register_proposal_beneficiary_route = RegisterProposalBeneficiaryController(
        register_proposal_beneficiary_use_case=register_proposal_beneficiary_use_case
    )

    response = register_proposal_beneficiary_route.route(HttpRequest())

    # Testing input
    assert register_proposal_beneficiary_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_proposal_beneficiary_use_case = RegisterProposalBeneficiarySpy(
        ProposalBeneficiaryRepositorySpy()
    )
    register_proposal_beneficiary_route = RegisterProposalBeneficiaryController(
        register_proposal_beneficiary_use_case=register_proposal_beneficiary_use_case
    )

    response = register_proposal_beneficiary_route.route(HttpRequest(body={}))

    # Testing input
    assert register_proposal_beneficiary_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_zero_quantidade():
    """Testing route with quantidade equal to zero"""

    register_proposal_beneficiary_use_case = RegisterProposalBeneficiarySpy(
        ProposalBeneficiaryRepositorySpy()
    )
    register_proposal_beneficiary_route = RegisterProposalBeneficiaryController(
        register_proposal_beneficiary_use_case=register_proposal_beneficiary_use_case
    )

    attributes = {"quantidade": 0, "proposta_id": str(uuid.uuid4())}

    response = register_proposal_beneficiary_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_beneficiary_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
