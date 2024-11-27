from faker import Faker
from src.data.test import FindInvestmentApproachSpy
from src.infra.test import InvestmentApproachRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_investment_approach_controller import FindInvestmentApproachController

faker = Faker()


def test_route_all():
    """Testing Route method"""

    find_investment_appr_use_case = FindInvestmentApproachSpy(
        InvestmentApproachRepositorySpy()
    )
    find_investment_appr_controller = FindInvestmentApproachController(
        find_investment_appr_use_case=find_investment_appr_use_case
    )
    http_request = HttpRequest()

    response = find_investment_appr_controller.route(http_request=http_request)

    # Testing Output
    assert response.status_code == 200
    assert response.body
