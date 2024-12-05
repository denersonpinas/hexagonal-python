from typing import Type

from src.domain.use_cases import RegisterAbginvestTpprojLeiInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterAbginvestTpprojLeiController(RouteInterface):
    """Class to define route to register_abginvest_tpproj_lei use case"""

    def __init__(
        self,
        register_abginvest_tpproj_lei_use_case: Type[
            RegisterAbginvestTpprojLeiInterface
        ],
    ):
        self.register_abginvest_tpproj_lei_use_case = (
            register_abginvest_tpproj_lei_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            # If query

            body_params = http_request.body.keys()

            if (
                "investment_approach_id" in body_params
                and "type_project_id" in body_params
                and "law_id" in body_params
            ):
                investment_approach_id = http_request.body["investment_approach_id"]
                type_project_id = http_request.body["type_project_id"]
                law_id = http_request.body["law_id"]

                response = self.register_abginvest_tpproj_lei_use_case.register(
                    investment_approach_id=investment_approach_id,
                    type_project_id=type_project_id,
                    law_id=law_id,
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
