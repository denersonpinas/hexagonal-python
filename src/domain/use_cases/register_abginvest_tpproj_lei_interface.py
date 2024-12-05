from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import AbginvestTpprojLei


class RegisterAbginvestTpprojLeiInterface(ABC):
    """Interface to Register AbginvestTpprojLei use case"""

    @abstractmethod
    def register(
        self, investment_approach_id: int, type_project_id: int, law_id: int
    ) -> Dict[bool, AbginvestTpprojLei]:
        """Use Case"""

        raise Exception("Should implement method: register")
