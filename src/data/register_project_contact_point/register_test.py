from faker import Faker
from uuid import uuid4
from src.infra.test import ProjectContactPointRepositorySpy
from .register import RegisterProjectContactPoint

faker = Faker()


def test_register():
    """Testing register method"""

    project_contact_point_repository = ProjectContactPointRepositorySpy()
    register_project_contact = RegisterProjectContactPoint(
        project_contact_point_repository
    )

    attributes = {
        "name": faker.name()[:100],
        "email": faker.email()[:100],
        "position": faker.job()[:100],
        "proposal_id": uuid4(),
    }

    response = register_project_contact.register(**attributes)

    # Testing inputs
    assert (
        project_contact_point_repository.insert_project_contact_params["name"]
        == attributes["name"]
    )
    assert (
        project_contact_point_repository.insert_project_contact_params["email"]
        == attributes["email"]
    )
    assert (
        project_contact_point_repository.insert_project_contact_params["position"]
        == attributes["position"]
    )
    assert (
        project_contact_point_repository.insert_project_contact_params["proposal_id"]
        == attributes["proposal_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_name_length():
    """Testing register with invalid name length"""

    project_contact_point_repository = ProjectContactPointRepositorySpy()
    register_project_contact = RegisterProjectContactPoint(
        project_contact_point_repository
    )

    attributes = {
        "name": faker.text(max_nb_chars=1500),
        "email": faker.email()[:100],
        "position": faker.job()[:100],
        "proposal_id": uuid4(),
    }

    response = register_project_contact.register(**attributes)

    # Testing inputs
    assert project_contact_point_repository.insert_project_contact_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_email():
    """Testing register with invalid email"""

    project_contact_point_repository = ProjectContactPointRepositorySpy()
    register_project_contact = RegisterProjectContactPoint(
        project_contact_point_repository
    )

    attributes = {
        "name": faker.name()[:100],
        "email": "invalid_email",
        "position": faker.job()[:100],
        "proposal_id": uuid4(),
    }

    response = register_project_contact.register(**attributes)

    # Testing inputs
    assert project_contact_point_repository.insert_project_contact_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_lengths():
    """Testing register with invalid field lengths"""

    project_contact_point_repository = ProjectContactPointRepositorySpy()
    register_project_contact = RegisterProjectContactPoint(
        project_contact_point_repository
    )

    attributes = {
        "name": faker.text(max_nb_chars=1500),
        "email": faker.email()[:1500],
        "position": faker.text(max_nb_chars=1500),
        "proposal_id": uuid4(),
    }

    response = register_project_contact.register(**attributes)

    # Testing inputs
    assert project_contact_point_repository.insert_project_contact_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    project_contact_point_repository = ProjectContactPointRepositorySpy()
    register_project_contact = RegisterProjectContactPoint(
        project_contact_point_repository
    )

    attributes = {
        "name": faker.random_number(),
        "email": faker.random_number(),
        "position": faker.random_number(),
        "proposal_id": faker.name(),
    }

    response = register_project_contact.register(**attributes)

    # Testing inputs
    assert project_contact_point_repository.insert_project_contact_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
