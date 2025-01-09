from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import Neighborhood


class RegisterNeighborhoodInterface(ABC):
    """Interface to Register Neighborhood use case"""

    @abstractmethod
    def register(self, name: str, city_id: int) -> Dict[bool, Neighborhood]:
        """Use Case"""

        raise Exception("Should implement method: register")
