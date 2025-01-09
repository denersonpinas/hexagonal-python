from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy import UUID

from src.domain.models import ProposalCounterpart


class ProposalCounterpartRepositoryInterface(ABC):
    """Interface to ProposalCounterpart Repository"""

    @abstractmethod
    def insert_proposal_counterpart(
        cls,
        id: UUID,
        description: str,
        quantity: int,
        investment_type_law_counterpart_id: int,
        proposal_investment_type_law_id: UUID,
        expected: Optional[int] = None,
    ) -> ProposalCounterpart:
        """abstractmethod"""
        raise Exception("Method not implemented")
