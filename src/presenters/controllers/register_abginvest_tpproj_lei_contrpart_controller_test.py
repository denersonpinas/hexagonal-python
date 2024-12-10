from faker import Faker

from src.data.test import RegisterAbginvestTpprojLeiContrpartSpy
from src.infra.test import AbginvestTpprojLeiContrpartRepositorySpy
from src.presenters.controllers import RegisterAbginvestTpprojLeiContrpartController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterAbginvestTpprojLeiContrpartRoute"""

    register_abginvest_tpproj_lei_contrpart_use_case = (
        RegisterAbginvestTpprojLeiContrpartSpy(
            AbginvestTpprojLeiContrpartRepositorySpy()
        )
    )
    register_abginvest_contpart_route = RegisterAbginvestTpprojLeiContrpartController(
        register_abginvest_tpproj_lei_contrpart_use_case=register_abginvest_tpproj_lei_contrpart_use_case
    )

    attributer = {
        "order": faker.random_number(digits=5),
        "id_relacao_contrapartida": faker.random_number(digits=5),
        "id_abginvest_tpproj_lei": faker.random_number(digits=5),
    }

    response = register_abginvest_contpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_abginvest_tpproj_lei_contrpart_use_case.register_param["ordem"]
        == attributer["order"]
    )
    assert (
        register_abginvest_tpproj_lei_contrpart_use_case.register_param[
            "id_relacao_contrapartida"
        ]
        == attributer["id_relacao_contrapartida"]
    )
    assert (
        register_abginvest_tpproj_lei_contrpart_use_case.register_param[
            "id_abginvest_tpproj_lei"
        ]
        == attributer["id_abginvest_tpproj_lei"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_abginvest_tpproj_lei_contrpart_use_case = (
        RegisterAbginvestTpprojLeiContrpartSpy(
            AbginvestTpprojLeiContrpartRepositorySpy()
        )
    )
    register_abginvest_contpart_route = RegisterAbginvestTpprojLeiContrpartController(
        register_abginvest_tpproj_lei_contrpart_use_case=register_abginvest_tpproj_lei_contrpart_use_case
    )

    attributer = {
        "ordem": faker.word(),
        "id_relacao_contrapartida": faker.word(),
        "id_abginvest_tpproj_lei": faker.word(),
    }

    response = register_abginvest_contpart_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_abginvest_tpproj_lei_contrpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_param():
    """Testing route no query param method"""

    register_abginvest_tpproj_lei_contrpart_use_case = (
        RegisterAbginvestTpprojLeiContrpartSpy(
            AbginvestTpprojLeiContrpartRepositorySpy()
        )
    )
    register_abginvest_contpart_route = RegisterAbginvestTpprojLeiContrpartController(
        register_abginvest_tpproj_lei_contrpart_use_case=register_abginvest_tpproj_lei_contrpart_use_case
    )

    response = register_abginvest_contpart_route.route(HttpRequest())

    # Testing input
    assert register_abginvest_tpproj_lei_contrpart_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
