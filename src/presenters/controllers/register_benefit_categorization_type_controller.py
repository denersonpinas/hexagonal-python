from typing import Type

from src.domain.use_cases import RegisterBenefitCategorizationTypeInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterBenefitCategorizationTypeController(RouteInterface):
    """Class to define route to register_categorization use case"""

    def __init__(
        self,
        register_categorization_type_use_case: Type[
            RegisterBenefitCategorizationTypeInterface
        ],
    ):
        self.register_categorization_type_use_case = (
            register_categorization_type_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            # If query

            body_params = http_request.body.keys()

            if (
                "id" in body_params
                and "description" in body_params
                and "info" in body_params
            ):
                id = http_request.body["id"]
                description = http_request.body["description"]
                info = http_request.body["info"]

                response = self.register_categorization_type_use_case.register(
                    id=id, description=description, info=info
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
