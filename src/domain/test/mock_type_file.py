from faker import Faker
from src.domain.models import TypeFile

faker = Faker()


def mock_type_file() -> TypeFile:
    """Mocking TypeFile"""

    return TypeFile(
        id=faker.random_number(digits=5),
        contexto=faker.text(max_nb_chars=32),
        descricao=faker.text(max_nb_chars=120),
        info=faker.text(max_nb_chars=1000),
    )
