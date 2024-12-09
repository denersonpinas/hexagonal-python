from faker import Faker

from src.data.test import RegisterInvestmentApproachSpy
from src.infra.test import InvestmentApproachRepositorySpy
from src.presenters.controllers import RegisterInvestmentApproachController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterInvestmentApproach"""

    register_investment_appr_use_case = RegisterInvestmentApproachSpy(
        InvestmentApproachRepositorySpy()
    )
    register_investment_approach_route = RegisterInvestmentApproachController(
        register_investment_approach_use_case=register_investment_appr_use_case
    )

    attributer = {
        "description": faker.word(),
        "incentivized": faker.boolean(),
    }

    response = register_investment_approach_route.route(HttpRequest(body=attributer))

    # Testing input
    assert (
        register_investment_appr_use_case.register_param["descricao"]
        == attributer["description"]
    )
    assert (
        register_investment_appr_use_case.register_param["incentivado"]
        == attributer["incentivized"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_investment_appr_use_case = RegisterInvestmentApproachSpy(
        InvestmentApproachRepositorySpy()
    )
    register_investment_approach_route = RegisterInvestmentApproachController(
        register_investment_approach_use_case=register_investment_appr_use_case
    )

    attributer = {
        "description": faker.boolean(),
        "incentivized": faker.word(),
    }

    response = register_investment_approach_route.route(HttpRequest(body=attributer))

    # Testing input
    assert register_investment_appr_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_investment_appr_use_case = RegisterInvestmentApproachSpy(
        InvestmentApproachRepositorySpy()
    )
    register_investment_approach_route = RegisterInvestmentApproachController(
        register_investment_approach_use_case=register_investment_appr_use_case
    )

    response = register_investment_approach_route.route(HttpRequest())

    # Testing input
    assert register_investment_appr_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body
