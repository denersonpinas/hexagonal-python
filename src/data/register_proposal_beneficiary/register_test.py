from faker import Faker
from uuid import uuid4
from src.infra.test import ProposalBeneficiaryRepositorySpy
from .register import RegisterProposalBeneficiary

faker = Faker()


def test_register():
    """Testing register method"""

    proposal_beneficiary_repository = ProposalBeneficiaryRepositorySpy()
    register_proposal_beneficiary = RegisterProposalBeneficiary(
        proposal_beneficiary_repository
    )

    attributes = {"quantidade": faker.random_int(min=1), "proposta_id": uuid4()}

    response = register_proposal_beneficiary.register(**attributes)

    # Testing inputs
    assert (
        proposal_beneficiary_repository.insert_proposal_beneficiary_params["quantidade"]
        == attributes["quantidade"]
    )
    assert (
        proposal_beneficiary_repository.insert_proposal_beneficiary_params[
            "proposta_id"
        ]
        == attributes["proposta_id"]
    )
    assert isinstance(
        proposal_beneficiary_repository.insert_proposal_beneficiary_params["id"], str
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_quantity_zero():
    """Testing register with zero quantity"""

    proposal_beneficiary_repository = ProposalBeneficiaryRepositorySpy()
    register_proposal_beneficiary = RegisterProposalBeneficiary(
        proposal_beneficiary_repository
    )

    attributes = {"quantidade": 0, "proposta_id": uuid4()}

    response = register_proposal_beneficiary.register(**attributes)

    # Testing inputs
    assert proposal_beneficiary_repository.insert_proposal_beneficiary_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    proposal_beneficiary_repository = ProposalBeneficiaryRepositorySpy()
    register_proposal_beneficiary = RegisterProposalBeneficiary(
        proposal_beneficiary_repository
    )

    attributes = {"quantidade": faker.name(), "proposta_id": faker.name()}

    response = register_proposal_beneficiary.register(**attributes)

    # Testing inputs
    assert proposal_beneficiary_repository.insert_proposal_beneficiary_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
