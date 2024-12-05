from faker import Faker

from src.infra.test import TypeFileRepositorySpy
from .find import FindTypeFile

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    type_file_repository = TypeFileRepositorySpy()
    find_type_file = FindTypeFile(type_file_repository=type_file_repository)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_type_file.by_id(id=attributes["id"])

    # Testing inputs
    assert type_file_repository.select_type_file_params["id"] == attributes["id"]

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_fail():
    """Testing by_id method fail"""

    type_file_repository = TypeFileRepositorySpy()
    find_type_file = FindTypeFile(type_file_repository=type_file_repository)

    attributes = {"id": faker.word()}
    response = find_type_file.by_id(id=attributes["id"])

    # Testing inputs
    assert type_file_repository.select_type_file_params == {}

    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None


def test_all():
    """Testing all method"""

    type_file_repository = TypeFileRepositorySpy()
    find_type_file = FindTypeFile(type_file_repository=type_file_repository)

    response = find_type_file.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
