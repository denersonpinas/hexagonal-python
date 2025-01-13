from faker import Faker
import uuid
from src.data.test import RegisterProjectContactPointSpy
from src.infra.test import ProjectContactPointRepositorySpy
from src.presenters.controllers import RegisterProjectContactPointController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProjectContactPoint"""

    register_project_contact_point_use_case = RegisterProjectContactPointSpy(
        ProjectContactPointRepositorySpy()
    )
    register_project_contact_point_route = RegisterProjectContactPointController(
        register_project_contact_point_use_case=register_project_contact_point_use_case
    )

    attributes = {
        "name": faker.name(),
        "email": faker.email(),
        "position": faker.job(),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_contact_point_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_contact_point_use_case.register_param["name"]
        == attributes["name"]
    )
    assert (
        register_project_contact_point_use_case.register_param["email"]
        == attributes["email"]
    )
    assert (
        register_project_contact_point_use_case.register_param["position"]
        == attributes["position"]
    )
    assert (
        register_project_contact_point_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_email():
    """Testing route with invalid email format"""

    register_project_contact_point_use_case = RegisterProjectContactPointSpy(
        ProjectContactPointRepositorySpy()
    )
    register_project_contact_point_route = RegisterProjectContactPointController(
        register_project_contact_point_use_case=register_project_contact_point_use_case
    )

    attributes = {
        "name": faker.name(),
        "email": "invalid_email",
        "position": faker.job(),
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_contact_point_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_contact_point_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_proposal_id():
    """Testing route with invalid proposal_id"""

    register_project_contact_point_use_case = RegisterProjectContactPointSpy(
        ProjectContactPointRepositorySpy()
    )
    register_project_contact_point_route = RegisterProjectContactPointController(
        register_project_contact_point_use_case=register_project_contact_point_use_case
    )

    attributes = {
        "name": faker.name(),
        "email": faker.email(),
        "position": faker.job(),
        "proposal_id": "invalid_uuid",
    }

    response = register_project_contact_point_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_contact_point_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_project_contact_point_use_case = RegisterProjectContactPointSpy(
        ProjectContactPointRepositorySpy()
    )
    register_project_contact_point_route = RegisterProjectContactPointController(
        register_project_contact_point_use_case=register_project_contact_point_use_case
    )

    attributes = {
        "name": faker.name(),
        "email": faker.email(),
        # Missing position and proposal_id
    }

    response = register_project_contact_point_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_contact_point_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_project_contact_point_use_case = RegisterProjectContactPointSpy(
        ProjectContactPointRepositorySpy()
    )
    register_project_contact_point_route = RegisterProjectContactPointController(
        register_project_contact_point_use_case=register_project_contact_point_use_case
    )

    response = register_project_contact_point_route.route(HttpRequest())

    # Testing input
    assert register_project_contact_point_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_project_contact_point_use_case = RegisterProjectContactPointSpy(
        ProjectContactPointRepositorySpy()
    )
    register_project_contact_point_route = RegisterProjectContactPointController(
        register_project_contact_point_use_case=register_project_contact_point_use_case
    )

    response = register_project_contact_point_route.route(HttpRequest(body={}))

    # Testing input
    assert register_project_contact_point_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_params():
    """Testing route with empty parameters"""

    register_project_contact_point_use_case = RegisterProjectContactPointSpy(
        ProjectContactPointRepositorySpy()
    )
    register_project_contact_point_route = RegisterProjectContactPointController(
        register_project_contact_point_use_case=register_project_contact_point_use_case
    )

    attributes = {
        "name": "",
        "email": "",
        "position": "",
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_contact_point_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_project_contact_point_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in text fields"""

    register_project_contact_point_use_case = RegisterProjectContactPointSpy(
        ProjectContactPointRepositorySpy()
    )
    register_project_contact_point_route = RegisterProjectContactPointController(
        register_project_contact_point_use_case=register_project_contact_point_use_case
    )

    attributes = {
        "name": "Name@#$%",
        "email": faker.email(),
        "position": "Position@#$%",
        "proposal_id": uuid.uuid4(),
    }

    response = register_project_contact_point_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_project_contact_point_use_case.register_param["name"]
        == attributes["name"]
    )
    assert (
        register_project_contact_point_use_case.register_param["email"]
        == attributes["email"]
    )
    assert (
        register_project_contact_point_use_case.register_param["position"]
        == attributes["position"]
    )
    assert (
        register_project_contact_point_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body
