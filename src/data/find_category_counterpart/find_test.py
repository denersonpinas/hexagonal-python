from faker import Faker

from .find import FindCategoryCounterpart
from src.infra.test import CategoryCounterpartRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    category_counterpart_repo = CategoryCounterpartRepositorySpy()
    find_category_counterpart = FindCategoryCounterpart(
        category_counterpart_repo=category_counterpart_repo
    )

    attributes = {"id": faker.random_number(digits=2)}
    response = find_category_counterpart.by_id(category_counterpart_id=attributes["id"])

    # Testing inputs
    assert (
        category_counterpart_repo.select_category_counterpart_params[
            "category_counterpart_id"
        ]
        == attributes["id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method fail"""

    category_counterpart_repo = CategoryCounterpartRepositorySpy()
    find_category_counterpart = FindCategoryCounterpart(
        category_counterpart_repo=category_counterpart_repo
    )

    attributes = {"id": faker.word()}
    response = find_category_counterpart.by_id(category_counterpart_id=attributes["id"])

    # Testing inputs
    assert category_counterpart_repo.select_category_counterpart_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_subcategory():
    """Testing by_subcategory method"""

    category_counterpart_repo = CategoryCounterpartRepositorySpy()
    find_category_counterpart = FindCategoryCounterpart(
        category_counterpart_repo=category_counterpart_repo
    )

    attributes = {"id": faker.random_number(digits=2)}
    response = find_category_counterpart.by_subcategory(subcategory_id=attributes["id"])

    # Testing inputs
    assert (
        category_counterpart_repo.select_category_counterpart_params[
            "subcategoria_de_id"
        ]
        == attributes["id"]
    )

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_subcategory_fail():
    """Testing by_subcategory method fail"""

    category_counterpart_repo = CategoryCounterpartRepositorySpy()
    find_category_counterpart = FindCategoryCounterpart(
        category_counterpart_repo=category_counterpart_repo
    )

    attributes = {"id": faker.word()}
    response = find_category_counterpart.by_subcategory(subcategory_id=attributes["id"])

    # Testing inputs
    assert category_counterpart_repo.select_category_counterpart_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_all():
    """Testing by_default method"""

    category_counterpart_repo = CategoryCounterpartRepositorySpy()
    find_category_counterpart = FindCategoryCounterpart(
        category_counterpart_repo=category_counterpart_repo
    )

    response = find_category_counterpart.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
