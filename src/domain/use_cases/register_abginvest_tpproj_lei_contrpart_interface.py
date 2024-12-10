from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import AbginvestTpprojLeiContrpart


class RegisterAbginvestTpprojLeiContrpartInterface(ABC):
    """Interface to Register AbginvestTpprojLeiContrpart use case"""

    @abstractmethod
    def register(
        self, ordem: int, id_relacao_contrapartida: int, id_abginvest_tpproj_lei: int
    ) -> Dict[bool, AbginvestTpprojLeiContrpart]:
        """Use Case"""

        raise Exception("Should implement method: register")
