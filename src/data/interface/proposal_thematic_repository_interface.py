from abc import ABC, abstractmethod

from src.domain.models import ProposalThematic


class ProposalThematicRepositoryInterface(ABC):
    """Interface to ProposalThematic Repository"""

    @abstractmethod
    def insert_proposal_thematic(
        cls, proposal_id: str, thematic_id: int
    ) -> ProposalThematic:
        """abstractmethod"""
        raise Exception("Method not implemented")
