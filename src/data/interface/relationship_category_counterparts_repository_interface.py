from abc import ABC, abstractmethod
from typing import List

from src.domain.models import RelationshipCategoryCounterparts


class RelationshipCategoryCounterpartsRepositoryInterface(ABC):
    """Interface to Relationship Category Counterparts Repository"""

    @abstractmethod
    def insert_relationship_category_counterparts(
        self, categoria_id: int, contrapartida_id: int
    ) -> RelationshipCategoryCounterparts:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_relationship_category_counterparts(
        self,
    ) -> List[RelationshipCategoryCounterparts]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_relationship_category_counterparts(
        self, id: int = None, categoria_id: int = None, contrapartida_id: int = None
    ) -> List[RelationshipCategoryCounterparts]:
        """abstractmethod"""
        raise Exception("Method not implemented")
