from faker import Faker
from uuid import uuid4
from src.infra.test import ProposalInvestmentTypeLawRepositorySpy
from .register import RegisterProposalInvestmentTypeLaw

faker = Faker()


def test_register():
    """Testing register method"""

    repository = ProposalInvestmentTypeLawRepositorySpy()
    register_investment_type_law = RegisterProposalInvestmentTypeLaw(repository)

    attributes = {
        "investment_type_law_id": faker.random_int(min=1),
        "proposal_id": uuid4(),
    }

    response = register_investment_type_law.register(**attributes)

    # Testing inputs
    assert (
        repository.insert_proposal_investment_type_law_params["investment_type_law_id"]
        == attributes["investment_type_law_id"]
    )
    assert (
        repository.insert_proposal_investment_type_law_params["proposal_id"]
        == attributes["proposal_id"]
    )
    assert isinstance(repository.insert_proposal_investment_type_law_params["id"], str)

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_investment_type_law_id():
    """Testing register with invalid investment type law id"""

    repository = ProposalInvestmentTypeLawRepositorySpy()
    register_investment_type_law = RegisterProposalInvestmentTypeLaw(repository)

    attributes = {"investment_type_law_id": 0, "proposal_id": uuid4()}

    response = register_investment_type_law.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_investment_type_law_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    repository = ProposalInvestmentTypeLawRepositorySpy()
    register_investment_type_law = RegisterProposalInvestmentTypeLaw(repository)

    attributes = {
        "investment_type_law_id": faker.name(),
        "proposal_id": faker.random_number(),
    }

    response = register_investment_type_law.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_investment_type_law_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
