from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import Street


class RegisterStreetInterface(ABC):
    """Interface to Register Street use case"""

    @abstractmethod
    def register(self, name: str, neighborhood_id: int) -> Dict[bool, Street]:
        """Use Case"""

        raise Exception("Should implement method: register")
