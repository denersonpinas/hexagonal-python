from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import Counterpart


class RegisterCounterpartInterface(ABC):
    """Interface to Register Counterpart use case"""

    @abstractmethod
    def register(
        self, descricao: str, exemplo_aplicabilidade: str, obrigatoria: bool
    ) -> Dict[bool, Counterpart]:
        """Use Case"""

        raise Exception("Should implement method: register")
