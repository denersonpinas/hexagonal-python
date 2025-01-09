from faker import Faker
from src.infra.test import GoalHistoryRepositorySpy
from .register import RegisterGoalHistory

faker = Faker()


def test_register():
    """Testing register method"""

    goal_history_repository = GoalHistoryRepositorySpy()
    register_goal_history = RegisterGoalHistory(goal_history_repository)

    attributes = {
        "expected": faker.text(max_nb_chars=500),
        "achieved": faker.text(max_nb_chars=500),
        "project_history_id": faker.random_int(min=1),
    }

    response = register_goal_history.register(**attributes)

    # Testing inputs
    assert (
        goal_history_repository.insert_goal_history_params["expected"]
        == attributes["expected"]
    )
    assert (
        goal_history_repository.insert_goal_history_params["achieved"]
        == attributes["achieved"]
    )
    assert (
        goal_history_repository.insert_goal_history_params["project_history_id"]
        == attributes["project_history_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_lengths():
    """Testing register with invalid text lengths"""

    goal_history_repository = GoalHistoryRepositorySpy()
    register_goal_history = RegisterGoalHistory(goal_history_repository)

    attributes = {
        "expected": faker.text(max_nb_chars=6000),
        "achieved": faker.text(max_nb_chars=6000),
        "project_history_id": faker.random_int(min=1),
    }

    response = register_goal_history.register(**attributes)

    # Testing inputs
    assert goal_history_repository.insert_goal_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_project_history_id():
    """Testing register with invalid project history id"""

    goal_history_repository = GoalHistoryRepositorySpy()
    register_goal_history = RegisterGoalHistory(goal_history_repository)

    attributes = {
        "expected": faker.text(max_nb_chars=500),
        "achieved": faker.text(max_nb_chars=500),
        "project_history_id": 0,
    }

    response = register_goal_history.register(**attributes)

    # Testing inputs
    assert goal_history_repository.insert_goal_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    goal_history_repository = GoalHistoryRepositorySpy()
    register_goal_history = RegisterGoalHistory(goal_history_repository)

    attributes = {
        "expected": faker.random_number(),
        "achieved": faker.random_number(),
        "project_history_id": faker.name(),
    }

    response = register_goal_history.register(**attributes)

    # Testing inputs
    assert goal_history_repository.insert_goal_history_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
