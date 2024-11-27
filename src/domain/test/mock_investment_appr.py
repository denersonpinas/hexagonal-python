from faker import Faker
from src.domain.models import InvestmentApproach

faker = Faker()


def mock_investment_appr() -> InvestmentApproach:
    """Mocking InvestmentApproach"""

    return InvestmentApproach(
        id=faker.random_number(digits=5),
        descricao=faker.word(),
        incetivado=faker.boolean(),
    )
