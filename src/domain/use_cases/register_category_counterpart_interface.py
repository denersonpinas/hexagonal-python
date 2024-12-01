from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import CategoryCounterpart


class RegisterCategoryCounterpartInterface(ABC):
    """Interface to Register Category Counterpart use case"""

    @abstractmethod
    def registry(
        self, nome: str, descricao: str, subcategoria_id: int = None
    ) -> Dict[bool, CategoryCounterpart]:
        """Use Case"""

        raise Exception("Should implement method: register")
