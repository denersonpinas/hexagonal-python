from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.models import ProposalBeneficiary


class ProposalBeneficiaryRepositoryInterface(ABC):
    """Interface to ProposalBeneficiary Repository"""

    @abstractmethod
    def insert_proposal_beneficiary(
        cls, id: UUID, quantidade: int, proposta_id: UUID
    ) -> ProposalBeneficiary:
        """abstractmethod"""
        raise Exception("Method not implemented")
