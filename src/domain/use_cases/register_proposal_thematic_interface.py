from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import ProposalThematic


class RegisterProposalThematicInterface(ABC):
    """Interface to Register ProposalThematic use case"""

    @abstractmethod
    def register(
        self, proposal_id: str, thematic_id: int
    ) -> Dict[bool, ProposalThematic]:
        """Use Case"""

        raise Exception("Should implement method: register")
