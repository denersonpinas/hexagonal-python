from typing import Type
from src.domain.use_cases.register_proposal_sponsor_interface import (
    RegisterProposalSponsorInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterProposalSponsorController(RouteInterface):
    """Class to define route to register_proposal_sponsor use case"""

    def __init__(
        self,
        register_proposal_sponsor_use_case: Type[RegisterProposalSponsorInterface],
    ):
        self.register_proposal_sponsor_use_case = register_proposal_sponsor_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["nome", "formato", "valor", "proposta_id"]

            if all(param in body_params for param in required_params):
                try:
                    nome = http_request.body["nome"]
                    formato = http_request.body["formato"]
                    valor = float(http_request.body["valor"])
                    proposta_id = http_request.body["proposta_id"]

                    response = self.register_proposal_sponsor_use_case.register(
                        nome=nome, formato=formato, valor=valor, proposta_id=proposta_id
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
