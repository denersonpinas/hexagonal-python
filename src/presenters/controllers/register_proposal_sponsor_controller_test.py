from faker import Faker
import uuid
from src.data.test import RegisterProposalSponsorSpy
from src.infra.test import ProposalSponsorRepositorySpy
from src.presenters.controllers import RegisterProposalSponsorController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalSponsor"""

    register_proposal_sponsor_use_case = RegisterProposalSponsorSpy(
        ProposalSponsorRepositorySpy()
    )
    register_proposal_sponsor_route = RegisterProposalSponsorController(
        register_proposal_sponsor_use_case=register_proposal_sponsor_use_case
    )

    attributes = {
        "nome": faker.name(),
        "formato": faker.random_element(elements=("PATROCINADOR", "APOIADOR")),
        "valor": faker.pyfloat(positive=True, min_value=100, max_value=1000000),
        "proposta_id": str(uuid.uuid4()),
    }

    response = register_proposal_sponsor_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_sponsor_use_case.register_param["nome"] == attributes["nome"]
    )
    assert (
        register_proposal_sponsor_use_case.register_param["formato"]
        == attributes["formato"]
    )
    assert (
        register_proposal_sponsor_use_case.register_param["valor"]
        == attributes["valor"]
    )
    assert register_proposal_sponsor_use_case.register_param[
        "proposta_id"
    ] == uuid.UUID(attributes["proposta_id"])

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_uuid():
    """Testing route method with invalid UUID"""

    register_proposal_sponsor_use_case = RegisterProposalSponsorSpy(
        ProposalSponsorRepositorySpy()
    )
    register_proposal_sponsor_route = RegisterProposalSponsorController(
        register_proposal_sponsor_use_case=register_proposal_sponsor_use_case
    )

    attributes = {
        "nome": faker.name(),
        "formato": faker.random_element(elements=("PATROCINADOR", "APOIADOR")),
        "valor": faker.pyfloat(positive=True),
        "proposta_id": "invalid_uuid",
    }

    response = register_proposal_sponsor_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_sponsor_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_valor():
    """Testing route method with invalid valor"""

    register_proposal_sponsor_use_case = RegisterProposalSponsorSpy(
        ProposalSponsorRepositorySpy()
    )
    register_proposal_sponsor_route = RegisterProposalSponsorController(
        register_proposal_sponsor_use_case=register_proposal_sponsor_use_case
    )

    attributes = {
        "nome": faker.name(),
        "formato": faker.random_element(elements=("PATROCINADOR", "APOIADOR")),
        "valor": "invalid_value",
        "proposta_id": str(uuid.uuid4()),
    }

    response = register_proposal_sponsor_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_sponsor_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_proposal_sponsor_use_case = RegisterProposalSponsorSpy(
        ProposalSponsorRepositorySpy()
    )
    register_proposal_sponsor_route = RegisterProposalSponsorController(
        register_proposal_sponsor_use_case=register_proposal_sponsor_use_case
    )

    attributes = {
        "nome": faker.name(),
        "formato": faker.random_element(elements=("PATROCINADOR", "APOIADOR")),
        # Missing valor and proposta_id
    }

    response = register_proposal_sponsor_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_sponsor_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_sponsor_use_case = RegisterProposalSponsorSpy(
        ProposalSponsorRepositorySpy()
    )
    register_proposal_sponsor_route = RegisterProposalSponsorController(
        register_proposal_sponsor_use_case=register_proposal_sponsor_use_case
    )

    response = register_proposal_sponsor_route.route(HttpRequest())

    # Testing input
    assert register_proposal_sponsor_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_proposal_sponsor_use_case = RegisterProposalSponsorSpy(
        ProposalSponsorRepositorySpy()
    )
    register_proposal_sponsor_route = RegisterProposalSponsorController(
        register_proposal_sponsor_use_case=register_proposal_sponsor_use_case
    )

    response = register_proposal_sponsor_route.route(HttpRequest(body={}))

    # Testing input
    assert register_proposal_sponsor_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_zero_valor():
    """Testing route with valor equal to zero"""

    register_proposal_sponsor_use_case = RegisterProposalSponsorSpy(
        ProposalSponsorRepositorySpy()
    )
    register_proposal_sponsor_route = RegisterProposalSponsorController(
        register_proposal_sponsor_use_case=register_proposal_sponsor_use_case
    )

    attributes = {
        "nome": faker.name(),
        "formato": faker.random_element(elements=("PATROCINADOR", "APOIADOR")),
        "valor": 0.0,
        "proposta_id": str(uuid.uuid4()),
    }

    response = register_proposal_sponsor_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_sponsor_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
