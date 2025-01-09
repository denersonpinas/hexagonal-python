from faker import Faker
from uuid import uuid4
from src.infra.test import ProposalCounterpartRepositorySpy
from .register import RegisterProposalCounterpart

faker = Faker()


def test_register():
    """Testing register method with all fields"""

    repository = ProposalCounterpartRepositorySpy()
    register_counterpart = RegisterProposalCounterpart(repository)

    attributes = {
        "description": faker.text(max_nb_chars=500),
        "quantity": faker.random_int(min=1),
        "investment_type_law_counterpart_id": faker.random_int(min=1),
        "proposal_investment_type_law_id": uuid4(),
        "expected": faker.random_int(min=1),
    }

    response = register_counterpart.register(**attributes)

    # Testing inputs
    assert (
        repository.insert_proposal_counterpart_params["description"]
        == attributes["description"]
    )
    assert (
        repository.insert_proposal_counterpart_params["quantity"]
        == attributes["quantity"]
    )
    assert (
        repository.insert_proposal_counterpart_params[
            "investment_type_law_counterpart_id"
        ]
        == attributes["investment_type_law_counterpart_id"]
    )
    assert (
        repository.insert_proposal_counterpart_params["proposal_investment_type_law_id"]
        == attributes["proposal_investment_type_law_id"]
    )
    assert (
        repository.insert_proposal_counterpart_params["expected"]
        == attributes["expected"]
    )
    assert isinstance(repository.insert_proposal_counterpart_params["id"], str)

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_only_required():
    """Testing register method with only required fields"""

    repository = ProposalCounterpartRepositorySpy()
    register_counterpart = RegisterProposalCounterpart(repository)

    attributes = {
        "description": faker.text(max_nb_chars=500),
        "quantity": faker.random_int(min=1),
        "investment_type_law_counterpart_id": faker.random_int(min=1),
        "proposal_investment_type_law_id": uuid4(),
    }

    response = register_counterpart.register(**attributes)

    # Testing inputs
    assert (
        repository.insert_proposal_counterpart_params["description"]
        == attributes["description"]
    )
    assert (
        repository.insert_proposal_counterpart_params["quantity"]
        == attributes["quantity"]
    )
    assert (
        repository.insert_proposal_counterpart_params[
            "investment_type_law_counterpart_id"
        ]
        == attributes["investment_type_law_counterpart_id"]
    )
    assert (
        repository.insert_proposal_counterpart_params["proposal_investment_type_law_id"]
        == attributes["proposal_investment_type_law_id"]
    )
    assert isinstance(repository.insert_proposal_counterpart_params["id"], str)

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_description_length():
    """Testing register with invalid description length"""

    repository = ProposalCounterpartRepositorySpy()
    register_counterpart = RegisterProposalCounterpart(repository)

    attributes = {
        "description": faker.text(max_nb_chars=6000),
        "quantity": faker.random_int(min=1),
        "investment_type_law_counterpart_id": faker.random_int(min=1),
        "proposal_investment_type_law_id": uuid4(),
    }

    response = register_counterpart.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_counterpart_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_quantities():
    """Testing register with invalid quantities"""

    repository = ProposalCounterpartRepositorySpy()
    register_counterpart = RegisterProposalCounterpart(repository)

    attributes = {
        "description": faker.text(max_nb_chars=500),
        "quantity": 0,
        "investment_type_law_counterpart_id": faker.random_int(min=1),
        "proposal_investment_type_law_id": uuid4(),
        "expected": 0,
    }

    response = register_counterpart.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_counterpart_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_investment_type_law_counterpart_id():
    """Testing register with invalid investment type law counterpart id"""

    repository = ProposalCounterpartRepositorySpy()
    register_counterpart = RegisterProposalCounterpart(repository)

    attributes = {
        "description": faker.text(max_nb_chars=500),
        "quantity": faker.random_int(min=1),
        "investment_type_law_counterpart_id": 0,
        "proposal_investment_type_law_id": uuid4(),
    }

    response = register_counterpart.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_counterpart_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    repository = ProposalCounterpartRepositorySpy()
    register_counterpart = RegisterProposalCounterpart(repository)

    attributes = {
        "description": faker.random_number(),
        "quantity": faker.name(),
        "investment_type_law_counterpart_id": faker.name(),
        "proposal_investment_type_law_id": faker.random_number(),
        "expected": faker.name(),
    }

    response = register_counterpart.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_counterpart_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
