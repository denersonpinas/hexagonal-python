from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import BenefitCategorization


class FindBenefitCategorizationInterface(ABC):
    """Interface to Find BenefitCategorization use case"""

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[BenefitCategorization]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_type(self, type_id: str) -> Dict[bool, List[BenefitCategorization]]:
        """Specific Case"""

        raise Exception("Should implement method: by_type")

    @abstractmethod
    def all(self) -> Dict[bool, List[BenefitCategorization]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
