import uuid
from faker import Faker
from src.infra.test import PartnershipHistoryRepositorySpy
from .register import RegisterPartnershipHistory

faker = Faker()


def test_register():
    """Testing register method with all fields"""

    partnership_history_repository = PartnershipHistoryRepositorySpy()
    register_partnership_history = RegisterPartnershipHistory(
        partnership_history_repository
    )

    attributes = {
        "sponsors_number": faker.random_int(min=0),
        "renewal_number": faker.random_int(min=0),
        "proposal_id": uuid.uuid4(),
        "additional_info": faker.text(max_nb_chars=500),
    }

    response = register_partnership_history.register(**attributes)

    # Testing inputs
    assert (
        partnership_history_repository.insert_partnership_history_params == attributes
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_only_required():
    """Testing register method with only required fields"""

    partnership_history_repository = PartnershipHistoryRepositorySpy()
    register_partnership_history = RegisterPartnershipHistory(
        partnership_history_repository
    )

    attributes = {
        "sponsors_number": faker.random_int(min=0),
        "renewal_number": faker.random_int(min=0),
        "proposal_id": uuid.uuid4(),
    }

    response = register_partnership_history.register(**attributes)

    # Testing inputs
    assert (
        partnership_history_repository.insert_partnership_history_params[
            "sponsors_number"
        ]
        == attributes["sponsors_number"]
    )
    assert (
        partnership_history_repository.insert_partnership_history_params[
            "renewal_number"
        ]
        == attributes["renewal_number"]
    )
    assert (
        partnership_history_repository.insert_partnership_history_params["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_numbers():
    """Testing register with invalid negative numbers"""

    partnership_history_repository = PartnershipHistoryRepositorySpy()
    register_partnership_history = RegisterPartnershipHistory(
        partnership_history_repository
    )

    attributes = {
        "sponsors_number": -1,
        "renewal_number": -1,
        "proposal_id": faker.uuid4(),
    }

    response = register_partnership_history.register(**attributes)

    # Testing inputs
    assert partnership_history_repository.insert_partnership_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_additional_info():
    """Testing register with invalid additional info length"""

    partnership_history_repository = PartnershipHistoryRepositorySpy()
    register_partnership_history = RegisterPartnershipHistory(
        partnership_history_repository
    )

    attributes = {
        "sponsors_number": faker.random_int(min=0),
        "renewal_number": faker.random_int(min=0),
        "proposal_id": faker.uuid4(),
        "additional_info": faker.text(max_nb_chars=6000),
    }

    response = register_partnership_history.register(**attributes)

    # Testing inputs
    assert partnership_history_repository.insert_partnership_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    partnership_history_repository = PartnershipHistoryRepositorySpy()
    register_partnership_history = RegisterPartnershipHistory(
        partnership_history_repository
    )

    attributes = {
        "sponsors_number": faker.name(),
        "renewal_number": faker.name(),
        "proposal_id": faker.random_number(),
        "additional_info": faker.random_number(),
    }

    response = register_partnership_history.register(**attributes)

    # Testing inputs
    assert partnership_history_repository.insert_partnership_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
