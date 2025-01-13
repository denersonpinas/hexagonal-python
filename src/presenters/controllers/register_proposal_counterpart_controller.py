from typing import Type
from src.domain.use_cases.register_proposal_counterpart_interface import (
    RegisterProposalCounterpartInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterProposalCounterpartController(RouteInterface):
    """Class to define route to register_proposal_counterpart use case"""

    def __init__(
        self,
        register_proposal_counterpart_use_case: Type[
            RegisterProposalCounterpartInterface
        ],
    ):
        self.register_proposal_counterpart_use_case = (
            register_proposal_counterpart_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = [
                "description",
                "quantity",
                "investment_type_law_counterpart_id",
                "proposal_investment_type_law_id",
            ]

            if all(param in body_params for param in required_params):
                try:
                    description = http_request.body["description"]
                    quantity = int(http_request.body["quantity"])
                    investment_type_law_counterpart_id = int(
                        http_request.body["investment_type_law_counterpart_id"]
                    )
                    proposal_investment_type_law_id = http_request.body[
                        "proposal_investment_type_law_id"
                    ]
                    expected = (
                        int(http_request.body["expected"])
                        if "expected" in http_request.body
                        else None
                    )

                    response = self.register_proposal_counterpart_use_case.register(
                        description=description,
                        quantity=quantity,
                        investment_type_law_counterpart_id=investment_type_law_counterpart_id,
                        proposal_investment_type_law_id=proposal_investment_type_law_id,
                        expected=expected,
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
