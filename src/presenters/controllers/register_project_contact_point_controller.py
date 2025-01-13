from typing import Type
from src.domain.use_cases.register_project_contact_point_interface import (
    RegisterProjectContactPointInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterProjectContactPointController(RouteInterface):
    """Class to define route to register_project_contact_point use case"""

    def __init__(
        self,
        register_project_contact_point_use_case: Type[
            RegisterProjectContactPointInterface
        ],
    ):
        self.register_project_contact_point_use_case = (
            register_project_contact_point_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["name", "email", "position", "proposal_id"]

            if all(param in body_params for param in required_params):
                try:
                    name = http_request.body["name"]
                    email = http_request.body["email"]
                    position = http_request.body["position"]
                    proposal_id = http_request.body["proposal_id"]

                    response = self.register_project_contact_point_use_case.register(
                        name=name,
                        email=email,
                        position=position,
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
