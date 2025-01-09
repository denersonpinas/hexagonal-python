from faker import Faker
from uuid import uuid4
from src.infra.test import ProposalBeneficiaryCategorizationRepositorySpy
from .register import RegisterProposalBeneficiaryCategorization

faker = Faker()


def test_register():
    """Testing register method"""

    repository = ProposalBeneficiaryCategorizationRepositorySpy()
    register_categorization = RegisterProposalBeneficiaryCategorization(repository)

    attributes = {
        "categorizacao_id": faker.random_int(min=1),
        "proposta_beneficiario_id": uuid4(),
    }

    response = register_categorization.register(**attributes)

    # Testing inputs
    assert (
        repository.insert_proposal_beneficiary_categorization_params["categorizacao_id"]
        == attributes["categorizacao_id"]
    )
    assert (
        repository.insert_proposal_beneficiary_categorization_params[
            "proposta_beneficiario_id"
        ]
        == attributes["proposta_beneficiario_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_categorization():
    """Testing register with invalid categorization id"""

    repository = ProposalBeneficiaryCategorizationRepositorySpy()
    register_categorization = RegisterProposalBeneficiaryCategorization(repository)

    attributes = {"categorizacao_id": 0, "proposta_beneficiario_id": uuid4()}

    response = register_categorization.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_beneficiary_categorization_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    repository = ProposalBeneficiaryCategorizationRepositorySpy()
    register_categorization = RegisterProposalBeneficiaryCategorization(repository)

    attributes = {
        "categorizacao_id": faker.name(),
        "proposta_beneficiario_id": faker.name(),
    }

    response = register_categorization.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_beneficiary_categorization_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
