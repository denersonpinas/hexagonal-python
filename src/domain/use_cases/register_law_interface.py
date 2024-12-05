from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import Law


class RegisterLawInterface(ABC):
    """Interface to Register Law use case"""

    @abstractmethod
    def register(self, nome: str, descricao: str) -> Dict[bool, Law]:
        """Use Case"""

        raise Exception("Should implement method: register")
