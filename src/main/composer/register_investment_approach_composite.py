from src.data.register_investment_approach import RegisterInvestmentApproach
from src.infra.repo import InvestmentApproachRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterInvestmentApproachController


def register_investmento_approacht_composer() -> RouteInterface:
    """Composing Register Investment Approach Route
    :param  -   None
    :return -   Object with Register Investment Approach Route
    """

    repository = InvestmentApproachRepository()
    use_case = RegisterInvestmentApproach(repository)
    register_invest_appr_route = RegisterInvestmentApproachController(use_case)

    return register_invest_appr_route
