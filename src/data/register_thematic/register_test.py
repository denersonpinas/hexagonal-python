from faker import Faker
from src.infra.test import ThematicRepositorySpy
from .register import RegisterThematic

faker = Faker()


def test_register():
    """Testing register method"""

    thematic_repo = ThematicRepositorySpy()
    register_thematic = RegisterThematic(thematic_repo=thematic_repo)

    attributes = {"description": faker.text(max_nb_chars=50)}

    response = register_thematic.register(description=attributes["description"])

    # Testing inputs
    assert (
        thematic_repo.insert_thematic_params["descricao"] == attributes["description"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing register method in fail"""

    thematic_repo = ThematicRepositorySpy()
    register_thematic = RegisterThematic(thematic_repo=thematic_repo)

    attributes = {"description": faker.boolean()}

    response = register_thematic.register(description=attributes["description"])

    # Testing inputs
    assert thematic_repo.insert_thematic_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
