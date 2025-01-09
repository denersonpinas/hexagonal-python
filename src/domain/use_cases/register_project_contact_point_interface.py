from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy import UUID

from src.domain.models import ProjectContactPoint


class RegisterProjectContactPointInterface(ABC):
    """Interface to Register ProjectContactPoint use case"""

    @abstractmethod
    def register(
        self, name: str, email: str, position: str, proposal_id: UUID
    ) -> Dict[bool, ProjectContactPoint]:
        """Use Case"""

        raise Exception("Should implement method: register")
