from faker import Faker
import uuid
from src.data.test import RegisterProposalMetaSpy
from src.infra.test import ProposalMetaRepositorySpy
from src.presenters.controllers import RegisterProposalMetaController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalMeta"""

    register_proposal_meta_use_case = RegisterProposalMetaSpy(
        ProposalMetaRepositorySpy()
    )
    register_proposal_meta_route = RegisterProposalMetaController(
        register_proposal_meta_use_case=register_proposal_meta_use_case
    )

    attributes = {
        "order": faker.random_int(min=1, max=100),
        "goal": faker.text(max_nb_chars=200),
        "quantity": faker.random_int(min=1, max=1000),
        "proposal_id": str(uuid.uuid4()),
    }

    response = register_proposal_meta_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_meta_use_case.register_param["order"] == attributes["order"]
    )
    assert register_proposal_meta_use_case.register_param["goal"] == attributes["goal"]
    assert (
        register_proposal_meta_use_case.register_param["quantity"]
        == attributes["quantity"]
    )
    assert register_proposal_meta_use_case.register_param["proposal_id"] == uuid.UUID(
        attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_uuid():
    """Testing route method with invalid UUID"""

    register_proposal_meta_use_case = RegisterProposalMetaSpy(
        ProposalMetaRepositorySpy()
    )
    register_proposal_meta_route = RegisterProposalMetaController(
        register_proposal_meta_use_case=register_proposal_meta_use_case
    )

    attributes = {
        "order": faker.random_int(min=1, max=100),
        "goal": faker.text(),
        "quantity": faker.random_int(min=1, max=1000),
        "proposal_id": "invalid_uuid",
    }

    response = register_proposal_meta_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_meta_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_integers():
    """Testing route method with invalid integer values"""

    register_proposal_meta_use_case = RegisterProposalMetaSpy(
        ProposalMetaRepositorySpy()
    )
    register_proposal_meta_route = RegisterProposalMetaController(
        register_proposal_meta_use_case=register_proposal_meta_use_case
    )

    attributes = {
        "order": "invalid_order",
        "goal": faker.text(),
        "quantity": "invalid_quantity",
        "proposal_id": str(uuid.uuid4()),
    }

    response = register_proposal_meta_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_meta_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_proposal_meta_use_case = RegisterProposalMetaSpy(
        ProposalMetaRepositorySpy()
    )
    register_proposal_meta_route = RegisterProposalMetaController(
        register_proposal_meta_use_case=register_proposal_meta_use_case
    )

    attributes = {
        "order": faker.random_int(min=1, max=100),
        "goal": faker.text(),
        # Missing quantity and proposal_id
    }

    response = register_proposal_meta_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_meta_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_meta_use_case = RegisterProposalMetaSpy(
        ProposalMetaRepositorySpy()
    )
    register_proposal_meta_route = RegisterProposalMetaController(
        register_proposal_meta_use_case=register_proposal_meta_use_case
    )

    response = register_proposal_meta_route.route(HttpRequest())

    # Testing input
    assert register_proposal_meta_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_proposal_meta_use_case = RegisterProposalMetaSpy(
        ProposalMetaRepositorySpy()
    )
    register_proposal_meta_route = RegisterProposalMetaController(
        register_proposal_meta_use_case=register_proposal_meta_use_case
    )

    response = register_proposal_meta_route.route(HttpRequest(body={}))

    # Testing input
    assert register_proposal_meta_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_zero_values():
    """Testing route with zero values for order and quantity"""

    register_proposal_meta_use_case = RegisterProposalMetaSpy(
        ProposalMetaRepositorySpy()
    )
    register_proposal_meta_route = RegisterProposalMetaController(
        register_proposal_meta_use_case=register_proposal_meta_use_case
    )

    attributes = {
        "order": 0,
        "goal": faker.text(),
        "quantity": 0,
        "proposal_id": str(uuid.uuid4()),
    }

    response = register_proposal_meta_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_meta_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
