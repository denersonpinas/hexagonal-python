from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import TypeProject


class RegisterTypeProjectInterface(ABC):
    """Interface to Register TypeProject use case"""

    @abstractmethod
    def register(self, nome: str, descricao: str) -> Dict[bool, TypeProject]:
        """Use Case"""

        raise Exception("Should implement method: register")
