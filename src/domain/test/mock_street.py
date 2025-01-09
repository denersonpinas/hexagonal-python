from uuid import uuid4
from faker import Faker
from src.domain.models import Street

faker = Faker()


def mock_street() -> Street:
    """Mocking Street"""

    return Street(
        id=uuid4(), nome=faker.street_name()[:100], bairro_id_id=faker.random_int(min=1)
    )
