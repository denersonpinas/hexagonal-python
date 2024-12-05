from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import RelationshipCategoryCounterparts


class RegisterRelationshipCategoryCounterpartsInterface(ABC):
    """Interface to Register Relationship Category Counterparts use case"""

    @abstractmethod
    def register(
        self, categoria_id: int, contrapartida_id: int
    ) -> Dict[bool, RelationshipCategoryCounterparts]:
        """Use Case"""

        raise Exception("Should implement method: register")
