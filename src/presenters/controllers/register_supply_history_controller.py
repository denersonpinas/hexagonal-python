from typing import Type
from src.domain.use_cases.register_supply_history_interface import (
    RegisterSupplyHistoryInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterSupplyHistoryController(RouteInterface):
    """Class to define route to register_supply_history use case"""

    def __init__(
        self,
        register_supply_history_use_case: Type[RegisterSupplyHistoryInterface],
    ):
        self.register_supply_history_use_case = register_supply_history_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["service_provided", "hiring_manager", "proposal_id"]

            if all(param in body_params for param in required_params):
                try:
                    service_provided = http_request.body["service_provided"]
                    hiring_manager = http_request.body["hiring_manager"]
                    proposal_id = http_request.body["proposal_id"]

                    response = self.register_supply_history_use_case.register(
                        service_provided=service_provided,
                        hiring_manager=hiring_manager,
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
