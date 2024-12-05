from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import Thematic


class RegisterThematicInterface(ABC):
    """Interface to Register Thematic use case"""

    @abstractmethod
    def register(self, description: str) -> Dict[bool, Thematic]:
        """Use Case"""

        raise Exception("Should implement method: register")
