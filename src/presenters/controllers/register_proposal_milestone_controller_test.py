from faker import Faker
from src.data.test import RegisterProposalMilestoneSpy
from src.infra.test import ProposalMilestoneRepositorySpy
from src.presenters.controllers import RegisterProposalMilestoneController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalMilestone"""

    register_proposal_milestone_use_case = RegisterProposalMilestoneSpy(
        ProposalMilestoneRepositorySpy()
    )
    register_proposal_milestone_route = RegisterProposalMilestoneController(
        register_proposal_milestone_use_case=register_proposal_milestone_use_case
    )

    attributes = {
        "description": faker.text()[:500],
        "execution_date": faker.date(),
        "proposal_id": faker.uuid4(),
    }

    response = register_proposal_milestone_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_milestone_use_case.register_param["description"]
        == attributes["description"]
    )
    assert (
        register_proposal_milestone_use_case.register_param["execution_date"]
        == attributes["execution_date"]
    )
    assert (
        register_proposal_milestone_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_date():
    """Testing route with invalid execution_date format"""

    register_proposal_milestone_use_case = RegisterProposalMilestoneSpy(
        ProposalMilestoneRepositorySpy()
    )
    register_proposal_milestone_route = RegisterProposalMilestoneController(
        register_proposal_milestone_use_case=register_proposal_milestone_use_case
    )

    attributes = {
        "description": faker.text()[:500],
        "execution_date": "invalid_date",
        "proposal_id": faker.uuid4(),
    }

    response = register_proposal_milestone_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_milestone_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_proposal_milestone_use_case = RegisterProposalMilestoneSpy(
        ProposalMilestoneRepositorySpy()
    )
    register_proposal_milestone_route = RegisterProposalMilestoneController(
        register_proposal_milestone_use_case=register_proposal_milestone_use_case
    )

    attributes = {
        "description": faker.text()[:500],
        # Missing execution_date and proposal_id
    }

    response = register_proposal_milestone_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_milestone_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_milestone_use_case = RegisterProposalMilestoneSpy(
        ProposalMilestoneRepositorySpy()
    )
    register_proposal_milestone_route = RegisterProposalMilestoneController(
        register_proposal_milestone_use_case=register_proposal_milestone_use_case
    )

    response = register_proposal_milestone_route.route(HttpRequest())

    # Testing input
    assert register_proposal_milestone_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_proposal_milestone_use_case = RegisterProposalMilestoneSpy(
        ProposalMilestoneRepositorySpy()
    )
    register_proposal_milestone_route = RegisterProposalMilestoneController(
        register_proposal_milestone_use_case=register_proposal_milestone_use_case
    )

    response = register_proposal_milestone_route.route(HttpRequest(body={}))

    # Testing input
    assert register_proposal_milestone_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_description():
    """Testing route with empty description"""

    register_proposal_milestone_use_case = RegisterProposalMilestoneSpy(
        ProposalMilestoneRepositorySpy()
    )
    register_proposal_milestone_route = RegisterProposalMilestoneController(
        register_proposal_milestone_use_case=register_proposal_milestone_use_case
    )

    attributes = {
        "description": "",
        "execution_date": faker.date(),
        "proposal_id": faker.uuid4(),
    }

    response = register_proposal_milestone_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_milestone_use_case.register_param["description"]
        == attributes["description"]
    )
    assert (
        register_proposal_milestone_use_case.register_param["execution_date"]
        == attributes["execution_date"]
    )
    assert (
        register_proposal_milestone_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_future_date():
    """Testing route with future execution date"""

    register_proposal_milestone_use_case = RegisterProposalMilestoneSpy(
        ProposalMilestoneRepositorySpy()
    )
    register_proposal_milestone_route = RegisterProposalMilestoneController(
        register_proposal_milestone_use_case=register_proposal_milestone_use_case
    )

    attributes = {
        "description": faker.text()[:500],
        "execution_date": str(faker.future_date()),
        "proposal_id": faker.uuid4(),
    }

    response = register_proposal_milestone_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_milestone_use_case.register_param["description"]
        == attributes["description"]
    )
    assert (
        register_proposal_milestone_use_case.register_param["execution_date"]
        == attributes["execution_date"]
    )
    assert (
        register_proposal_milestone_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_past_date():
    """Testing route with past execution date"""

    register_proposal_milestone_use_case = RegisterProposalMilestoneSpy(
        ProposalMilestoneRepositorySpy()
    )
    register_proposal_milestone_route = RegisterProposalMilestoneController(
        register_proposal_milestone_use_case=register_proposal_milestone_use_case
    )

    attributes = {
        "description": faker.text(),
        "execution_date": str(faker.past_date()),
        "proposal_id": faker.uuid4(),
    }

    response = register_proposal_milestone_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_milestone_use_case.register_param["description"]
        == attributes["description"]
    )
    assert (
        register_proposal_milestone_use_case.register_param["execution_date"]
        == attributes["execution_date"]
    )
    assert (
        register_proposal_milestone_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body
