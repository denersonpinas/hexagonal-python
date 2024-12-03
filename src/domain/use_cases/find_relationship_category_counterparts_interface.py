from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import RelationshipCategoryCounterparts


class FindRelationshipCategoryCounterpartsInterface(ABC):
    """Interface to Find Relationship Category Counterpart use case"""

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_category(
        self, category_id: int
    ) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Specific Case"""

        raise Exception("Should implement method: by_category")

    @abstractmethod
    def by_counterpart(
        self, counterpart_id: int
    ) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Specific Case"""

        raise Exception("Should implement method: by_counterpart")

    @abstractmethod
    def all(self) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
