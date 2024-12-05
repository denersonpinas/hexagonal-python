from faker import Faker
from src.domain.models import Thematic

faker = Faker()


def mock_thematic() -> Thematic:
    """Mocking Thematic"""

    return Thematic(
        id=faker.random_number(digits=5), descricao=faker.text(max_nb_chars=50)
    )
