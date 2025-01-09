from typing import Type
from src.domain.use_cases.register_proposal_interface import RegisterProposalInterface
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterProposalController(RouteInterface):
    """Class to define route to register_proposal use case"""

    def __init__(
        self,
        register_proposal_use_case: Type[RegisterProposalInterface],
    ):
        self.register_proposal_use_case = register_proposal_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = [
                "titulo_projeto",
                "resumo_projeto",
                "descricao_projeto",
                "dados_bancario_instituicao",
                "dados_bancario_agencia_conta_bancaria",
                "dados_bancario_conta_corrente",
            ]

            # Validate required parameters
            if all(param in body_params for param in required_params):
                response = self.register_proposal_use_case.register(
                    titulo_projeto=http_request.body["titulo_projeto"],
                    resumo_projeto=http_request.body["resumo_projeto"],
                    descricao_projeto=http_request.body["descricao_projeto"],
                    dados_bancario_instituicao=http_request.body[
                        "dados_bancario_instituicao"
                    ],
                    dados_bancario_agencia_conta_bancaria=http_request.body[
                        "dados_bancario_agencia_conta_bancaria"
                    ],
                    dados_bancario_conta_corrente=http_request.body[
                        "dados_bancario_conta_corrente"
                    ],
                    dados_bancario_cnpj_fundo=http_request.body.get(
                        "dados_bancario_cnpj_fundo"
                    ),
                    dados_bancario_razao_social_fundo=http_request.body.get(
                        "dados_bancario_razao_social_fundo"
                    ),
                    dados_bancario_contato_fundo_nome=http_request.body.get(
                        "dados_bancario_contato_fundo_nome"
                    ),
                    dados_bancario_contato_fundo_email=http_request.body.get(
                        "dados_bancario_contato_fundo_email"
                    ),
                    valor_total_projeto=float(
                        http_request.body.get("valor_total_projeto", 0.0)
                    ),
                    valor_total_lei_incentivo=float(
                        http_request.body.get("valor_total_lei_incentivo", 0.0)
                    ),
                    valor_total_captado=float(
                        http_request.body.get("valor_total_captado", 0.0)
                    ),
                    valor_total_captado_lei_incentivo=float(
                        http_request.body.get("valor_total_captado_lei_incentivo", 0.0)
                    ),
                    valor_total_incentivado_nubank=float(
                        http_request.body.get("valor_total_incentivado_nubank", 0.0)
                    ),
                    observacoes=http_request.body.get("observacoes", ""),
                    data_inicio_projeto=http_request.body.get(
                        "data_inicio_projeto", ""
                    ),
                    data_fim_projeto=http_request.body.get("data_fim_projeto", ""),
                )
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
