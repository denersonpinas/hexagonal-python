from faker import Faker
from src.infra.test import SupplyHistoryRepositorySpy
from .register import RegisterSupplyHistory

faker = Faker()


def test_register():
    """Testing register method"""

    supply_history_repository = SupplyHistoryRepositorySpy()
    register_supply_history = RegisterSupplyHistory(supply_history_repository)

    attributes = {
        "service_provided": faker.text(max_nb_chars=500),
        "hiring_manager": faker.name()[:100],
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history.register(**attributes)

    # Testing inputs
    assert (
        supply_history_repository.insert_supply_history_params["service_provided"]
        == attributes["service_provided"]
    )
    assert (
        supply_history_repository.insert_supply_history_params["hiring_manager"]
        == attributes["hiring_manager"]
    )
    assert (
        supply_history_repository.insert_supply_history_params["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_service_length():
    """Testing register with invalid service_provided length"""

    supply_history_repository = SupplyHistoryRepositorySpy()
    register_supply_history = RegisterSupplyHistory(supply_history_repository)

    attributes = {
        "service_provided": faker.text(max_nb_chars=6000),
        "hiring_manager": faker.name()[:100],
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history.register(**attributes)

    # Testing inputs
    assert supply_history_repository.insert_supply_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_manager_length():
    """Testing register with invalid hiring_manager length"""

    supply_history_repository = SupplyHistoryRepositorySpy()
    register_supply_history = RegisterSupplyHistory(supply_history_repository)

    attributes = {
        "service_provided": faker.text(max_nb_chars=500),
        "hiring_manager": faker.text(max_nb_chars=1500),
        "proposal_id": faker.uuid4(),
    }

    response = register_supply_history.register(**attributes)

    # Testing inputs
    assert supply_history_repository.insert_supply_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    supply_history_repository = SupplyHistoryRepositorySpy()
    register_supply_history = RegisterSupplyHistory(supply_history_repository)

    attributes = {
        "service_provided": faker.random_number(),
        "hiring_manager": faker.random_number(),
        "proposal_id": faker.random_number(),
    }

    response = register_supply_history.register(**attributes)

    # Testing inputs
    assert supply_history_repository.insert_supply_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
