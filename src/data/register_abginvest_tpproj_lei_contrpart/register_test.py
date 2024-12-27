from faker import Faker
from src.infra.test import AbginvestTpprojLeiContrpartRepositorySpy
from .register import RegisterAbginvestTpprojLeiContrpart

faker = Faker()


def test_register():
    """Testing register method"""

    abginvest_tpproj_lei_contrpart_repo = AbginvestTpprojLeiContrpartRepositorySpy()
    register_abginvest_tpproj_lei_contrpart = RegisterAbginvestTpprojLeiContrpart(
        abginvest_tpproj_lei_contrpart_repo=abginvest_tpproj_lei_contrpart_repo
    )

    attributes = {
        "ordem": faker.random_number(digits=5),
        "id_relacao_contrapartida_categoria": faker.random_number(digits=5),
        "id_abginvest_tpproj_lei": faker.random_number(digits=5),
    }

    response = register_abginvest_tpproj_lei_contrpart.register(
        ordem=attributes["ordem"],
        id_relacao_contrapartida=attributes["id_relacao_contrapartida_categoria"],
        id_abginvest_tpproj_lei=attributes["id_abginvest_tpproj_lei"],
    )

    # Testing inputs
    assert (
        abginvest_tpproj_lei_contrpart_repo.insert_abginvest_tpproj_lei_contrpart_params[
            "ordem"
        ]
        == attributes["ordem"]
    )
    assert (
        abginvest_tpproj_lei_contrpart_repo.insert_abginvest_tpproj_lei_contrpart_params[
            "id_relacao_contrapartida_categoria"
        ]
        == attributes["id_relacao_contrapartida_categoria"]
    )
    assert (
        abginvest_tpproj_lei_contrpart_repo.insert_abginvest_tpproj_lei_contrpart_params[
            "id_abginvest_tpproj_lei"
        ]
        == attributes["id_abginvest_tpproj_lei"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing register method in fail"""

    abginvest_tpproj_lei_contrpart_repo = AbginvestTpprojLeiContrpartRepositorySpy()
    register_abginvest_tpproj_lei_contrpart = RegisterAbginvestTpprojLeiContrpart(
        abginvest_tpproj_lei_contrpart_repo=abginvest_tpproj_lei_contrpart_repo
    )

    attributes = {
        "ordem": faker.boolean(),
        "id_relacao_contrapartida": faker.boolean(),
        "id_abginvest_tpproj_lei": faker.word(),
    }

    response = register_abginvest_tpproj_lei_contrpart.register(
        ordem=attributes["ordem"],
        id_relacao_contrapartida=attributes["id_relacao_contrapartida"],
        id_abginvest_tpproj_lei=attributes["id_abginvest_tpproj_lei"],
    )

    # Testing inputs
    assert (
        abginvest_tpproj_lei_contrpart_repo.insert_abginvest_tpproj_lei_contrpart_params
        == {}
    )

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
