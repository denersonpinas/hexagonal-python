from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProjectHistory


class RegisterProjectHistoryInterface(ABC):
    """Interface to Register ProjectHistory use case"""

    @abstractmethod
    def register(
        self, investment_year: int, title: str, investment_type: str, proposal_id: UUID
    ) -> Dict[bool, ProjectHistory]:
        """Use Case"""

        raise Exception("Should implement method: register")
