from faker import Faker
from src.infra.test import InvestmentApproachRepositorySpy
from .register import RegisterInvestmentApproach

faker = Faker()


def test_register():
    """Testing register method"""

    investment_appr_repo = InvestmentApproachRepositorySpy()
    register_investment_appr = RegisterInvestmentApproach(investment_appr_repo)

    attributes = {
        "description": faker.text(max_nb_chars=80),
        "incentivado": faker.boolean(),
    }

    response = register_investment_appr.register(
        descricao=attributes["description"], incentivado=attributes["incentivado"]
    )

    # Testing inputs
    assert (
        investment_appr_repo.insert_investment_appr_params["descricao"]
        == attributes["description"]
    )
    assert (
        investment_appr_repo.insert_investment_appr_params["incentivado"]
        == attributes["incentivado"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_max_len_description():
    """Testing register with long description method"""

    investment_appr_repo = InvestmentApproachRepositorySpy()
    register_investment_appr = RegisterInvestmentApproach(investment_appr_repo)

    attributes = {
        "description": faker.text(max_nb_chars=9000),
        "incentivado": faker.boolean(),
    }

    response = register_investment_appr.register(
        descricao=attributes["description"], incentivado=attributes["incentivado"]
    )

    # Testing inputs
    assert investment_appr_repo.insert_investment_appr_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    investment_appr_repo = InvestmentApproachRepositorySpy()
    register_investment_appr = RegisterInvestmentApproach(investment_appr_repo)

    attributes = {
        "description": faker.boolean(),
        "incentivado": faker.word(),
    }

    response = register_investment_appr.register(
        descricao=attributes["description"], incentivado=attributes["incentivado"]
    )

    # Testing inputs
    assert investment_appr_repo.insert_investment_appr_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
