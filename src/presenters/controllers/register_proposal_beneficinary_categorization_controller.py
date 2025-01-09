from typing import Type
import uuid
from src.domain.use_cases.register_proposal_beneficiary_categorization_interface import (
    RegisterProposalBeneficiaryCategorizationInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterProposalBeneficinaryCategorizationController(RouteInterface):
    """Class to define route to register_proposal_beneficiary_categorization use case"""

    def __init__(
        self,
        register_proposal_beneficiary_categorization_use_case: Type[
            RegisterProposalBeneficiaryCategorizationInterface
        ],
    ):
        self.register_proposal_beneficiary_categorization_use_case = (
            register_proposal_beneficiary_categorization_use_case
        )

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["categorizacao_id", "proposta_beneficiario_id"]

            if all(param in body_params for param in required_params):
                try:
                    categorizacao_id = http_request.body["categorizacao_id"]
                    proposta_beneficiario_id = uuid.UUID(
                        http_request.body["proposta_beneficiario_id"]
                    )

                    response = self.register_proposal_beneficiary_categorization_use_case.register(
                        categorizacao_id=categorizacao_id,
                        proposta_beneficiario_id=proposta_beneficiario_id,
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
