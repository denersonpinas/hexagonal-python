from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProposalInvestmentTypeLaw


class RegisterProposalInvestmentTypeLawInterface(ABC):
    """Interface to Register ProposalInvestmentTypeLaw use case"""

    @abstractmethod
    def register(
        self, investment_type_law_id: int, proposal_id: UUID
    ) -> Dict[bool, ProposalInvestmentTypeLaw]:
        """Use Case"""

        raise Exception("Should implement method: register")
