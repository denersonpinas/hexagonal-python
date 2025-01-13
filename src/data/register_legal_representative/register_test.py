import uuid
from faker import Faker
from src.infra.test import LegalRepresentativeRepositorySpy
from .register import RegisterLegalRepresentative

faker = Faker("pt_BR")


def test_register():
    """Testing register method with all fields"""

    legal_representative_repository = LegalRepresentativeRepositorySpy()
    register_legal_representative = RegisterLegalRepresentative(
        legal_representative_repository
    )

    attributes = {
        "name": faker.name()[:100],
        "cpf": faker.numerify(text="#" * 11),
        "email": faker.email()[:100],
        "position": faker.job()[:100],
        "proposal_id": uuid.uuid4(),
        "summary": faker.text(max_nb_chars=500),
    }

    response = register_legal_representative.register(**attributes)

    # Testing inputs
    assert (
        legal_representative_repository.insert_legal_representative_params == attributes
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_only_required():
    """Testing register method with only required fields"""

    legal_representative_repository = LegalRepresentativeRepositorySpy()
    register_legal_representative = RegisterLegalRepresentative(
        legal_representative_repository
    )

    attributes = {
        "name": faker.name()[:100],
        "cpf": faker.numerify(text="#" * 11),
        "email": faker.email()[:100],
        "position": faker.job()[:100],
        "proposal_id": uuid.uuid4(),
    }

    response = register_legal_representative.register(**attributes)

    # Testing inputs
    assert (
        legal_representative_repository.insert_legal_representative_params["name"]
        == attributes["name"]
    )
    assert (
        legal_representative_repository.insert_legal_representative_params["cpf"]
        == attributes["cpf"]
    )
    assert (
        legal_representative_repository.insert_legal_representative_params["email"]
        == attributes["email"]
    )
    assert (
        legal_representative_repository.insert_legal_representative_params["position"]
        == attributes["position"]
    )
    assert (
        legal_representative_repository.insert_legal_representative_params[
            "proposal_id"
        ]
        == attributes["proposal_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_lengths():
    """Testing register with invalid field lengths"""

    legal_representative_repository = LegalRepresentativeRepositorySpy()
    register_legal_representative = RegisterLegalRepresentative(
        legal_representative_repository
    )

    attributes = {
        "name": faker.text(max_nb_chars=150),
        "cpf": faker.numerify(text="#" * 12),
        "email": faker.email()[:150],
        "position": faker.text(max_nb_chars=150),
        "proposal_id": faker.uuid4(),
        "summary": faker.text(max_nb_chars=600),
    }

    response = register_legal_representative.register(**attributes)

    # Testing inputs
    assert legal_representative_repository.insert_legal_representative_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_email():
    """Testing register with invalid email"""

    legal_representative_repository = LegalRepresentativeRepositorySpy()
    register_legal_representative = RegisterLegalRepresentative(
        legal_representative_repository
    )

    attributes = {
        "name": faker.name()[:100],
        "cpf": faker.numerify(text="#" * 11),
        "email": "invalid_email",
        "position": faker.job()[:100],
        "proposal_id": faker.uuid4(),
    }

    response = register_legal_representative.register(**attributes)

    # Testing inputs
    assert legal_representative_repository.insert_legal_representative_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    legal_representative_repository = LegalRepresentativeRepositorySpy()
    register_legal_representative = RegisterLegalRepresentative(
        legal_representative_repository
    )

    attributes = {
        "name": faker.random_number(),
        "cpf": faker.random_number(),
        "email": faker.random_number(),
        "position": faker.random_number(),
        "proposal_id": faker.random_number(),
        "summary": faker.random_number(),
    }

    response = register_legal_representative.register(**attributes)

    # Testing inputs
    assert legal_representative_repository.insert_legal_representative_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_invalid_cpf():
    """Testing register with invalid CPF length"""

    legal_representative_repository = LegalRepresentativeRepositorySpy()
    register_legal_representative = RegisterLegalRepresentative(
        legal_representative_repository
    )

    attributes = {
        "name": faker.name()[:100],
        "cpf": faker.numerify(text="#" * 10),  # CPF with 10 digits instead of 11
        "email": faker.email()[:100],
        "position": faker.job()[:100],
        "proposal_id": faker.uuid4(),
    }

    response = register_legal_representative.register(**attributes)

    # Testing inputs
    assert legal_representative_repository.insert_legal_representative_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
