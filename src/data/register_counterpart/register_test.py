from faker import Faker
from src.data.register_counterpart import RegisterCounterpart
from src.infra.test import CounterpartRepositorySpy

faker = Faker()


def test_register():
    """Testing registry method"""

    counterpart_repo = CounterpartRepositorySpy()
    register_counterpart = RegisterCounterpart(counterpart_repo)

    attributes = {
        "description": faker.word(),
        "example_aplicabilirity": faker.word(),
        "required": faker.boolean(),
    }

    response = register_counterpart.register(
        descricao=attributes["description"],
        exemplo_aplicabilidade=attributes["example_aplicabilirity"],
        obrigatoria=attributes["required"],
    )

    # Testing inputs
    assert (
        counterpart_repo.insert_counterpart_params["descricao"]
        == attributes["description"]
    )
    assert (
        counterpart_repo.insert_counterpart_params["exemplo_aplicabilidade"]
        == attributes["example_aplicabilirity"]
    )
    assert (
        counterpart_repo.insert_counterpart_params["obrigatoria"]
        == attributes["required"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing registry method in fail"""

    counterpart_repo = CounterpartRepositorySpy()
    register_counterpart = RegisterCounterpart(counterpart_repo)

    attributes = {
        "description": faker.random_number(),
        "example_aplicabilirity": faker.random_number(),
        "required": faker.word(),
    }

    response = register_counterpart.register(
        descricao=attributes["description"],
        exemplo_aplicabilidade=attributes["example_aplicabilirity"],
        obrigatoria=attributes["required"],
    )

    # Testing inputs
    assert counterpart_repo.insert_counterpart_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
