from abc import ABC, abstractmethod
from typing import Dict, Optional

from sqlalchemy import UUID

from src.domain.models import ProposalCounterpart


class RegisterProposalCounterpartInterface(ABC):
    """Interface to Register ProposalCounterpart use case"""

    @abstractmethod
    def register(
        self,
        description: str,
        quantity: int,
        investment_type_law_counterpart_id: int,
        proposal_investment_type_law_id: UUID,
        expected: Optional[int] = None,
    ) -> Dict[bool, ProposalCounterpart]:
        """Use Case"""

        raise Exception("Should implement method: register")
