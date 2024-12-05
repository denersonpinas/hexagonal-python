from faker import Faker

from src.data.test import RegisterAbginvestTpprojLeiSpy
from src.infra.test import AbginvestTpprojLeiRepositorySpy
from src.presenters.controllers import RegisterAbginvestTpprojLeiController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterAbginvestTpprojLeiRoute"""

    register_abginvest_tpproj_lei_use_case = RegisterAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    register_counterpart_route = RegisterAbginvestTpprojLeiController(
        register_abginvest_tpproj_lei_use_case=register_abginvest_tpproj_lei_use_case
    )

    attributer = {
        "investment_approach_id": faker.random_number(digits=5),
        "type_project_id": faker.random_number(digits=5),
        "law_id": faker.random_number(digits=5),
    }

    response = register_counterpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_abginvest_tpproj_lei_use_case.register_param["investment_approach_id"]
        == attributer["investment_approach_id"]
    )
    assert (
        register_abginvest_tpproj_lei_use_case.register_param["type_project_id"]
        == attributer["type_project_id"]
    )
    assert (
        register_abginvest_tpproj_lei_use_case.register_param["law_id"]
        == attributer["law_id"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_abginvest_tpproj_lei_use_case = RegisterAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    register_counterpart_route = RegisterAbginvestTpprojLeiController(
        register_abginvest_tpproj_lei_use_case=register_abginvest_tpproj_lei_use_case
    )

    attributer = {
        "investment_approach_id": faker.word(),
        "type_project_id": faker.word(),
        "law_id": faker.word(),
    }

    response = register_counterpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_abginvest_tpproj_lei_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_abginvest_tpproj_lei_use_case = RegisterAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    register_counterpart_route = RegisterAbginvestTpprojLeiController(
        register_abginvest_tpproj_lei_use_case=register_abginvest_tpproj_lei_use_case
    )

    response = register_counterpart_route.route(HttpRequest())

    # Testing input
    assert register_abginvest_tpproj_lei_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
