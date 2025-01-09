from uuid import uuid4
from faker import Faker
from src.domain.models import Neighborhood

faker = Faker()


def mock_neighborhood() -> Neighborhood:
    """Mocking Neighborhood"""

    return Neighborhood(
        id=uuid4(), name=faker.city_suffix()[:100], city_id=faker.random_int(min=1)
    )
