from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProposalSponsor


class RegisterProposalSponsorInterface(ABC):
    """Interface to Register ProposalSponsor use case"""

    @abstractmethod
    def register(
        self, nome: str, formato: str, valor: float, proposta_id: UUID
    ) -> Dict[bool, ProposalSponsor]:
        """Use Case"""

        raise Exception("Should implement method: register")
