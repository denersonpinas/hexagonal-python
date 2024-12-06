from faker import Faker

from .find import FindBenefitCategorization
from src.infra.test import BenefitCategorizationRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    categorization_repo = BenefitCategorizationRepositorySpy()
    find_categorization = FindBenefitCategorization(
        categorization_repo=categorization_repo
    )

    attributes = {"id": faker.random_number(digits=2)}
    response = find_categorization.by_id(id=attributes["id"])

    # Testing inputs
    assert categorization_repo.select_categorization_params["id"] == attributes["id"]

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method fail"""

    categorization_repo = BenefitCategorizationRepositorySpy()
    find_categorization = FindBenefitCategorization(
        categorization_repo=categorization_repo
    )

    attributes = {"id": faker.word()}
    response = find_categorization.by_id(id=attributes["id"])

    # Testing inputs
    assert categorization_repo.select_categorization_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_type():
    """Testing by_type method"""

    categorization_repo = BenefitCategorizationRepositorySpy()
    find_categorization = FindBenefitCategorization(
        categorization_repo=categorization_repo
    )

    attributes = {"type_id": faker.text(max_nb_chars=32)}
    response = find_categorization.by_type(type_id=attributes["type_id"])

    # Testing inputs
    assert (
        categorization_repo.select_categorization_params["tipo_id"]
        == attributes["type_id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_type_fail():
    """Testing by_type method fail"""

    categorization_repo = BenefitCategorizationRepositorySpy()
    find_categorization = FindBenefitCategorization(
        categorization_repo=categorization_repo
    )

    attributes = {"type_id": faker.boolean()}
    response = find_categorization.by_type(type_id=attributes["type_id"])

    # Testing inputs
    assert categorization_repo.select_categorization_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_all():
    """Testing by_default method"""

    categorization_repo = BenefitCategorizationRepositorySpy()
    find_categorization = FindBenefitCategorization(
        categorization_repo=categorization_repo
    )

    response = find_categorization.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
