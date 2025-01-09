from abc import ABC, abstractmethod
from typing import Dict, Optional

from src.domain.models import PartnershipHistory


class RegisterPartnershipHistoryInterface(ABC):
    """Interface to Register PartnershipHistory use case"""

    @abstractmethod
    def register(
        self,
        sponsors_number: int,
        renewal_number: int,
        proposal_id: str,
        additional_info: Optional[str] = None,
    ) -> Dict[bool, PartnershipHistory]:
        """Use Case"""

        raise Exception("Should implement method: register")
