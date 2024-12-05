from faker import Faker
from src.data.test import FindAbginvestTpprojLeiSpy
from src.infra.test import AbginvestTpprojLeiRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_abginvest_tpproj_lei_controller import FindAbginvestTpprojLeiController

faker = Faker()


def test_route_by_id():
    """Testing Route by id method"""

    find_abginvest_tpproj_lei_use_case = FindAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    find_abginvest_tpproj_lei_controller = FindAbginvestTpprojLeiController(
        find_abginvest_tpproj_lei_use_case=find_abginvest_tpproj_lei_use_case
    )
    http_request = HttpRequest(
        query={
            "id": faker.random_number(digits=5),
        }
    )

    response = find_abginvest_tpproj_lei_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_abginvest_tpproj_lei_use_case.by_id_param["id"] == http_request.query["id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_by_investment_approach():
    """Testing Route by investment approach id method"""

    find_abginvest_tpproj_lei_use_case = FindAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    find_abginvest_tpproj_lei_controller = FindAbginvestTpprojLeiController(
        find_abginvest_tpproj_lei_use_case=find_abginvest_tpproj_lei_use_case
    )
    http_request = HttpRequest(
        query={
            "investment_approach_id": faker.random_number(digits=5),
        }
    )

    response = find_abginvest_tpproj_lei_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_abginvest_tpproj_lei_use_case.by_investment_approach_param[
            "investment_approach_id"
        ]
        == http_request.query["investment_approach_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_by_type_project():
    """Testing Route by type project id method"""

    find_abginvest_tpproj_lei_use_case = FindAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    find_abginvest_tpproj_lei_controller = FindAbginvestTpprojLeiController(
        find_abginvest_tpproj_lei_use_case=find_abginvest_tpproj_lei_use_case
    )
    http_request = HttpRequest(
        query={
            "type_project_id": faker.random_number(digits=5),
        }
    )

    response = find_abginvest_tpproj_lei_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_abginvest_tpproj_lei_use_case.by_type_project_param["type_project_id"]
        == http_request.query["type_project_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_by_law():
    """Testing Route by law id method"""

    find_abginvest_tpproj_lei_use_case = FindAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    find_abginvest_tpproj_lei_controller = FindAbginvestTpprojLeiController(
        find_abginvest_tpproj_lei_use_case=find_abginvest_tpproj_lei_use_case
    )
    http_request = HttpRequest(
        query={
            "law_id": faker.random_number(digits=5),
        }
    )

    response = find_abginvest_tpproj_lei_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_abginvest_tpproj_lei_use_case.by_law_param["law_id"]
        == http_request.query["law_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_all():
    """Testing Route by id and default method"""

    find_abginvest_tpproj_lei_use_case = FindAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    find_abginvest_tpproj_lei_controller = FindAbginvestTpprojLeiController(
        find_abginvest_tpproj_lei_use_case=find_abginvest_tpproj_lei_use_case
    )
    http_request = HttpRequest(query={})

    response = find_abginvest_tpproj_lei_controller.route(http_request=http_request)

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing Route method fail"""

    find_abginvest_tpproj_lei_use_case = FindAbginvestTpprojLeiSpy(
        AbginvestTpprojLeiRepositorySpy()
    )
    find_abginvest_tpproj_lei_controller = FindAbginvestTpprojLeiController(
        find_abginvest_tpproj_lei_use_case=find_abginvest_tpproj_lei_use_case
    )
    http_request = HttpRequest(query={"other_query": faker.word()})

    response = find_abginvest_tpproj_lei_controller.route(http_request=http_request)

    # Testing Inputs
    assert find_abginvest_tpproj_lei_use_case.by_id_param == {}
    assert find_abginvest_tpproj_lei_use_case.by_investment_approach_param == {}
    assert find_abginvest_tpproj_lei_use_case.by_type_project_param == {}
    assert find_abginvest_tpproj_lei_use_case.by_law_param == {}

    # Testing Output
    assert response.status_code == 422
    assert response.body
