from typing import Type

from src.domain.use_cases import FindCategoryCounterpartInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


class FindCategoryCounterpartController(RouteInterface):
    """Class to define controller to find category counterpart use case"""

    def __init__(
        self, find_category_counterpart_use_case: Type[FindCategoryCounterpartInterface]
    ):
        self.find_category_counterpart_use_case = find_category_counterpart_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = http_request.query.keys()
            if (
                "category_counterpart_id" in query_string_params
                and "subcategory_id" not in query_string_params
            ):
                category_counterpart_id = http_request.query["category_counterpart_id"]

                response = self.find_category_counterpart_use_case.by_id(
                    category_counterpart_id=category_counterpart_id
                )

            elif (
                "subcategory_id" in query_string_params
                and "category_counterpart_id" not in query_string_params
            ):
                subcategory_id = http_request.query["subcategory_id"]

                response = self.find_category_counterpart_use_case.by_subcategory(
                    subcategory_id=subcategory_id
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        response = self.find_category_counterpart_use_case.all()
        return HttpResponse(status_code=200, body=response["Data"])
