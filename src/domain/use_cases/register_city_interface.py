from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import City


class RegisterCityInterface(ABC):
    """Interface to Register City use case"""

    @abstractmethod
    def register(self, name: str, state: str) -> Dict[bool, City]:
        """Use Case"""

        raise Exception("Should implement method: register")
