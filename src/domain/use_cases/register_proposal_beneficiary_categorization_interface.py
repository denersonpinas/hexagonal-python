from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProposalBeneficiaryCategorization


class RegisterProposalBeneficiaryCategorizationInterface(ABC):
    """Interface to Register ProposalBeneficiaryCategorization use case"""

    @abstractmethod
    def register(
        self, categorizacao_id: int, proposta_beneficiario_id: UUID
    ) -> Dict[bool, ProposalBeneficiaryCategorization]:
        """Use Case"""

        raise Exception("Should implement method: register")
