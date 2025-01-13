import uuid
from faker import Faker
from src.infra.test import ProposalMilestoneRepositorySpy
from .register import RegisterProposalMilestone

faker = Faker()


def test_register():
    """Testing register method"""

    proposal_milestone_repository = ProposalMilestoneRepositorySpy()
    register_proposal_milestone = RegisterProposalMilestone(
        proposal_milestone_repository
    )

    attributes = {
        "description": faker.text(max_nb_chars=500),
        "execution_date": faker.date(),
        "proposal_id": uuid.uuid4(),
    }

    response = register_proposal_milestone.register(**attributes)

    # Testing inputs
    assert (
        proposal_milestone_repository.insert_proposal_milestone_params["description"]
        == attributes["description"]
    )
    assert (
        proposal_milestone_repository.insert_proposal_milestone_params["execution_date"]
        == attributes["execution_date"]
    )
    assert (
        proposal_milestone_repository.insert_proposal_milestone_params["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_description_length():
    """Testing register with invalid description length"""

    proposal_milestone_repository = ProposalMilestoneRepositorySpy()
    register_proposal_milestone = RegisterProposalMilestone(
        proposal_milestone_repository
    )

    attributes = {
        "description": faker.text(max_nb_chars=6000),
        "execution_date": faker.date(),
        "proposal_id": faker.uuid4(),
    }

    response = register_proposal_milestone.register(**attributes)

    # Testing inputs
    assert proposal_milestone_repository.insert_proposal_milestone_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_date_format():
    """Testing register with invalid date format"""

    proposal_milestone_repository = ProposalMilestoneRepositorySpy()
    register_proposal_milestone = RegisterProposalMilestone(
        proposal_milestone_repository
    )

    attributes = {
        "description": faker.text(max_nb_chars=500),
        "execution_date": "2023-13-45-67",  # Invalid date format
        "proposal_id": faker.uuid4(),
    }

    response = register_proposal_milestone.register(**attributes)

    # Testing inputs
    assert proposal_milestone_repository.insert_proposal_milestone_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_date_length():
    """Testing register with invalid date length"""

    proposal_milestone_repository = ProposalMilestoneRepositorySpy()
    register_proposal_milestone = RegisterProposalMilestone(
        proposal_milestone_repository
    )

    attributes = {
        "description": faker.text(max_nb_chars=500),
        "execution_date": "2023-01-01 12:00:00",  # Date string too long
        "proposal_id": faker.uuid4(),
    }

    response = register_proposal_milestone.register(**attributes)

    # Testing inputs
    assert proposal_milestone_repository.insert_proposal_milestone_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    proposal_milestone_repository = ProposalMilestoneRepositorySpy()
    register_proposal_milestone = RegisterProposalMilestone(
        proposal_milestone_repository
    )

    attributes = {
        "description": faker.random_number(),
        "execution_date": faker.random_number(),
        "proposal_id": faker.random_number(),
    }

    response = register_proposal_milestone.register(**attributes)

    # Testing inputs
    assert proposal_milestone_repository.insert_proposal_milestone_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
