from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProposalMeta


class RegisterProposalMetaInterface(ABC):
    """Interface to Register ProposalMeta use case"""

    @abstractmethod
    def register(
        self, order: int, goal: str, quantity: int, proposal_id: UUID
    ) -> Dict[bool, ProposalMeta]:
        """Use Case"""

        raise Exception("Should implement method: register")
