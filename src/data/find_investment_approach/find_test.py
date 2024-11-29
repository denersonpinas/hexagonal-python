from faker import Faker

from src.infra.test import InvestmentApproachRepositorySpy
from .find import FindInvestmentApproach

faker = Faker()


def test_all():
    """Testing all method"""

    investment_approach_repo = InvestmentApproachRepositorySpy()
    find_investment_appr = FindInvestmentApproach(
        investment_appr_repository=investment_approach_repo
    )

    response = find_investment_appr.all()

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
