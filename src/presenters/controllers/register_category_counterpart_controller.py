from typing import Type

from src.domain.use_cases import RegisterCategoryCounterpartInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterCategoryCounterpartController(RouteInterface):
    """Class to define route to register_category_counterpart use case"""

    def __init__(
        self,
        register_category_counterpart_use_case: Type[
            RegisterCategoryCounterpartInterface
        ],
    ):
        self.register_category_counterpart_use_case = (
            register_category_counterpart_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            # If query

            body_params = http_request.body.keys()

            if "name" in body_params and "description" in body_params:
                name = http_request.body["name"]
                description = http_request.body["description"]
                subcategory_id = None

                if "subcategory_id" in body_params:
                    subcategory_id = http_request.body["subcategory_id"]

                response = self.register_category_counterpart_use_case.registry(
                    nome=name, descricao=description, subcategoria_id=subcategory_id
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
