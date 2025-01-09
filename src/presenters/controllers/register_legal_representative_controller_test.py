from faker import Faker
from src.data.test import RegisterLegalRepresentativeSpy
from src.infra.test import LegalRepresentativeRepositorySpy
from src.presenters.controllers import RegisterLegalRepresentativeController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterLegalRepresentative"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": faker.name()[:100],
        "cpf": faker.bothify(text="###.###.###-##")[:11],
        "email": faker.email()[:100],
        "position": faker.job()[:100],
        "proposal_id": faker.uuid4(),
        "summary": faker.text(),
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_legal_representative_use_case.register_param["name"]
        == attributes["name"]
    )
    assert (
        register_legal_representative_use_case.register_param["cpf"]
        == attributes["cpf"]
    )
    assert (
        register_legal_representative_use_case.register_param["email"]
        == attributes["email"]
    )
    assert (
        register_legal_representative_use_case.register_param["position"]
        == attributes["position"]
    )
    assert (
        register_legal_representative_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_legal_representative_use_case.register_param["summary"]
        == attributes["summary"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_without_summary():
    """Testing route without optional summary parameter"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": faker.name()[:100],
        "cpf": faker.bothify(text="###.###.###-##")[:11],
        "email": faker.email()[:100],
        "position": faker.job()[:100],
        "proposal_id": faker.uuid4(),
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_legal_representative_use_case.register_param["name"]
        == attributes["name"]
    )
    assert (
        register_legal_representative_use_case.register_param["cpf"]
        == attributes["cpf"]
    )
    assert (
        register_legal_representative_use_case.register_param["email"]
        == attributes["email"]
    )
    assert (
        register_legal_representative_use_case.register_param["position"]
        == attributes["position"]
    )
    assert (
        register_legal_representative_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert register_legal_representative_use_case.register_param["summary"] is None

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_missing_required_params():
    """Testing route with missing required parameters"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": faker.name(),
        "email": faker.email(),
        # Missing cpf, position and proposal_id
        "summary": faker.text(),
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_email():
    """Testing route with invalid email format"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": faker.name(),
        "cpf": faker.bothify(text="###.###.###-##"),
        "email": "invalid_email",
        "position": faker.job(),
        "proposal_id": faker.uuid4(),
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_cpf():
    """Testing route with invalid CPF format"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": faker.name(),
        "cpf": faker.text(max_nb_chars=150),
        "email": faker.email(),
        "position": faker.job(),
        "proposal_id": faker.uuid4(),
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_invalid_proposal_id():
    """Testing route with invalid proposal_id format"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": faker.name(),
        "cpf": faker.bothify(text="###.###.###-##"),
        "email": faker.email(),
        "position": faker.job(),
        "proposal_id": -1,
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    response = register_legal_representative_route.route(HttpRequest())

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    response = register_legal_representative_route.route(HttpRequest(body={}))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_required_params():
    """Testing route with empty required parameters"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": "",
        "cpf": "",
        "email": "",
        "position": "",
        "proposal_id": "",
        "summary": faker.text(),
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in text fields"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": "Name@#$%",
        "cpf": faker.bothify(text="###.###.###-##"),
        "email": faker.email(),
        "position": "Position@#$%",
        "proposal_id": faker.uuid4(),
        "summary": "Summary@#$%",
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_long_text():
    """Testing route with very long text in fields"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": faker.text(max_nb_chars=500),
        "cpf": faker.bothify(text="###.###.###-##"),
        "email": faker.email(),
        "position": faker.text(max_nb_chars=500),
        "proposal_id": faker.uuid4(),
        "summary": faker.text(max_nb_chars=1000),
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_whitespace_only():
    """Testing route with whitespace-only in optional fields"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": faker.name(),
        "cpf": faker.bothify(text="###.###.###-##"),
        "email": faker.email(),
        "position": faker.job(),
        "proposal_id": faker.uuid4(),
        "summary": "    ",
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_html_content():
    """Testing route with HTML content in text fields"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": "<p>Test Name</p>",
        "cpf": faker.bothify(text="###.###.###-##"),
        "email": faker.email(),
        "position": "<strong>Test Position</strong>",
        "proposal_id": faker.uuid4(),
        "summary": "<div>Test Summary</div>",
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_numeric_values():
    """Testing route with numeric values in text fields"""

    register_legal_representative_use_case = RegisterLegalRepresentativeSpy(
        LegalRepresentativeRepositorySpy()
    )
    register_legal_representative_route = RegisterLegalRepresentativeController(
        register_legal_representative_use_case=register_legal_representative_use_case
    )

    attributes = {
        "name": "12345",
        "cpf": faker.bothify(text="###.###.###-##"),
        "email": faker.email(),
        "position": "67890",
        "proposal_id": faker.uuid4(),
        "summary": "11223",
    }

    response = register_legal_representative_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_legal_representative_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body
