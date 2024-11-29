from typing import Type

from src.domain.use_cases import FindLawInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.helpers import HttpRequest, HttpResponse


class FindLawController(RouteInterface):
    """Class to define controller to find law use case"""

    def __init__(self, find_law_use_case: Type[FindLawInterface]):
        self.find_law_use_case = find_law_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = self.find_law_use_case.all()

        return HttpResponse(status_code=200, body=response["Data"])
