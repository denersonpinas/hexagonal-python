from faker import Faker
from src.data.test import RegisterProposalThematicSpy
from src.infra.test import ProposalThematicRepositorySpy
from src.presenters.controllers import RegisterProposalThematicController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalThematic"""

    register_proposal_thematic_use_case = RegisterProposalThematicSpy(
        ProposalThematicRepositorySpy()
    )
    register_proposal_thematic_route = RegisterProposalThematicController(
        register_proposal_thematic_use_case=register_proposal_thematic_use_case
    )

    attributes = {
        "proposal_id": faker.uuid4(),
        "thematic_id": faker.random_int(min=1, max=100),
    }

    response = register_proposal_thematic_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_thematic_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proposal_thematic_use_case.register_param["thematic_id"]
        == attributes["thematic_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_thematic_id():
    """Testing route with invalid thematic_id"""

    register_proposal_thematic_use_case = RegisterProposalThematicSpy(
        ProposalThematicRepositorySpy()
    )
    register_proposal_thematic_route = RegisterProposalThematicController(
        register_proposal_thematic_use_case=register_proposal_thematic_use_case
    )

    attributes = {"proposal_id": faker.uuid4(), "thematic_id": "invalid_id"}

    response = register_proposal_thematic_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_thematic_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_proposal_thematic_use_case = RegisterProposalThematicSpy(
        ProposalThematicRepositorySpy()
    )
    register_proposal_thematic_route = RegisterProposalThematicController(
        register_proposal_thematic_use_case=register_proposal_thematic_use_case
    )

    attributes = {
        "proposal_id": faker.uuid4()
        # Missing thematic_id
    }

    response = register_proposal_thematic_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_thematic_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_thematic_use_case = RegisterProposalThematicSpy(
        ProposalThematicRepositorySpy()
    )
    register_proposal_thematic_route = RegisterProposalThematicController(
        register_proposal_thematic_use_case=register_proposal_thematic_use_case
    )

    response = register_proposal_thematic_route.route(HttpRequest())

    # Testing input
    assert register_proposal_thematic_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
