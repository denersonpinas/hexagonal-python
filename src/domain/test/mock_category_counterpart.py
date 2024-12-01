from faker import Faker
from src.domain.models import CategoryCounterpart

faker = Faker()


def mock_category_counterpart() -> CategoryCounterpart:
    """Mocking CategoryCounterpart"""

    return CategoryCounterpart(
        id=faker.random_number(digits=5),
        nome=faker.text(max_nb_chars=120),
        descricao=faker.text(max_nb_chars=500),
        subcategoria_id=faker.random_number(digits=5),
    )
