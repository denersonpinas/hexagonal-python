from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import TypeFile


class RegisterTypeFileInterface(ABC):
    """Interface to Register TypeFile use case"""

    @abstractmethod
    def register(
        self, id: str, context: str, description: str, info: str
    ) -> Dict[bool, TypeFile]:
        """Use Case"""

        raise Exception("Should implement method: register")
