from typing import Type

from src.domain.use_cases import FindTypeProjectInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.helpers import HttpRequest, HttpResponse


class FindTypeProjectController(RouteInterface):
    """Class to define controller to find type project use case"""

    def __init__(self, find_type_project_use_case: Type[FindTypeProjectInterface]):
        self.find_type_project_use_case = find_type_project_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = self.find_type_project_use_case.all()

        return HttpResponse(status_code=200, body=response["Data"])
