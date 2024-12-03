from typing import Type

from src.domain.use_cases import RegisterRelationshipCategoryCounterpartsInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterRelationshipCategoryCounterpartsController(RouteInterface):
    """Class to define route to register_relationship_category_counterparts use case"""

    def __init__(
        self,
        register_relationship_category_counterparts_use_case: Type[
            RegisterRelationshipCategoryCounterpartsInterface
        ],
    ):
        self.register_relationship_category_counterparts_use_case = (
            register_relationship_category_counterparts_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            # If query

            body_params = http_request.body.keys()

            if "category_id" in body_params and "counterpart_id" in body_params:
                category_id = http_request.body["category_id"]
                counterpart_id = http_request.body["counterpart_id"]

                response = (
                    self.register_relationship_category_counterparts_use_case.registry(
                        categoria_id=category_id, contrapartida_id=counterpart_id
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
