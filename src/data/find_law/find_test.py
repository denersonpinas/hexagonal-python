from faker import Faker

from src.infra.test import LawRepositorySpy
from .find import FindLaw

faker = Faker()


def test_all():
    """Testing all method"""

    law_repository = LawRepositorySpy()
    find_law = FindLaw(law_repository=law_repository)

    response = find_law.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
