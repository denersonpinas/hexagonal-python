from typing import Dict, Type

from src.data.interface import RelationshipCategoryCounterpartsRepositoryInterface
from src.domain.models import RelationshipCategoryCounterparts
from src.domain.test import mock_relationship_category_counterparts
from src.domain.use_cases import RegisterRelationshipCategoryCounterpartsInterface


class RegisterRelationshipCategoryCounterpartsSpy(
    RegisterRelationshipCategoryCounterpartsInterface
):
    "Class te define use case: Register Relationship Category Counterpart"

    def __init__(
        self,
        relationship_category_counterparts_repo: Type[
            RelationshipCategoryCounterpartsRepositoryInterface
        ],
    ):
        self._relationship_category_counterparts_repo = (
            relationship_category_counterparts_repo
        )
        self.registry_param = {}

    def registry(
        self, categoria_id: int, contrapartida_id: int
    ) -> Dict[bool, RelationshipCategoryCounterparts]:
        """Register relationhip category counterpart use case"""

        response = None
        validate_entry = isinstance(categoria_id, int) and isinstance(
            contrapartida_id, int
        )

        if validate_entry:
            self.registry_param["categoria_id"] = categoria_id
            self.registry_param["contrapartida_id"] = contrapartida_id

            response = mock_relationship_category_counterparts()

        return {"Success": validate_entry, "Data": response}
