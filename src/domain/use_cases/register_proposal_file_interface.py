from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProposalFile


class RegisterProposalFileInterface(ABC):
    """Interface to Register ProposalFile use case"""

    @abstractmethod
    def register(
        self,
        name: str,
        extension: str,
        size: int,
        uri: str,
        proposal_id: UUID,
        type_id: str,
    ) -> Dict[bool, ProposalFile]:
        """Use Case"""

        raise Exception("Should implement method: register")
