from faker import Faker
from src.infra.test import ProponentRepositorySpy
from .register import RegisterProponent

faker = Faker("pt_BR")


def test_register():
    """Testing register method with all fields"""

    proponent_repository = ProponentRepositorySpy()
    register_proponent = RegisterProponent(proponent_repository)

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.company()[:200],
        "trade_name": faker.company()[:200],
        "zip_code": faker.numerify(text="#" * 8),
        "state": faker.city_suffix()[:2],
        "city": faker.city()[:100],
        "neighborhood": faker.street_name()[:100],
        "street": faker.street_name()[:100],
        "number": faker.random_int(min=1),
        "complement": faker.text(max_nb_chars=100),
        "website": faker.url()[:100],
        "social_media": faker.url()[:100],
        "curriculum_summary": faker.text(max_nb_chars=500),
    }

    response = register_proponent.register(**attributes)

    # Testing inputs
    assert proponent_repository.insert_proponent_params == attributes

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_only_required():
    """Testing register method with only required fields"""

    proponent_repository = ProponentRepositorySpy()
    register_proponent = RegisterProponent(proponent_repository)

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.company()[:200],
    }

    response = register_proponent.register(**attributes)

    # Testing inputs
    assert proponent_repository.insert_proponent_params["cnpj"] == attributes["cnpj"]
    assert (
        proponent_repository.insert_proponent_params["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        proponent_repository.insert_proponent_params["company_name"]
        == attributes["company_name"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_invalid_lengths():
    """Testing register with invalid field lengths"""

    proponent_repository = ProponentRepositorySpy()
    register_proponent = RegisterProponent(proponent_repository)

    attributes = {
        "cnpj": faker.numerify(text="#" * 15),
        "proposal_id": faker.uuid4(),
        "company_name": faker.text(max_nb_chars=250),
        "zip_code": faker.numerify(text="#" * 9),
        "state": faker.estado(),
    }

    response = register_proponent.register(**attributes)

    # Testing inputs
    assert proponent_repository.insert_proponent_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    proponent_repository = ProponentRepositorySpy()
    register_proponent = RegisterProponent(proponent_repository)

    attributes = {
        "cnpj": faker.random_number(),
        "proposal_id": faker.random_number(),
        "company_name": faker.random_number(),
    }

    response = register_proponent.register(**attributes)

    # Testing inputs
    assert proponent_repository.insert_proponent_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
