from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProposalExecutionLocation


class RegisterProposalExecutionLocationInterface(ABC):
    """Interface to Register ProposalExecutionLocation use case"""

    @abstractmethod
    def register(
        self, city_id: int, proposal_id: UUID
    ) -> Dict[bool, ProposalExecutionLocation]:
        """Use Case"""

        raise Exception("Should implement method: register")
