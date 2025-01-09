from faker import Faker
from src.data.test import RegisterGoalHistorySpy
from src.infra.test import GoalHistoryRepositorySpy
from src.presenters.controllers import RegisterGoalHistoryController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterGoalHistory"""

    register_goal_history_use_case = RegisterGoalHistorySpy(GoalHistoryRepositorySpy())
    register_goal_history_route = RegisterGoalHistoryController(
        register_goal_history_use_case=register_goal_history_use_case
    )

    attributes = {
        "expected": faker.text(max_nb_chars=200),
        "achieved": faker.text(max_nb_chars=200),
        "project_history_id": faker.random_int(min=1, max=1000),
    }

    response = register_goal_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_goal_history_use_case.register_param["expected"]
        == attributes["expected"]
    )
    assert (
        register_goal_history_use_case.register_param["achieved"]
        == attributes["achieved"]
    )
    assert (
        register_goal_history_use_case.register_param["project_history_id"]
        == attributes["project_history_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_project_history_id():
    """Testing route with invalid project_history_id"""

    register_goal_history_use_case = RegisterGoalHistorySpy(GoalHistoryRepositorySpy())
    register_goal_history_route = RegisterGoalHistoryController(
        register_goal_history_use_case=register_goal_history_use_case
    )

    attributes = {
        "expected": faker.text(),
        "achieved": faker.text(),
        "project_history_id": "invalid_id",
    }

    response = register_goal_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_goal_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_goal_history_use_case = RegisterGoalHistorySpy(GoalHistoryRepositorySpy())
    register_goal_history_route = RegisterGoalHistoryController(
        register_goal_history_use_case=register_goal_history_use_case
    )

    attributes = {
        "expected": faker.text(),
        # Missing achieved and project_history_id
    }

    response = register_goal_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_goal_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_goal_history_use_case = RegisterGoalHistorySpy(GoalHistoryRepositorySpy())
    register_goal_history_route = RegisterGoalHistoryController(
        register_goal_history_use_case=register_goal_history_use_case
    )

    response = register_goal_history_route.route(HttpRequest())

    # Testing input
    assert register_goal_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_goal_history_use_case = RegisterGoalHistorySpy(GoalHistoryRepositorySpy())
    register_goal_history_route = RegisterGoalHistoryController(
        register_goal_history_use_case=register_goal_history_use_case
    )

    response = register_goal_history_route.route(HttpRequest(body={}))

    # Testing input
    assert register_goal_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_params():
    """Testing route with empty parameters"""

    register_goal_history_use_case = RegisterGoalHistorySpy(GoalHistoryRepositorySpy())
    register_goal_history_route = RegisterGoalHistoryController(
        register_goal_history_use_case=register_goal_history_use_case
    )

    attributes = {
        "expected": "",
        "achieved": "",
        "project_history_id": faker.random_int(min=1, max=1000),
    }

    response = register_goal_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_goal_history_use_case.register_param["expected"]
        == attributes["expected"]
    )
    assert (
        register_goal_history_use_case.register_param["achieved"]
        == attributes["achieved"]
    )
    assert (
        register_goal_history_use_case.register_param["project_history_id"]
        == attributes["project_history_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in text fields"""

    register_goal_history_use_case = RegisterGoalHistorySpy(GoalHistoryRepositorySpy())
    register_goal_history_route = RegisterGoalHistoryController(
        register_goal_history_use_case=register_goal_history_use_case
    )

    attributes = {
        "expected": "Expected@#$%",
        "achieved": "Achieved@#$%",
        "project_history_id": faker.random_int(min=1, max=1000),
    }

    response = register_goal_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_goal_history_use_case.register_param["expected"]
        == attributes["expected"]
    )
    assert (
        register_goal_history_use_case.register_param["achieved"]
        == attributes["achieved"]
    )
    assert (
        register_goal_history_use_case.register_param["project_history_id"]
        == attributes["project_history_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_long_text():
    """Testing route with very long text in fields"""

    register_goal_history_use_case = RegisterGoalHistorySpy(GoalHistoryRepositorySpy())
    register_goal_history_route = RegisterGoalHistoryController(
        register_goal_history_use_case=register_goal_history_use_case
    )

    attributes = {
        "expected": faker.text(max_nb_chars=1000),
        "achieved": faker.text(max_nb_chars=1000),
        "project_history_id": faker.random_int(min=1, max=1000),
    }

    response = register_goal_history_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_goal_history_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
