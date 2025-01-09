from faker import Faker
import uuid
from src.data.test import RegisterProposalFileSpy
from src.infra.test import ProposalFileRepositorySpy
from src.presenters.controllers import RegisterProposalFileController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposalFile"""

    register_proposal_file_use_case = RegisterProposalFileSpy(
        ProposalFileRepositorySpy()
    )
    register_proposal_file_route = RegisterProposalFileController(
        register_proposal_file_use_case=register_proposal_file_use_case
    )

    attributes = {
        "name": faker.file_name()[:100],
        "extension": faker.file_extension()[:10],
        "size": faker.random_int(min=1000, max=10000000),
        "uri": faker.uri()[:500],
        "proposal_id": uuid.uuid4(),
        "type_id": faker.file_name()[:100],
    }

    response = register_proposal_file_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_file_use_case.register_param["name"] == attributes["name"]
    assert (
        register_proposal_file_use_case.register_param["extension"]
        == attributes["extension"]
    )
    assert register_proposal_file_use_case.register_param["size"] == attributes["size"]
    assert register_proposal_file_use_case.register_param["uri"] == attributes["uri"]
    assert (
        register_proposal_file_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proposal_file_use_case.register_param["type_id"]
        == attributes["type_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_size():
    """Testing route with invalid size"""

    register_proposal_file_use_case = RegisterProposalFileSpy(
        ProposalFileRepositorySpy()
    )
    register_proposal_file_route = RegisterProposalFileController(
        register_proposal_file_use_case=register_proposal_file_use_case
    )

    attributes = {
        "name": faker.file_name(),
        "extension": faker.file_extension(),
        "size": "invalid_size",
        "uri": faker.uri(),
        "proposal_id": str(uuid.uuid4()),
        "type_id": faker.file_name()[:100],
    }

    response = register_proposal_file_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_file_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_proposal_id():
    """Testing route with invalid proposal_id"""

    register_proposal_file_use_case = RegisterProposalFileSpy(
        ProposalFileRepositorySpy()
    )
    register_proposal_file_route = RegisterProposalFileController(
        register_proposal_file_use_case=register_proposal_file_use_case
    )

    attributes = {
        "name": faker.file_name(),
        "extension": faker.file_extension(),
        "size": faker.random_int(min=1000, max=10000000),
        "uri": faker.uri(),
        "proposal_id": "invalid_uuid",
        "type_id": faker.file_name()[:100],
    }

    response = register_proposal_file_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_file_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_params():
    """Testing route with missing parameters"""

    register_proposal_file_use_case = RegisterProposalFileSpy(
        ProposalFileRepositorySpy()
    )
    register_proposal_file_route = RegisterProposalFileController(
        register_proposal_file_use_case=register_proposal_file_use_case
    )

    attributes = {
        "name": faker.file_name(),
        "extension": faker.file_extension(),
        # Missing other required parameters
        "uri": faker.uri(),
    }

    response = register_proposal_file_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_file_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_file_use_case = RegisterProposalFileSpy(
        ProposalFileRepositorySpy()
    )
    register_proposal_file_route = RegisterProposalFileController(
        register_proposal_file_use_case=register_proposal_file_use_case
    )

    response = register_proposal_file_route.route(HttpRequest())

    # Testing input
    assert register_proposal_file_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_proposal_file_use_case = RegisterProposalFileSpy(
        ProposalFileRepositorySpy()
    )
    register_proposal_file_route = RegisterProposalFileController(
        register_proposal_file_use_case=register_proposal_file_use_case
    )

    response = register_proposal_file_route.route(HttpRequest(body={}))

    # Testing input
    assert register_proposal_file_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_negative_size():
    """Testing route with negative size value"""

    register_proposal_file_use_case = RegisterProposalFileSpy(
        ProposalFileRepositorySpy()
    )
    register_proposal_file_route = RegisterProposalFileController(
        register_proposal_file_use_case=register_proposal_file_use_case
    )

    attributes = {
        "name": faker.file_name(),
        "extension": faker.file_extension(),
        "size": -1000,
        "uri": faker.uri(),
        "proposal_id": str(uuid.uuid4()),
        "type_id": faker.file_name()[:100],
    }

    response = register_proposal_file_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_file_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
