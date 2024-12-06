from uuid import uuid4
from faker import Faker
from src.domain.models import BenefitCategorizationType

faker = Faker()


def mock_categorization_type() -> BenefitCategorizationType:
    """Mocking BenefitCategorizationType"""

    return BenefitCategorizationType(
        id=str(uuid4().hex),
        descricao=faker.text(max_nb_chars=50),
        info=faker.text(max_nb_chars=150),
    )
