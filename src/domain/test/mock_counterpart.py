from faker import Faker
from src.domain.models import Counterpart

faker = Faker()


def mock_counterpart() -> Counterpart:
    """Mocking Counterpart"""

    return Counterpart(
        id=faker.random_number(digits=5),
        descricao=faker.word(),
        exemplo_aplicabilidade=faker.word(),
        obrigatoria=faker.boolean(),
        padrao=True,
    )
