from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.models import ProposalMeta


class PropostaMetaRepositoryInterface(ABC):
    """Interface to ProposalMeta Repository"""

    @abstractmethod
    def insert_proposal_meta(
        cls, order: int, goal: str, quantity: int, proposal_id: UUID
    ) -> ProposalMeta:
        """abstractmethod"""
        raise Exception("Method not implemented")
