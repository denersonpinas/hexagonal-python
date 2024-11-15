from typing import Type

from src.domain.use_cases import FindCounterpartInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


class FindCounterpartController:
    """Class to define controller to find counterpart use case"""

    def __init__(self, find_counterpart_use_case: Type[FindCounterpartInterface]):
        self.find_counterpart_use_case = find_counterpart_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = http_request.query.keys()

            if (
                "counterpart_id" in query_string_params
                and "required" in query_string_params
                and "default" in query_string_params
            ):
                counterpart_id = http_request.query["counterpart_id"]
                required = http_request.query["required"]
                default = http_request.query["default"]

                response = (
                    self.find_counterpart_use_case.by_id_and_required_and_default(
                        counterpart_id=counterpart_id,
                        required=required,
                        default=default,
                    )
                )

            elif (
                "counterpart_id" in query_string_params
                and "required" in query_string_params
                and "default" not in query_string_params
            ):
                counterpart_id = http_request.query["counterpart_id"]
                required = http_request.query["required"]

                response = self.find_counterpart_use_case.by_id_and_required(
                    counterpart_id=counterpart_id, required=required
                )

            elif (
                "counterpart_id" in query_string_params
                and "required" not in query_string_params
                and "default" in query_string_params
            ):
                counterpart_id = http_request.query["counterpart_id"]
                default = http_request.query["default"]

                response = self.find_counterpart_use_case.by_id_and_default(
                    counterpart_id=counterpart_id, default=default
                )

            elif (
                "counterpart_id" not in query_string_params
                and "required" in query_string_params
                and "default" in query_string_params
            ):
                required = http_request.query["required"]
                default = http_request.query["default"]

                response = self.find_counterpart_use_case.by_required_and_default(
                    required=required, default=default
                )

            elif (
                "counterpart_id" in query_string_params
                and "required" not in query_string_params
                and "default" not in query_string_params
            ):
                counterpart_id = http_request.query["counterpart_id"]

                response = self.find_counterpart_use_case.by_id(
                    counterpart_id=counterpart_id
                )

            elif (
                "counterpart_id" not in query_string_params
                and "required" in query_string_params
                and "default" not in query_string_params
            ):
                required = http_request.query["required"]

                response = self.find_counterpart_use_case.by_required(required=required)

            elif (
                "counterpart_id" not in query_string_params
                and "required" not in query_string_params
                and "default" in query_string_params
            ):
                default = http_request.query["default"]

                response = self.find_counterpart_use_case.by_default(default=default)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=response["Data"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If not query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error["status_code"], body=response)
