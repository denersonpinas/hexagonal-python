from typing import Type
import uuid
from src.domain.use_cases.register_proposal_execution_location_interface import (
    RegisterProposalExecutionLocationInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterProposalExecutionLocationController(RouteInterface):
    """Class to define route to register_proposal_execution_location use case"""

    def __init__(
        self,
        register_proposal_execution_location_use_case: Type[
            RegisterProposalExecutionLocationInterface
        ],
    ):
        self.register_proposal_execution_location_use_case = (
            register_proposal_execution_location_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["city_id", "proposal_id"]

            if all(param in body_params for param in required_params):
                try:
                    city_id = int(http_request.body["city_id"])
                    proposal_id = uuid.UUID(http_request.body["proposal_id"])

                    response = (
                        self.register_proposal_execution_location_use_case.register(
                            city_id=city_id, proposal_id=proposal_id
                        )
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
