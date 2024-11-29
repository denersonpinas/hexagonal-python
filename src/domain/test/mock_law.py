from faker import Faker
from src.domain.models import Law

faker = Faker()


def mock_law() -> Law:
    """Mocking InvestmentApproach"""

    return Law(
        id=faker.random_number(digits=5),
        nome=faker.text(max_nb_chars=100),
        descricao=faker.text(max_nb_chars=250),
    )
