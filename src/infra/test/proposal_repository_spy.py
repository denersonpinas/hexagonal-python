from typing import Optional

from sqlalchemy import UUID
from src.data.interface import ProposalRepositoryInterface
from src.domain.models import Proposal
from src.domain.test import mock_proposal


class ProposalRepositorySpy(ProposalRepositoryInterface):
    """Spy to Proposal Repository"""

    def __init__(self):
        self.insert_proposal_params = {}

    def insert_proposal(
        self,
        id: UUID,
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
    ) -> Proposal:
        """Spy to all the attributes"""

        self.insert_proposal_params["titulo_projeto"] = titulo_projeto
        self.insert_proposal_params["resumo_projeto"] = resumo_projeto
        self.insert_proposal_params["descricao_projeto"] = descricao_projeto
        self.insert_proposal_params["dados_bancario_instituicao"] = (
            dados_bancario_instituicao
        )
        self.insert_proposal_params["dados_bancario_agencia_conta_bancaria"] = (
            dados_bancario_agencia_conta_bancaria
        )
        self.insert_proposal_params["dados_bancario_conta_corrente"] = (
            dados_bancario_conta_corrente
        )
        self.insert_proposal_params["dados_bancario_cnpj_fundo"] = (
            dados_bancario_cnpj_fundo
        )
        self.insert_proposal_params["dados_bancario_razao_social_fundo"] = (
            dados_bancario_razao_social_fundo
        )
        self.insert_proposal_params["dados_bancario_contato_fundo_nome"] = (
            dados_bancario_contato_fundo_nome
        )
        self.insert_proposal_params["dados_bancario_contato_fundo_email"] = (
            dados_bancario_contato_fundo_email
        )
        self.insert_proposal_params["valor_total_projeto"] = valor_total_projeto
        self.insert_proposal_params["valor_total_lei_incentivo"] = (
            valor_total_lei_incentivo
        )
        self.insert_proposal_params["valor_total_captado"] = valor_total_captado
        self.insert_proposal_params["valor_total_captado_lei_incentivo"] = (
            valor_total_captado_lei_incentivo
        )
        self.insert_proposal_params["valor_total_incentivado_nubank"] = (
            valor_total_incentivado_nubank
        )
        self.insert_proposal_params["observacoes"] = observacoes
        self.insert_proposal_params["data_inicio_projeto"] = data_inicio_projeto
        self.insert_proposal_params["data_fim_projeto"] = data_fim_projeto

        return mock_proposal()
