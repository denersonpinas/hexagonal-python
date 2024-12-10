from faker import Faker

from .find import FindAbginvestTpprojLeiContrpart
from src.infra.test import AbginvestTpprojLeiContrpartRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    abginvest_tpproj_lei_contrpart_repo = AbginvestTpprojLeiContrpartRepositorySpy()
    find_abginvest_tpproj_lei_contrpart = FindAbginvestTpprojLeiContrpart(
        abginvest_tpproj_lei_contrpart_repo=abginvest_tpproj_lei_contrpart_repo
    )

    attributes = {"id": faker.random_number(digits=2)}
    response = find_abginvest_tpproj_lei_contrpart.by_id(id=attributes["id"])

    # Testing inputs
    assert (
        abginvest_tpproj_lei_contrpart_repo.select_abginvest_tpproj_lei_contrpart_params[
            "id"
        ]
        == attributes["id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method fail"""

    abginvest_tpproj_lei_contrpart_repo = AbginvestTpprojLeiContrpartRepositorySpy()
    find_abginvest_tpproj_lei_contrpart = FindAbginvestTpprojLeiContrpart(
        abginvest_tpproj_lei_contrpart_repo=abginvest_tpproj_lei_contrpart_repo
    )

    attributes = {"id": faker.word()}
    response = find_abginvest_tpproj_lei_contrpart.by_id(id=attributes["id"])

    # Testing inputs
    assert (
        abginvest_tpproj_lei_contrpart_repo.select_abginvest_tpproj_lei_contrpart_params
        == {}
    )

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_abginvest_tpproj_lei():
    """Testing by_abginvest_tpproj_lei method"""

    abginvest_tpproj_lei_contrpart_repo = AbginvestTpprojLeiContrpartRepositorySpy()
    find_abginvest_tpproj_lei_contrpart = FindAbginvestTpprojLeiContrpart(
        abginvest_tpproj_lei_contrpart_repo=abginvest_tpproj_lei_contrpart_repo
    )

    attributes = {"abginvest_tpproj_lei_id": faker.random_number(digits=2)}
    response = find_abginvest_tpproj_lei_contrpart.by_abginvest_tpproj_lei(
        abginvest_tpproj_lei_id=attributes["abginvest_tpproj_lei_id"]
    )

    # Testing inputs
    assert (
        abginvest_tpproj_lei_contrpart_repo.select_abginvest_tpproj_lei_contrpart_params[
            "id_abginvest_tpproj_lei"
        ]
        == attributes["abginvest_tpproj_lei_id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_abginvest_tpproj_lei_fail():
    """Testing by_abginvest_tpproj_lei method fail"""

    abginvest_tpproj_lei_contrpart_repo = AbginvestTpprojLeiContrpartRepositorySpy()
    find_abginvest_tpproj_lei_contrpart = FindAbginvestTpprojLeiContrpart(
        abginvest_tpproj_lei_contrpart_repo=abginvest_tpproj_lei_contrpart_repo
    )

    attributes = {"abginvest_tpproj_lei_id": faker.word()}
    response = find_abginvest_tpproj_lei_contrpart.by_abginvest_tpproj_lei(
        abginvest_tpproj_lei_id=attributes["abginvest_tpproj_lei_id"]
    )

    # Testing inputs
    assert (
        abginvest_tpproj_lei_contrpart_repo.select_abginvest_tpproj_lei_contrpart_params
        == {}
    )

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_all():
    """Testing by_default method"""

    abginvest_tpproj_lei_contrpart_repo = AbginvestTpprojLeiContrpartRepositorySpy()
    find_abginvest_tpproj_lei_contrpart = FindAbginvestTpprojLeiContrpart(
        abginvest_tpproj_lei_contrpart_repo=abginvest_tpproj_lei_contrpart_repo
    )

    response = find_abginvest_tpproj_lei_contrpart.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
