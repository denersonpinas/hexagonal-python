from faker import Faker
from src.infra.test import ProposalThematicRepositorySpy
from .register import RegisterProposalThematic

faker = Faker()


def test_register():
    """Testing register method"""

    proposal_thematic_repository = ProposalThematicRepositorySpy()
    register_proposal_thematic = RegisterProposalThematic(proposal_thematic_repository)

    attributes = {"proposal_id": faker.uuid4(), "thematic_id": faker.random_int(min=1)}

    response = register_proposal_thematic.register(**attributes)

    # Testing inputs
    assert (
        proposal_thematic_repository.insert_proposal_thematic_params["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        proposal_thematic_repository.insert_proposal_thematic_params["thematic_id"]
        == attributes["thematic_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_thematic_id():
    """Testing register with invalid thematic id"""

    proposal_thematic_repository = ProposalThematicRepositorySpy()
    register_proposal_thematic = RegisterProposalThematic(proposal_thematic_repository)

    attributes = {"proposal_id": faker.uuid4(), "thematic_id": 0}

    response = register_proposal_thematic.register(**attributes)

    # Testing inputs
    assert proposal_thematic_repository.insert_proposal_thematic_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    proposal_thematic_repository = ProposalThematicRepositorySpy()
    register_proposal_thematic = RegisterProposalThematic(proposal_thematic_repository)

    attributes = {"proposal_id": faker.random_number(), "thematic_id": faker.name()}

    response = register_proposal_thematic.register(**attributes)

    # Testing inputs
    assert proposal_thematic_repository.insert_proposal_thematic_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
