from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import BenefitCategorizationType


class FindBenefitCategorizationTypeInterface(ABC):
    """Interface to Find BenefitCategorizationType use case"""

    @abstractmethod
    def by_id(self, id: str) -> Dict[bool, List[BenefitCategorizationType]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def all(self) -> Dict[bool, List[BenefitCategorizationType]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
