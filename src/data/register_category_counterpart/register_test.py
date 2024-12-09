from faker import Faker
from src.infra.test import CategoryCounterpartRepositorySpy
from .register import RegisterCategoryCounterpart

faker = Faker()


def test_register():
    """Testing register method"""

    category_counterpart_repo = CategoryCounterpartRepositorySpy()
    register_category_counterpart = RegisterCategoryCounterpart(
        category_counterpart_repo
    )

    attributes = {
        "name": faker.text(max_nb_chars=120),
        "description": faker.text(max_nb_chars=500),
        "subcategory_id": faker.random_number(digits=5),
    }

    response = register_category_counterpart.register(
        nome=attributes["name"],
        descricao=attributes["description"],
        subcategoria_de_id=attributes["subcategory_id"],
    )

    # Testing inputs
    assert (
        category_counterpart_repo.insert_category_counterpart_params["descricao"]
        == attributes["description"]
    )
    assert (
        category_counterpart_repo.insert_category_counterpart_params["nome"]
        == attributes["name"]
    )
    assert (
        category_counterpart_repo.insert_category_counterpart_params[
            "subcategoria_de_id"
        ]
        == attributes["subcategory_id"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail_max_nb_char():
    """Testing register method in fail with max lenght char"""

    category_counterpart_repo = CategoryCounterpartRepositorySpy()
    register_category_counterpart = RegisterCategoryCounterpart(
        category_counterpart_repo
    )

    attributes = {
        "name": faker.text(max_nb_chars=1200),
        "description": faker.text(max_nb_chars=5000),
        "subcategory_id": faker.random_number(digits=5),
    }

    response = register_category_counterpart.register(
        nome=attributes["name"],
        descricao=attributes["description"],
        subcategoria_de_id=attributes["subcategory_id"],
    )

    # Testing inputs
    assert category_counterpart_repo.insert_category_counterpart_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method in fail"""

    category_counterpart_repo = CategoryCounterpartRepositorySpy()
    register_category_counterpart = RegisterCategoryCounterpart(
        category_counterpart_repo
    )

    attributes = {
        "name": faker.boolean(),
        "description": faker.boolean(),
        "subcategory_id": faker.word(),
    }

    response = register_category_counterpart.register(
        nome=attributes["name"],
        descricao=attributes["description"],
        subcategoria_de_id=attributes["subcategory_id"],
    )

    # Testing inputs
    assert category_counterpart_repo.insert_category_counterpart_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
