from uuid import uuid4
from faker import Faker
from src.domain.models import City

faker = Faker()


def mock_city() -> City:
    """Mocking City"""

    return City(id=uuid4(), name=faker.city()[:100], state=faker.state_abbr())
