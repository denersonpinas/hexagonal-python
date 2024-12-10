from faker import Faker
from src.data.test import FindAbginvestTpprojLeiContrpartSpy
from src.infra.test import AbginvestTpprojLeiContrpartRepositorySpy
from src.presenters.helpers import HttpRequest
from src.presenters.controllers import FindAbginvestTpprojLeiContrpartController

faker = Faker()


def test_route_by_id():
    """Testing Route by id method"""

    find_abginvest_tpproj_lei_contrpart_use_case = FindAbginvestTpprojLeiContrpartSpy(
        AbginvestTpprojLeiContrpartRepositorySpy()
    )
    find_abginvest_tpproj_lei_contrpart_controller = FindAbginvestTpprojLeiContrpartController(
        find_abginvest_tpproj_lei_contrpart_use_case=find_abginvest_tpproj_lei_contrpart_use_case
    )
    http_request = HttpRequest(
        query={
            "id": faker.random_number(digits=5),
        }
    )

    response = find_abginvest_tpproj_lei_contrpart_controller.route(
        http_request=http_request
    )

    # Testing Inputs
    assert (
        find_abginvest_tpproj_lei_contrpart_use_case.by_id_param["id"]
        == http_request.query["id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_by_abginvest_tpproj_lei():
    """Testing Route by abginvest_tpproj_lei method"""

    find_abginvest_tpproj_lei_contrpart_use_case = FindAbginvestTpprojLeiContrpartSpy(
        AbginvestTpprojLeiContrpartRepositorySpy()
    )
    find_abginvest_tpproj_lei_contrpart_controller = FindAbginvestTpprojLeiContrpartController(
        find_abginvest_tpproj_lei_contrpart_use_case=find_abginvest_tpproj_lei_contrpart_use_case
    )
    http_request = HttpRequest(
        query={
            "abginvest_tpproj_lei_id": faker.random_number(digits=5),
        }
    )

    response = find_abginvest_tpproj_lei_contrpart_controller.route(
        http_request=http_request
    )

    # Testing Inputs
    assert (
        find_abginvest_tpproj_lei_contrpart_use_case.by_abginvest_tpproj_lei_param[
            "abginvest_tpproj_lei_id"
        ]
        == http_request.query["abginvest_tpproj_lei_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_all():
    """Testing Route by id and default method"""

    find_abginvest_tpproj_lei_contrpart_use_case = FindAbginvestTpprojLeiContrpartSpy(
        AbginvestTpprojLeiContrpartRepositorySpy()
    )
    find_abginvest_tpproj_lei_contrpart_controller = FindAbginvestTpprojLeiContrpartController(
        find_abginvest_tpproj_lei_contrpart_use_case=find_abginvest_tpproj_lei_contrpart_use_case
    )
    http_request = HttpRequest(query={})

    response = find_abginvest_tpproj_lei_contrpart_controller.route(
        http_request=http_request
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing Route method fail"""

    find_abginvest_tpproj_lei_contrpart_use_case = FindAbginvestTpprojLeiContrpartSpy(
        AbginvestTpprojLeiContrpartRepositorySpy()
    )
    find_abginvest_tpproj_lei_contrpart_controller = FindAbginvestTpprojLeiContrpartController(
        find_abginvest_tpproj_lei_contrpart_use_case=find_abginvest_tpproj_lei_contrpart_use_case
    )
    http_request = HttpRequest(query={"other_query": faker.word()})

    response = find_abginvest_tpproj_lei_contrpart_controller.route(
        http_request=http_request
    )

    # Testing Inputs
    assert find_abginvest_tpproj_lei_contrpart_use_case.by_id_param == {}
    assert (
        find_abginvest_tpproj_lei_contrpart_use_case.by_abginvest_tpproj_lei_param == {}
    )

    # Testing Output
    assert response.status_code == 422
    assert response.body
