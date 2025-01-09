from faker import Faker
from uuid import uuid4
from src.infra.test import ProposalMetaRepositorySpy
from .register import RegisterProposalMeta

faker = Faker()


def test_register():
    """Testing register method"""

    proposal_meta_repository = ProposalMetaRepositorySpy()
    register_proposal_meta = RegisterProposalMeta(proposal_meta_repository)

    attributes = {
        "order": faker.random_int(min=1),
        "goal": faker.text(max_nb_chars=500),
        "quantity": faker.random_int(min=1),
        "proposal_id": uuid4(),
    }

    response = register_proposal_meta.register(**attributes)

    # Testing inputs
    assert (
        proposal_meta_repository.insert_proposal_meta_params["order"]
        == attributes["order"]
    )
    assert (
        proposal_meta_repository.insert_proposal_meta_params["goal"]
        == attributes["goal"]
    )
    assert (
        proposal_meta_repository.insert_proposal_meta_params["quantity"]
        == attributes["quantity"]
    )
    assert (
        proposal_meta_repository.insert_proposal_meta_params["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_values():
    """Testing register with invalid numeric values"""

    proposal_meta_repository = ProposalMetaRepositorySpy()
    register_proposal_meta = RegisterProposalMeta(proposal_meta_repository)

    attributes = {
        "order": 0,
        "goal": faker.text(max_nb_chars=500),
        "quantity": 0,
        "proposal_id": uuid4(),
    }

    response = register_proposal_meta.register(**attributes)

    # Testing inputs
    assert proposal_meta_repository.insert_proposal_meta_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_goal_length():
    """Testing register with invalid goal length"""

    proposal_meta_repository = ProposalMetaRepositorySpy()
    register_proposal_meta = RegisterProposalMeta(proposal_meta_repository)

    attributes = {
        "order": faker.random_int(min=1),
        "goal": faker.text(max_nb_chars=1600),
        "quantity": faker.random_int(min=1),
        "proposal_id": uuid4(),
    }

    response = register_proposal_meta.register(**attributes)

    # Testing inputs
    assert proposal_meta_repository.insert_proposal_meta_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    proposal_meta_repository = ProposalMetaRepositorySpy()
    register_proposal_meta = RegisterProposalMeta(proposal_meta_repository)

    attributes = {
        "order": faker.name(),
        "goal": faker.random_number(),
        "quantity": faker.name(),
        "proposal_id": faker.name(),
    }

    response = register_proposal_meta.register(**attributes)

    # Testing inputs
    assert proposal_meta_repository.insert_proposal_meta_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
