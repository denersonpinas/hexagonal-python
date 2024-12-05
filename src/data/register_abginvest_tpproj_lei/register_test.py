from faker import Faker
from src.infra.test import AbginvestTpprojLeiRepositorySpy
from .register import RegisterAbginvestTpprojLei

faker = Faker()


def test_register():
    """Testing register method"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    register_abginvest_tpproj_lei = RegisterAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {
        "investment_approach_id": faker.random_number(digits=5),
        "type_project_id": faker.random_number(digits=5),
        "law_id": faker.random_number(digits=5),
    }

    response = register_abginvest_tpproj_lei.register(
        investment_approach_id=attributes["investment_approach_id"],
        type_project_id=attributes["type_project_id"],
        law_id=attributes["law_id"],
    )

    # Testing inputs
    assert (
        abginvest_tpproj_lei_repo.insert_abginvest_tpproj_lei_params[
            "abordagem_investimento_id"
        ]
        == attributes["investment_approach_id"]
    )
    assert (
        abginvest_tpproj_lei_repo.insert_abginvest_tpproj_lei_params["lei_id"]
        == attributes["law_id"]
    )
    assert (
        abginvest_tpproj_lei_repo.insert_abginvest_tpproj_lei_params["tipo_projeto_id"]
        == attributes["type_project_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing register method in fail"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    register_abginvest_tpproj_lei = RegisterAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {
        "investment_approach_id": faker.boolean(),
        "type_project_id": faker.boolean(),
        "law_id": faker.word(),
    }

    response = register_abginvest_tpproj_lei.register(
        investment_approach_id=attributes["investment_approach_id"],
        type_project_id=attributes["type_project_id"],
        law_id=attributes["law_id"],
    )

    # Testing inputs
    assert abginvest_tpproj_lei_repo.insert_abginvest_tpproj_lei_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
