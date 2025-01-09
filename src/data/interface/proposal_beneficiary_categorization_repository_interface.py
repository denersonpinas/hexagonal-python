from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.models import ProposalBeneficiaryCategorization


class ProposalBeneficiaryCategorizationRepositoryInterface(ABC):
    """Interface to ProposalBeneficiaryCategorization Repository"""

    @abstractmethod
    def insert_proposal_beneficiary_categorization(
        cls, categorizacao_id: int, proposta_beneficiario_id: UUID
    ) -> ProposalBeneficiaryCategorization:
        """abstractmethod"""
        raise Exception("Method not implemented")
