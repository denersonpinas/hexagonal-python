from typing import Type

from src.domain.use_cases import RegisterCounterpartInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterCounterpartController(RouteInterface):
    """Class to define route to register_counterpart use case"""

    def __init__(
        self, register_counterpart_use_case: Type[RegisterCounterpartInterface]
    ):
        self.register_counterpart_use_case = register_counterpart_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            # If query

            body_params = http_request.body.keys()

            if (
                "description" in body_params
                and "example_aplicability" in body_params
                and "required" in body_params
            ):
                description = http_request.body["description"]
                example_aplicability = http_request.body["example_aplicability"]
                required = http_request.body["required"]

                response = self.register_counterpart_use_case.register(
                    descricao=description,
                    exemplo_aplicabilidade=example_aplicability,
                    obrigatoria=required,
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
