from uuid import uuid4
from faker import Faker
from src.domain.models import BenefitCategorization

faker = Faker()


def mock_categorization() -> BenefitCategorization:
    """Mocking BenefitCategorization"""

    return BenefitCategorization(
        id=faker.random_number(digits=5),
        valor=faker.text(max_nb_chars=64),
        tipo_id=str(uuid4().hex),
    )
