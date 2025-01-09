from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from src.domain.models import Proposal


class ProposalRepositoryInterface(ABC):
    """Interface to Proposal Repository"""

    @abstractmethod
    def insert_proposal(
        cls,
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
        """abstractmethod"""
        raise Exception("Method not implemented")
