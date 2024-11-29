from faker import Faker
from src.domain.models import TypeProject

faker = Faker()


def mock_type_project() -> TypeProject:
    """Mocking TypeProject"""

    return TypeProject(
        id=faker.random_number(digits=5),
        nome=faker.text(max_nb_chars=100),
        descricao=faker.text(max_nb_chars=250),
    )
