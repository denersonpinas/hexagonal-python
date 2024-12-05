from faker import Faker

from .find import FindThematic
from src.infra.test import ThematicRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    thematic_repo = ThematicRepositorySpy()
    find_thematic = FindThematic(thematic_repo=thematic_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_thematic.by_id(id=attributes["id"])

    # Testing inputs
    assert thematic_repo.select_thematic_params["id"] == attributes["id"]

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method fail"""

    thematic_repo = ThematicRepositorySpy()
    find_thematic = FindThematic(thematic_repo=thematic_repo)

    attributes = {"id": faker.word()}
    response = find_thematic.by_id(id=attributes["id"])

    # Testing inputs
    assert thematic_repo.select_thematic_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_all():
    """Testing by_default method"""

    thematic_repo = ThematicRepositorySpy()
    find_thematic = FindThematic(thematic_repo=thematic_repo)

    response = find_thematic.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
