from typing import Type

from src.domain.use_cases import RegisterBenefitCategorizationInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterBenefitCategorizationController(RouteInterface):
    """Class to define route to register_categorization use case"""

    def __init__(
        self,
        register_categorization_use_case: Type[RegisterBenefitCategorizationInterface],
    ):
        self.register_categorization_use_case = register_categorization_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            # If query

            body_params = http_request.body.keys()

            if "value" in body_params and "type_id" in body_params:
                value = http_request.body["value"]
                type_id = http_request.body["type_id"]

                response = self.register_categorization_use_case.register(
                    value=value, type_id=type_id
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If not query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
