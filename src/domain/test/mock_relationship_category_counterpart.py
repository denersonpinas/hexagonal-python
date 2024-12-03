from faker import Faker
from src.domain.models import RelationshipCategoryCounterparts

faker = Faker()


def mock_relationship_category_counterparts() -> RelationshipCategoryCounterparts:
    """Mocking RelationshipCategoryCounterparts"""

    return RelationshipCategoryCounterparts(
        id=faker.random_number(digits=5),
        categoria_id=faker.random_number(digits=5),
        contrapartida_id=faker.random_number(digits=5),
    )
