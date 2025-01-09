from faker import Faker
from uuid import uuid4
from src.infra.test import ProjectHistoryRepositorySpy
from .register import RegisterProjectHistory

faker = Faker()


def test_register():
    """Testing register method"""

    project_history_repository = ProjectHistoryRepositorySpy()
    register_project_history = RegisterProjectHistory(project_history_repository)

    attributes = {
        "investment_year": faker.random_int(min=1901, max=2023),
        "title": faker.sentence()[:100],
        "investment_type": faker.word()[:50],
        "proposal_id": uuid4(),
    }

    response = register_project_history.register(**attributes)

    # Testing inputs
    assert (
        project_history_repository.insert_project_history_params["investment_year"]
        == attributes["investment_year"]
    )
    assert (
        project_history_repository.insert_project_history_params["title"]
        == attributes["title"]
    )
    assert (
        project_history_repository.insert_project_history_params["investment_type"]
        == attributes["investment_type"]
    )
    assert (
        project_history_repository.insert_project_history_params["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_year():
    """Testing register with invalid investment year"""

    project_history_repository = ProjectHistoryRepositorySpy()
    register_project_history = RegisterProjectHistory(project_history_repository)

    attributes = {
        "investment_year": 1800,
        "title": faker.sentence()[:100],
        "investment_type": faker.word()[:50],
        "proposal_id": uuid4(),
    }

    response = register_project_history.register(**attributes)

    # Testing inputs
    assert project_history_repository.insert_project_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_lengths():
    """Testing register with invalid string lengths"""

    project_history_repository = ProjectHistoryRepositorySpy()
    register_project_history = RegisterProjectHistory(project_history_repository)

    attributes = {
        "investment_year": faker.random_int(min=1901, max=2023),
        "title": faker.text(max_nb_chars=1500),
        "investment_type": faker.text(max_nb_chars=1000),
        "proposal_id": uuid4(),
    }

    response = register_project_history.register(**attributes)

    # Testing inputs
    assert project_history_repository.insert_project_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    project_history_repository = ProjectHistoryRepositorySpy()
    register_project_history = RegisterProjectHistory(project_history_repository)

    attributes = {
        "investment_year": faker.name(),
        "title": faker.random_number(),
        "investment_type": faker.random_number(),
        "proposal_id": faker.name(),
    }

    response = register_project_history.register(**attributes)

    # Testing inputs
    assert project_history_repository.insert_project_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
