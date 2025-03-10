from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import SupplyHistory


class RegisterSupplyHistoryInterface(ABC):
    """Interface to Register SupplyHistory use case"""

    @abstractmethod
    def register(
        self, service_provided: str, hiring_manager: str, proposal_id: UUID
    ) -> Dict[bool, SupplyHistory]:
        """Use Case"""

        raise Exception("Should implement method: register")
