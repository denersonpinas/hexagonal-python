from typing import Dict, Optional, Type

from src.data.interface import ProposalRepositoryInterface
from src.domain.models import Proposal
from src.domain.test import mock_proposal
from src.domain.use_cases import RegisterProposalInterface


class RegisterProposalSpy(RegisterProposalInterface):
    "Class te define use case: Register Proposal"

    def __init__(self, proposal_repository: Type[ProposalRepositoryInterface]):
        self._proposal_repository = proposal_repository
        self.register_param = {}

    def register(
        self,
        titulo_projeto: str,
        resumo_projeto: str,
        descricao_projeto: str,
        dados_bancario_instituicao: str,
        dados_bancario_agencia_conta_bancaria: str,
        dados_bancario_conta_corrente: str,
        dados_bancario_cnpj_fundo: Optional[str] = None,
        dados_bancario_razao_social_fundo: Optional[str] = None,
        dados_bancario_contato_fundo_nome: Optional[str] = None,
        dados_bancario_contato_fundo_email: Optional[str] = None,
        valor_total_projeto: float = 0.0,
        valor_total_lei_incentivo: float = 0.0,
        valor_total_captado: float = 0.0,
        valor_total_captado_lei_incentivo: float = 0.0,
        valor_total_incentivado_nubank: float = 0.0,
        observacoes: str = "",
        data_inicio_projeto: str = "",
        data_fim_projeto: str = "",
    ) -> Dict[bool, Proposal]:
        """Register proposal use case
        :param  -   id: project id
                -   titulo_projeto: project title
                -   resumo_projeto: project summary
                -   descricao_projeto: project description
                -   dados_bancario_instituicao: bank institution
                -   dados_bancario_agencia_conta_bancaria: agency and account
                -   dados_bancario_conta_corrente: current account
                -   dados_bancario_cnpj_fundo: fund CNPJ (optional)
                -   dados_bancario_razao_social_fundo: fund legal name (optional)
                -   dados_bancario_contato_fundo_nome: fund contact name (optional)
                -   dados_bancario_contato_fundo_email: fund contact email (optional)
                -   valor_total_projeto: total project value
                -   valor_total_lei_incentivo: total incentive law value
                -   valor_total_captado: total captured value
                -   valor_total_captado_lei_incentivo: total captured incentive value
                -   valor_total_incentivado_nubank: total Nubank incentive value
                -   observacoes: observations
                -   data_inicio_projeto: project start date
                -   data_fim_projeto: project end date
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(titulo_projeto, str)
            and isinstance(resumo_projeto, str)
            and isinstance(descricao_projeto, str)
            and isinstance(dados_bancario_instituicao, str)
            and isinstance(dados_bancario_agencia_conta_bancaria, str)
            and isinstance(dados_bancario_conta_corrente, str)
            and isinstance(valor_total_projeto, float)
            and isinstance(valor_total_lei_incentivo, float)
            and isinstance(valor_total_captado, float)
            and isinstance(valor_total_captado_lei_incentivo, float)
            and isinstance(valor_total_incentivado_nubank, float)
            and len(titulo_projeto) <= 100
            and len(resumo_projeto) <= 500
            and len(descricao_projeto) <= 1000
        )

        if validate_entry:
            self.register_param["titulo_projeto"] = titulo_projeto
            self.register_param["resumo_projeto"] = resumo_projeto
            self.register_param["descricao_projeto"] = descricao_projeto
            self.register_param["dados_bancario_instituicao"] = (
                dados_bancario_instituicao
            )
            self.register_param["dados_bancario_agencia_conta_bancaria"] = (
                dados_bancario_agencia_conta_bancaria
            )
            self.register_param["dados_bancario_conta_corrente"] = (
                dados_bancario_conta_corrente
            )
            self.register_param["dados_bancario_cnpj_fundo"] = dados_bancario_cnpj_fundo
            self.register_param["dados_bancario_razao_social_fundo"] = (
                dados_bancario_razao_social_fundo
            )
            self.register_param["dados_bancario_contato_fundo_nome"] = (
                dados_bancario_contato_fundo_nome
            )
            self.register_param["dados_bancario_contato_fundo_email"] = (
                dados_bancario_contato_fundo_email
            )
            self.register_param["valor_total_projeto"] = valor_total_projeto
            self.register_param["valor_total_lei_incentivo"] = valor_total_lei_incentivo
            self.register_param["valor_total_captado"] = valor_total_captado
            self.register_param["valor_total_captado_lei_incentivo"] = (
                valor_total_captado_lei_incentivo
            )
            self.register_param["valor_total_incentivado_nubank"] = (
                valor_total_incentivado_nubank
            )
            self.register_param["observacoes"] = observacoes
            self.register_param["data_inicio_projeto"] = data_inicio_projeto
            self.register_param["data_fim_projeto"] = data_fim_projeto

            response = mock_proposal()

        return {"Success": validate_entry, "Data": response}
