from faker import Faker
from uuid import uuid4
from src.infra.test import ProposalSponsorRepositorySpy
from .register import RegisterProposalSponsor

faker = Faker()


def test_register():
    """Testing register method"""

    proposal_sponsor_repository = ProposalSponsorRepositorySpy()
    register_proposal_sponsor = RegisterProposalSponsor(proposal_sponsor_repository)

    attributes = {
        "nome": faker.name()[:100],
        "formato": faker.word()[:50],
        "valor": faker.pyfloat(positive=True),
        "proposta_id": uuid4(),
    }

    response = register_proposal_sponsor.register(**attributes)

    # Testing inputs
    assert (
        proposal_sponsor_repository.insert_proposal_sponsor_params["nome"]
        == attributes["nome"]
    )
    assert (
        proposal_sponsor_repository.insert_proposal_sponsor_params["formato"]
        == attributes["formato"]
    )
    assert (
        proposal_sponsor_repository.insert_proposal_sponsor_params["valor"]
        == attributes["valor"]
    )
    assert (
        proposal_sponsor_repository.insert_proposal_sponsor_params["proposta_id"]
        == attributes["proposta_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_length():
    """Testing register with invalid string lengths"""

    proposal_sponsor_repository = ProposalSponsorRepositorySpy()
    register_proposal_sponsor = RegisterProposalSponsor(proposal_sponsor_repository)

    attributes = {
        "nome": faker.text(max_nb_chars=2000),
        "formato": faker.text(max_nb_chars=1000),
        "valor": faker.pyfloat(positive=True),
        "proposta_id": uuid4(),
    }

    response = register_proposal_sponsor.register(**attributes)

    # Testing inputs
    assert proposal_sponsor_repository.insert_proposal_sponsor_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_value():
    """Testing register with invalid value"""

    proposal_sponsor_repository = ProposalSponsorRepositorySpy()
    register_proposal_sponsor = RegisterProposalSponsor(proposal_sponsor_repository)

    attributes = {
        "nome": faker.name()[:100],
        "formato": faker.word()[:50],
        "valor": -1.0,
        "proposta_id": uuid4(),
    }

    response = register_proposal_sponsor.register(**attributes)

    # Testing inputs
    assert proposal_sponsor_repository.insert_proposal_sponsor_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    proposal_sponsor_repository = ProposalSponsorRepositorySpy()
    register_proposal_sponsor = RegisterProposalSponsor(proposal_sponsor_repository)

    attributes = {
        "nome": faker.random_number(),
        "formato": faker.random_number(),
        "valor": faker.name(),
        "proposta_id": faker.name(),
    }

    response = register_proposal_sponsor.register(**attributes)

    # Testing inputs
    assert proposal_sponsor_repository.insert_proposal_sponsor_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
