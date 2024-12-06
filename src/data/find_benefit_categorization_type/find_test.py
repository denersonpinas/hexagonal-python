from faker import Faker

from .find import FindBenefitCategorizationType
from src.infra.test import BenefitCategorizationTypeRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    categorization_type_repo = BenefitCategorizationTypeRepositorySpy()
    find_categorization_type = FindBenefitCategorizationType(
        categorization_type_repo=categorization_type_repo
    )

    attributes = {"id": faker.text(max_nb_chars=32)}
    response = find_categorization_type.by_id(id=attributes["id"])

    # Testing inputs
    assert (
        categorization_type_repo.select_categorization_type_params["id"]
        == attributes["id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method fail"""

    categorization_type_repo = BenefitCategorizationTypeRepositorySpy()
    find_categorization_type = FindBenefitCategorizationType(
        categorization_type_repo=categorization_type_repo
    )

    attributes = {"id": faker.boolean()}
    response = find_categorization_type.by_id(id=attributes["id"])

    # Testing inputs
    assert categorization_type_repo.select_categorization_type_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_all():
    """Testing by_default method"""

    categorization_type_repo = BenefitCategorizationTypeRepositorySpy()
    find_categorization_type = FindBenefitCategorizationType(
        categorization_type_repo=categorization_type_repo
    )

    response = find_categorization_type.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
