from faker import Faker
from uuid import uuid4
from src.infra.test import ProposalFileRepositorySpy
from .register import RegisterProposalFile

faker = Faker()


def test_register():
    """Testing register method"""

    proposal_file_repository = ProposalFileRepositorySpy()
    register_proposal_file = RegisterProposalFile(proposal_file_repository)

    attributes = {
        "name": faker.file_name()[:100],
        "extension": faker.file_extension()[:10],
        "size": faker.random_int(min=1),
        "uri": faker.uri()[:500],
        "proposal_id": uuid4(),
        "type_id": faker.uuid4(),
    }

    response = register_proposal_file.register(**attributes)

    # Testing inputs
    assert (
        proposal_file_repository.insert_proposal_file_params["name"]
        == attributes["name"]
    )
    assert (
        proposal_file_repository.insert_proposal_file_params["extension"]
        == attributes["extension"]
    )
    assert (
        proposal_file_repository.insert_proposal_file_params["size"]
        == attributes["size"]
    )
    assert (
        proposal_file_repository.insert_proposal_file_params["uri"] == attributes["uri"]
    )
    assert (
        proposal_file_repository.insert_proposal_file_params["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        proposal_file_repository.insert_proposal_file_params["type_id"]
        == attributes["type_id"]
    )
    assert isinstance(proposal_file_repository.insert_proposal_file_params["id"], str)

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_lengths():
    """Testing register with invalid string lengths"""

    proposal_file_repository = ProposalFileRepositorySpy()
    register_proposal_file = RegisterProposalFile(proposal_file_repository)

    attributes = {
        "name": faker.text(max_nb_chars=150),
        "extension": faker.text(max_nb_chars=20),
        "size": faker.random_int(min=1),
        "uri": faker.text(max_nb_chars=600),
        "proposal_id": uuid4(),
        "type_id": faker.uuid4(),
    }

    response = register_proposal_file.register(**attributes)

    # Testing inputs
    assert proposal_file_repository.insert_proposal_file_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_size():
    """Testing register with invalid file size"""

    proposal_file_repository = ProposalFileRepositorySpy()
    register_proposal_file = RegisterProposalFile(proposal_file_repository)

    attributes = {
        "name": faker.file_name()[:100],
        "extension": faker.file_extension()[:10],
        "size": 0,
        "uri": faker.uri()[:500],
        "proposal_id": uuid4(),
        "type_id": faker.uuid4(),
    }

    response = register_proposal_file.register(**attributes)

    # Testing inputs
    assert proposal_file_repository.insert_proposal_file_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    proposal_file_repository = ProposalFileRepositorySpy()
    register_proposal_file = RegisterProposalFile(proposal_file_repository)

    attributes = {
        "name": faker.random_number(),
        "extension": faker.random_number(),
        "size": faker.name(),
        "uri": faker.random_number(),
        "proposal_id": faker.name(),
        "type_id": faker.random_number(),
    }

    response = register_proposal_file.register(**attributes)

    # Testing inputs
    assert proposal_file_repository.insert_proposal_file_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
