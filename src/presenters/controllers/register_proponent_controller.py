from typing import Type
from src.domain.use_cases.register_proponent_interface import RegisterProponentInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterProponentController(RouteInterface):
    """Class to define route to register_proponent use case"""

    def __init__(
        self,
        register_proponent_use_case: Type[RegisterProponentInterface],
    ):
        self.register_proponent_use_case = register_proponent_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["cnpj", "proposal_id", "company_name"]

            if all(param in body_params for param in required_params):
                try:
                    response = self.register_proponent_use_case.register(
                        cnpj=http_request.body["cnpj"],
                        proposal_id=http_request.body["proposal_id"],
                        company_name=http_request.body["company_name"],
                        trade_name=http_request.body.get("trade_name"),
                        zip_code=http_request.body.get("zip_code"),
                        state=http_request.body.get("state"),
                        city=http_request.body.get("city"),
                        neighborhood=http_request.body.get("neighborhood"),
                        street=http_request.body.get("street"),
                        number=(
                            http_request.body.get("number")
                            if "number" in http_request.body
                            else None
                        ),
                        complement=http_request.body.get("complement"),
                        website=http_request.body.get("website"),
                        social_media=http_request.body.get("social_media"),
                        curriculum_summary=http_request.body.get("curriculum_summary"),
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
