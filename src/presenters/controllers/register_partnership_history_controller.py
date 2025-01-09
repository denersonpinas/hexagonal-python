from typing import Type
from src.domain.use_cases.register_partnership_history_interface import (
    RegisterPartnershipHistoryInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterPartnershipHistoryController(RouteInterface):
    """Class to define route to register_partnership_history use case"""

    def __init__(
        self,
        register_partnership_history_use_case: Type[
            RegisterPartnershipHistoryInterface
        ],
    ):
        self.register_partnership_history_use_case = (
            register_partnership_history_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["sponsors_number", "renewal_number", "proposal_id"]

            if all(param in body_params for param in required_params):
                try:
                    sponsors_number = int(http_request.body["sponsors_number"])
                    renewal_number = int(http_request.body["renewal_number"])
                    proposal_id = http_request.body["proposal_id"]
                    additional_info = http_request.body.get("additional_info")

                    response = self.register_partnership_history_use_case.register(
                        sponsors_number=sponsors_number,
                        renewal_number=renewal_number,
                        proposal_id=proposal_id,
                        additional_info=additional_info,
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
