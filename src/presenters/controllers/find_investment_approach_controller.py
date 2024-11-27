from typing import Type

from src.domain.use_cases import FindInvestmentApproachInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


class FindInvestmentApproachController(RouteInterface):
    """Class to define controller to find investment approach use case"""

    def __init__(
        self, find_investment_appr_use_case: Type[FindInvestmentApproachInterface]
    ):
        self.find_investment_appr_use_case = find_investment_appr_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = self.find_investment_appr_use_case.all()

        return HttpResponse(status_code=200, body=response["Data"])

        # If not query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
