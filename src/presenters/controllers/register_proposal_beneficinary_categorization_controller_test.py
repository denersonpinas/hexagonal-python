from faker import Faker
import uuid
from src.data.test import RegisterProposalBeneficiaryCategorizationSpy
from src.infra.test import ProposalBeneficiaryCategorizationRepositorySpy
from src.presenters.controllers import (
    RegisterProposalBeneficinaryCategorizationController,
)
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalBeneficiaryCategorizationController"""

    register_use_case = RegisterProposalBeneficiaryCategorizationSpy(
        ProposalBeneficiaryCategorizationRepositorySpy()
    )
    register_route = RegisterProposalBeneficinaryCategorizationController(
        register_proposal_beneficiary_categorization_use_case=register_use_case
    )

    attributes = {
        "categorizacao_id": faker.random_int(min=1, max=100),
        "proposta_beneficiario_id": str(uuid.uuid4()),
    }

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_use_case.register_param["categorizacao_id"]
        == attributes["categorizacao_id"]
    )
    assert register_use_case.register_param["proposta_beneficiario_id"] == uuid.UUID(
        attributes["proposta_beneficiario_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_uuid():
    """Testing route method with invalid UUID"""

    register_use_case = RegisterProposalBeneficiaryCategorizationSpy(
        ProposalBeneficiaryCategorizationRepositorySpy()
    )
    register_route = RegisterProposalBeneficinaryCategorizationController(
        register_proposal_beneficiary_categorization_use_case=register_use_case
    )

    attributes = {
        "categorizacao_id": faker.random_int(min=1, max=100),
        "proposta_beneficiario_id": "invalid_uuid",
    }

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_categorizacao_id():
    """Testing route method with invalid categorizacao_id"""

    register_use_case = RegisterProposalBeneficiaryCategorizationSpy(
        ProposalBeneficiaryCategorizationRepositorySpy()
    )
    register_route = RegisterProposalBeneficinaryCategorizationController(
        register_proposal_beneficiary_categorization_use_case=register_use_case
    )

    attributes = {
        "categorizacao_id": "invalid_id",
        "proposta_beneficiario_id": str(uuid.uuid4()),
    }

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_use_case = RegisterProposalBeneficiaryCategorizationSpy(
        ProposalBeneficiaryCategorizationRepositorySpy()
    )
    register_route = RegisterProposalBeneficinaryCategorizationController(
        register_proposal_beneficiary_categorization_use_case=register_use_case
    )

    attributes = {
        "categorizacao_id": faker.random_int(min=1, max=100)
        # Missing proposta_beneficiario_id
    }

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_use_case = RegisterProposalBeneficiaryCategorizationSpy(
        ProposalBeneficiaryCategorizationRepositorySpy()
    )
    register_route = RegisterProposalBeneficinaryCategorizationController(
        register_proposal_beneficiary_categorization_use_case=register_use_case
    )

    response = register_route.route(HttpRequest())

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_use_case = RegisterProposalBeneficiaryCategorizationSpy(
        ProposalBeneficiaryCategorizationRepositorySpy()
    )
    register_route = RegisterProposalBeneficinaryCategorizationController(
        register_proposal_beneficiary_categorization_use_case=register_use_case
    )

    response = register_route.route(HttpRequest(body={}))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_zero_categorizacao_id():
    """Testing route with categorizacao_id equal to zero"""

    register_use_case = RegisterProposalBeneficiaryCategorizationSpy(
        ProposalBeneficiaryCategorizationRepositorySpy()
    )
    register_route = RegisterProposalBeneficinaryCategorizationController(
        register_proposal_beneficiary_categorization_use_case=register_use_case
    )

    attributes = {"categorizacao_id": 0, "proposta_beneficiario_id": str(uuid.uuid4())}

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_negative_categorizacao_id():
    """Testing route with negative categorizacao_id"""

    register_use_case = RegisterProposalBeneficiaryCategorizationSpy(
        ProposalBeneficiaryCategorizationRepositorySpy()
    )
    register_route = RegisterProposalBeneficinaryCategorizationController(
        register_proposal_beneficiary_categorization_use_case=register_use_case
    )

    attributes = {"categorizacao_id": -1, "proposta_beneficiario_id": str(uuid.uuid4())}

    response = register_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
