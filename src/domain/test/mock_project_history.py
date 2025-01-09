from uuid import uuid4
from faker import Faker
from src.domain.models import ProjectHistory

faker = Faker()


def mock_project_history() -> ProjectHistory:
    """Mocking ProjectHistory"""

    return ProjectHistory(
        id=uuid4(),
        ano_investimento=faker.random_int(min=1901, max=2023),
        titulo=faker.sentence()[:100],
        tipo_investimento=faker.word()[:50],
        proposta_id=uuid4(),
    )
