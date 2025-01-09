from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProposalBeneficiary


class RegisterProposalBeneficiaryInterface(ABC):
    """Interface to Register ProposalBeneficiary use case"""

    @abstractmethod
    def register(
        self, quantidade: int, proposta_id: UUID
    ) -> Dict[bool, ProposalBeneficiary]:
        """Use Case"""

        raise Exception("Should implement method: register")
