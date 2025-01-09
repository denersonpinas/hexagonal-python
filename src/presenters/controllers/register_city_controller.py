from typing import Type
from src.domain.use_cases.register_city_interface import RegisterCityInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterCityController(RouteInterface):
    """Class to define route to register_city use case"""

    def __init__(
        self,
        register_city_use_case: Type[RegisterCityInterface],
    ):
        self.register_city_use_case = register_city_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["name", "state"]

            if all(param in body_params for param in required_params):
                try:
                    name = http_request.body["name"]
                    state = http_request.body["state"]

                    response = self.register_city_use_case.register(
                        name=name, state=state
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
