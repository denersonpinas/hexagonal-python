from typing import Type

from src.domain.use_cases import FindAbginvestTpprojLeiInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


class FindAbginvestTpprojLeiController(RouteInterface):
    """Class to define controller to find AbginvestTpprojLei use case"""

    def __init__(
        self, find_abginvest_tpproj_lei_use_case: Type[FindAbginvestTpprojLeiInterface]
    ):
        self.find_abginvest_tpproj_lei_use_case = find_abginvest_tpproj_lei_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            # If query

            query_string_params = http_request.query.keys()
            if (
                "id" in query_string_params
                and "investment_approach_id" not in query_string_params
                and "type_project_id" not in query_string_params
                and "law_id" not in query_string_params
            ):
                id = http_request.query["id"]

                response = self.find_abginvest_tpproj_lei_use_case.by_id(id=id)

            elif (
                "investment_approach_id" in query_string_params
                and "id" not in query_string_params
                and "type_project_id" not in query_string_params
                and "law_id" not in query_string_params
            ):
                investment_approach_id = http_request.query["investment_approach_id"]

                response = (
                    self.find_abginvest_tpproj_lei_use_case.by_investment_approach(
                        investment_approach_id=investment_approach_id
                    )
                )

            elif (
                "type_project_id" in query_string_params
                and "investment_approach_id" not in query_string_params
                and "id" not in query_string_params
                and "law_id" not in query_string_params
            ):
                type_project_id = http_request.query["type_project_id"]

                response = self.find_abginvest_tpproj_lei_use_case.by_type_project(
                    type_project_id=type_project_id
                )

            elif (
                "law_id" in query_string_params
                and "investment_approach_id" not in query_string_params
                and "type_project_id" not in query_string_params
                and "id" not in query_string_params
            ):
                law_id = http_request.query["law_id"]

                response = self.find_abginvest_tpproj_lei_use_case.by_law(law_id=law_id)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        response = self.find_abginvest_tpproj_lei_use_case.all()
        return HttpResponse(status_code=200, body=response["Data"])
