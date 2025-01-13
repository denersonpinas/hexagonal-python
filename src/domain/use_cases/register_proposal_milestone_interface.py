from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProposalMilestone


class RegisterProposalMilestoneInterface(ABC):
    """Interface to Register ProposalMilestone use case"""

    @abstractmethod
    def register(
        self, description: str, execution_date: str, proposal_id: UUID
    ) -> Dict[bool, ProposalMilestone]:
        """Use Case"""

        raise Exception("Should implement method: register")
