from typing import Type

from src.domain.use_cases import RegisterAbginvestTpprojLeiContrpartInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterAbginvestTpprojLeiContrpartController(RouteInterface):
    """Class to define route to register_abginvest_tpproj_lei_contrpart use case"""

    def __init__(
        self,
        register_abginvest_tpproj_lei_contrpart_use_case: Type[
            RegisterAbginvestTpprojLeiContrpartInterface
        ],
    ):
        self.register_abginvest_tpproj_lei_contrpart_use_case = (
            register_abginvest_tpproj_lei_contrpart_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            # If query

            body_params = http_request.body.keys()

            if (
                "order" in body_params
                and "id_relacao_contrapartida" in body_params
                and "id_abginvest_tpproj_lei" in body_params
            ):
                order = http_request.body["order"]
                id_relacao_contrapartida = http_request.body["id_relacao_contrapartida"]
                id_abginvest_tpproj_lei = http_request.body["id_abginvest_tpproj_lei"]

                response = (
                    self.register_abginvest_tpproj_lei_contrpart_use_case.register(
                        ordem=order,
                        id_relacao_contrapartida=id_relacao_contrapartida,
                        id_abginvest_tpproj_lei=id_abginvest_tpproj_lei,
                    )
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
