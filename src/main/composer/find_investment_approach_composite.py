from src.data.find_investment_approach import FindInvestmentApproach
from src.infra.repo import InvestmentApproachRepository
from src.presenters.controllers import FindInvestmentApproachController


def find_investmento_approacht_composer() -> FindInvestmentApproachController:
    """Composing Find InvestApproach Route
    :param  - None
    :return - Object with Find InvestApproach Route
    """

    repository = InvestmentApproachRepository()
    use_case = FindInvestmentApproach(repository)
    find_investment_approach_route = FindInvestmentApproachController(use_case)

    return find_investment_approach_route
