from typing import List
from src.data.interface import RelationshipCategoryCounterpartsRepositoryInterface
from src.domain.models import RelationshipCategoryCounterparts
from src.domain.test import mock_relationship_category_counterparts


class RelationshipCategoryCounterpartsRepositorySpy(
    RelationshipCategoryCounterpartsRepositoryInterface
):
    """Spy to Relationship Category Counterpart Repository"""

    def __init__(self):
        self.insert_relationship_category_counterparts_params = {}
        self.select_relationship_category_counterparts_params = {}

    def insert_relationship_category_counterparts(
        self, categoria_id: int, contrapartida_id: int
    ) -> RelationshipCategoryCounterparts:
        """Spy to all the attributes"""

        self.insert_relationship_category_counterparts_params["categoria_id"] = (
            categoria_id
        )
        self.insert_relationship_category_counterparts_params["contrapartida_id"] = (
            contrapartida_id
        )

        return mock_relationship_category_counterparts()

    def select_relationship_category_counterparts(
        self, id: int = None, categoria_id: int = None, contrapartida_id: int = None
    ) -> List[RelationshipCategoryCounterparts]:
        """Spy to all the attributes"""

        self.select_relationship_category_counterparts_params["id"] = id
        self.select_relationship_category_counterparts_params["categoria_id"] = (
            categoria_id
        )
        self.select_relationship_category_counterparts_params["contrapartida_id"] = (
            contrapartida_id
        )

        return [mock_relationship_category_counterparts()]

    def select_all_relationship_category_counterparts(
        self,
    ) -> List[RelationshipCategoryCounterparts]:
        """Spy to all the attributes"""

        return [mock_relationship_category_counterparts()]
