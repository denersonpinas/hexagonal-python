from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.models import ProposalSponsor


class ProposalSponsorRepositoryInterface(ABC):
    """Interface to ProposalSponsor Repository"""

    @abstractmethod
    def insert_proposal_sponsor(
        cls, nome: str, formato: str, valor: float, proposta_id: UUID
    ) -> ProposalSponsor:
        """abstractmethod"""
        raise Exception("Method not implemented")
