from typing import Type
from src.domain.use_cases.register_project_history_interface import (
    RegisterProjectHistoryInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterProjectHistoryController(RouteInterface):
    """Class to define route to register_project_history use case"""

    def __init__(
        self,
        register_project_history_use_case: Type[RegisterProjectHistoryInterface],
    ):
        self.register_project_history_use_case = register_project_history_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = [
                "investment_year",
                "title",
                "investment_type",
                "proposal_id",
            ]

            if all(param in body_params for param in required_params):
                try:
                    investment_year = int(http_request.body["investment_year"])
                    title = http_request.body["title"]
                    investment_type = http_request.body["investment_type"]
                    proposal_id = http_request.body["proposal_id"]

                    response = self.register_project_history_use_case.register(
                        investment_year=investment_year,
                        title=title,
                        investment_type=investment_type,
                        proposal_id=proposal_id,
                    )
                except (ValueError, TypeError):
                    response = {"Success": False, "Data": None}
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
