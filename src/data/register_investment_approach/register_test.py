from faker import Faker
from src.infra.test import InvestmentApproachRepositorySpy
from .register import RegisterInvestmentApproach

faker = Faker()


def test_register():
    """Testing registry method"""

    investment_appr_repo = InvestmentApproachRepositorySpy()
    register_investment_appr = RegisterInvestmentApproach(investment_appr_repo)

    attributes = {
        "description": faker.word(),
        "incetivado": faker.boolean(),
    }

    response = register_investment_appr.registry(
        descricao=attributes["description"], incetivado=attributes["incetivado"]
    )

    # Testing inputs
    assert (
        investment_appr_repo.insert_investment_appr_params["descricao"]
        == attributes["description"]
    )
    assert (
        investment_appr_repo.insert_investment_appr_params["incetivado"]
        == attributes["incetivado"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing registry method fail"""

    investment_appr_repo = InvestmentApproachRepositorySpy()
    register_investment_appr = RegisterInvestmentApproach(investment_appr_repo)

    attributes = {
        "description": faker.boolean(),
        "incetivado": faker.word(),
    }

    response = register_investment_appr.registry(
        descricao=attributes["description"], incetivado=attributes["incetivado"]
    )

    # Testing inputs
    assert investment_appr_repo.insert_investment_appr_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None