from faker import Faker

from src.infra.test import TypeProjectRepositorySpy
from .find import FindTypeProject

faker = Faker()


def test_all():
    """Testing all method"""

    type_project_repository = TypeProjectRepositorySpy()
    find_type_project = FindTypeProject(type_project_repository=type_project_repository)

    response = find_type_project.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
