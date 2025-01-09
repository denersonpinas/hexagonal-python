from uuid import uuid4
from faker import Faker
from src.domain.models import ProjectContactPoint

faker = Faker()


def mock_project_contact() -> ProjectContactPoint:
    """Mocking ProjectContactPoint"""

    return ProjectContactPoint(
        id=uuid4(),
        nome=faker.name()[:100],
        email=faker.email()[:100],
        cargo=faker.job()[:100],
        proposta_id=uuid4(),
    )
