from abc import ABC, abstractmethod

from src.domain.models import ProposalMilestone


class ProposalMilestoneRepositoryInterface(ABC):
    """Interface to ProposalMilestone Repository"""

    @abstractmethod
    def insert_proposal_milestone(
        cls, description: str, execution_date: str, proposal_id: str
    ) -> ProposalMilestone:
        """abstractmethod"""
        raise Exception("Method not implemented")
