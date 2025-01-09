from faker import Faker
from uuid import uuid4
from src.infra.test import ProposalExecutionLocationRepositorySpy
from .register import RegisterProposalExecutionLocation

faker = Faker()


def test_register():
    """Testing register method"""

    repository = ProposalExecutionLocationRepositorySpy()
    register_execution_location = RegisterProposalExecutionLocation(repository)

    attributes = {"city_id": faker.random_int(min=1), "proposal_id": uuid4()}

    response = register_execution_location.register(**attributes)

    # Testing inputs
    assert (
        repository.insert_proposal_execution_location_params["city_id"]
        == attributes["city_id"]
    )
    assert (
        repository.insert_proposal_execution_location_params["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_city():
    """Testing register with invalid city id"""

    repository = ProposalExecutionLocationRepositorySpy()
    register_execution_location = RegisterProposalExecutionLocation(repository)

    attributes = {"city_id": 0, "proposal_id": uuid4()}

    response = register_execution_location.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_execution_location_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    repository = ProposalExecutionLocationRepositorySpy()
    register_execution_location = RegisterProposalExecutionLocation(repository)

    attributes = {"city_id": faker.name(), "proposal_id": faker.name()}

    response = register_execution_location.register(**attributes)

    # Testing inputs
    assert repository.insert_proposal_execution_location_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
