from faker import Faker
from src.data.test import RegisterProponentSpy
from src.infra.test import ProponentRepositorySpy
from src.presenters.controllers import RegisterProponentController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProponent"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

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

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param["cnpj"] == attributes["cnpj"]
    assert (
        register_proponent_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proponent_use_case.register_param["company_name"]
        == attributes["company_name"]
    )
    assert (
        register_proponent_use_case.register_param["trade_name"]
        == attributes["trade_name"]
    )
    assert (
        register_proponent_use_case.register_param["zip_code"] == attributes["zip_code"]
    )
    assert register_proponent_use_case.register_param["number"] == attributes["number"]

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_only_required_params():
    """Testing route with only required parameters"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.company()[:200],
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param["cnpj"] == attributes["cnpj"]
    assert (
        register_proponent_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proponent_use_case.register_param["company_name"]
        == attributes["company_name"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_invalid_number():
    """Testing route with invalid number parameter"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.company()[:200],
        "number": "invalid_number",
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_missing_required_params():
    """Testing route with missing required parameters"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        # Missing proposal_id and company_name
        "trade_name": faker.company()[:200],
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    response = register_proponent_route.route(HttpRequest())

    # Testing input
    assert register_proponent_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_body():
    """Testing route with empty body"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    response = register_proponent_route.route(HttpRequest(body={}))

    # Testing input
    assert register_proponent_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_with_empty_required_params():
    """Testing route with empty required parameters"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {"cnpj": "", "proposal_id": "", "company_name": ""}

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_invalid_urls():
    """Testing route with invalid website and social_media URLs"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.company()[:200],
        "website": "invalid_url",
        "social_media": "invalid_url",
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param["cnpj"] == attributes["cnpj"]
    assert (
        register_proponent_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proponent_use_case.register_param["company_name"]
        == attributes["company_name"]
    )
    assert (
        register_proponent_use_case.register_param["website"] == attributes["website"]
    )
    assert (
        register_proponent_use_case.register_param["social_media"]
        == attributes["social_media"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_special_characters():
    """Testing route with special characters in text fields"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": "Company@#$%",
        "trade_name": "Trade@#$%",
        "complement": "Complement@#$%",
        "curriculum_summary": "Summary@#$%",
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param["cnpj"] == attributes["cnpj"]
    assert (
        register_proponent_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proponent_use_case.register_param["company_name"]
        == attributes["company_name"]
    )
    assert (
        register_proponent_use_case.register_param["trade_name"]
        == attributes["trade_name"]
    )
    assert (
        register_proponent_use_case.register_param["complement"]
        == attributes["complement"]
    )
    assert (
        register_proponent_use_case.register_param["curriculum_summary"]
        == attributes["curriculum_summary"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_invalid_zip_code():
    """Testing route with invalid zip_code format"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.company()[:200],
        "zip_code": "invalid_zip",
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_long_text_fields():
    """Testing route with very long text in fields"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.text(max_nb_chars=5000),
        "trade_name": faker.text(max_nb_chars=5000),
        "complement": faker.text(max_nb_chars=5000),
        "curriculum_summary": faker.text(max_nb_chars=10000),
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_invalid_cnpj():
    """Testing route with invalid CNPJ format"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": "invalid_cnpj",
        "proposal_id": faker.uuid4(),
        "company_name": faker.company(),
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_numeric_text_fields():
    """Testing route with numeric values in text fields"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": "12345",
        "trade_name": "67890",
        "complement": "11223",
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param["cnpj"] == attributes["cnpj"]
    assert (
        register_proponent_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proponent_use_case.register_param["company_name"]
        == attributes["company_name"]
    )
    assert (
        register_proponent_use_case.register_param["trade_name"]
        == attributes["trade_name"]
    )
    assert (
        register_proponent_use_case.register_param["complement"]
        == attributes["complement"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_whitespace_only():
    """Testing route with whitespace-only values in optional fields"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.company(),
        "trade_name": "   ",
        "complement": "     ",
        "curriculum_summary": "    ",
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param["cnpj"] == attributes["cnpj"]
    assert (
        register_proponent_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proponent_use_case.register_param["company_name"]
        == attributes["company_name"]
    )
    assert (
        register_proponent_use_case.register_param["trade_name"]
        == attributes["trade_name"]
    )
    assert (
        register_proponent_use_case.register_param["complement"]
        == attributes["complement"]
    )
    assert (
        register_proponent_use_case.register_param["curriculum_summary"]
        == attributes["curriculum_summary"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_with_none_optional_params():
    """Testing route with None values in optional parameters"""

    register_proponent_use_case = RegisterProponentSpy(ProponentRepositorySpy())
    register_proponent_route = RegisterProponentController(
        register_proponent_use_case=register_proponent_use_case
    )

    attributes = {
        "cnpj": faker.numerify(text="#" * 14),
        "proposal_id": faker.uuid4(),
        "company_name": faker.company()[:200],
        "trade_name": None,
        "zip_code": None,
        "state": None,
        "city": None,
        "neighborhood": None,
        "street": None,
        "number": None,
        "complement": None,
        "website": None,
        "social_media": None,
        "curriculum_summary": None,
    }

    response = register_proponent_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proponent_use_case.register_param["cnpj"] == attributes["cnpj"]
    assert (
        register_proponent_use_case.register_param["proposal_id"]
        == attributes["proposal_id"]
    )
    assert (
        register_proponent_use_case.register_param["company_name"]
        == attributes["company_name"]
    )
    assert all(
        register_proponent_use_case.register_param[key] is None
        for key in [
            "trade_name",
            "zip_code",
            "state",
            "city",
            "neighborhood",
            "street",
            "number",
            "complement",
            "website",
            "social_media",
            "curriculum_summary",
        ]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body
