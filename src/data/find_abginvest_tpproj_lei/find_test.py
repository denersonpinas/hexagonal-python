from faker import Faker

from .find import FindAbginvestTpprojLei
from src.infra.test import AbginvestTpprojLeiRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {"id": faker.random_number(digits=2)}
    response = find_abginvest_tpproj_lei.by_id(id=attributes["id"])

    # Testing inputs
    assert (
        abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei_params["id"]
        == attributes["id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method fail"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {"id": faker.word()}
    response = find_abginvest_tpproj_lei.by_id(id=attributes["id"])

    # Testing inputs
    assert abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_investment_approach():
    """Testing by_investment_approach method"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {"investment_approach_id": faker.random_number(digits=2)}
    response = find_abginvest_tpproj_lei.by_investment_approach(
        investment_approach_id=attributes["investment_approach_id"]
    )

    # Testing inputs
    assert (
        abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei_params[
            "abordagem_investimento_id"
        ]
        == attributes["investment_approach_id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_investment_approach_fail():
    """Testing by_investment_approach method fail"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {"investment_approach_id": faker.word()}
    response = find_abginvest_tpproj_lei.by_investment_approach(
        investment_approach_id=attributes["investment_approach_id"]
    )

    # Testing inputs
    assert abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_type_project():
    """Testing by_type_project method"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {"type_project_id": faker.random_number(digits=2)}
    response = find_abginvest_tpproj_lei.by_type_project(
        type_project_id=attributes["type_project_id"]
    )

    # Testing inputs
    assert (
        abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei_params["tipo_projeto_id"]
        == attributes["type_project_id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_type_project_fail():
    """Testing by_type_project_fail method"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {"type_project_id": faker.word()}
    response = find_abginvest_tpproj_lei.by_type_project(
        type_project_id=attributes["type_project_id"]
    )

    # Testing inputs
    assert abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_law():
    """Testing by_law method"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {"law_id": faker.random_number(digits=2)}
    response = find_abginvest_tpproj_lei.by_law(law_id=attributes["law_id"])

    # Testing inputs
    assert (
        abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei_params["lei_id"]
        == attributes["law_id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_law_fail():
    """Testing by_law_fail method"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    attributes = {"law_id": faker.word()}
    response = find_abginvest_tpproj_lei.by_law(law_id=attributes["law_id"])

    # Testing inputs
    assert abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_all():
    """Testing by_default method"""

    abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepositorySpy()
    find_abginvest_tpproj_lei = FindAbginvestTpprojLei(
        abginvest_tpproj_lei_repo=abginvest_tpproj_lei_repo
    )

    response = find_abginvest_tpproj_lei.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
