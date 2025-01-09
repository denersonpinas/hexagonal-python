from abc import ABC, abstractmethod
from typing import Optional

from src.domain.models import PartnershipHistory


class PartnershipHistoryRepositoryInterface(ABC):
    """Interface to PartnershipHistory Repository"""

    @abstractmethod
    def insert_partnership_history(
        cls,
        sponsors_number: int,
        renewal_number: int,
        proposal_id: str,
        additional_info: Optional[str] = None,
    ) -> PartnershipHistory:
        """abstractmethod"""
        raise Exception("Method not implemented")
