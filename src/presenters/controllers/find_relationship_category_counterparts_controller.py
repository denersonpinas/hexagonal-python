from typing import Type

from src.domain.use_cases import FindRelationshipCategoryCounterpartsInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


class FindRelationshipCategoryCounterpartsController(RouteInterface):
    """Class to define controller to find relationship category counterpart use case"""

    def __init__(
        self,
        find_relationship_category_counterparts_use_case: Type[
            FindRelationshipCategoryCounterpartsInterface
        ],
    ):
        self.find_relationship_category_counterparts_use_case = (
            find_relationship_category_counterparts_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = http_request.query.keys()
            if (
                "id" in query_string_params
                and "category_id" not in query_string_params
                and "counterpart_id" not in query_string_params
            ):
                id = http_request.query["id"]

                response = self.find_relationship_category_counterparts_use_case.by_id(
                    id=id
                )

            elif (
                "category_id" in query_string_params
                and "id" not in query_string_params
                and "counterpart_id" not in query_string_params
            ):
                category_id = http_request.query["category_id"]

                response = (
                    self.find_relationship_category_counterparts_use_case.by_category(
                        category_id=category_id
                    )
                )

            elif (
                "counterpart_id" in query_string_params
                and "id" not in query_string_params
                and "category_id" not in query_string_params
            ):
                counterpart_id = http_request.query["counterpart_id"]

                response = self.find_relationship_category_counterparts_use_case.by_counterpart(
                    counterpart_id=counterpart_id
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        response = self.find_relationship_category_counterparts_use_case.all()
        return HttpResponse(status_code=200, body=response["Data"])
