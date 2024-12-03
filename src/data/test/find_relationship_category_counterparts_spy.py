from typing import Dict, List, Type
from src.data.interface import RelationshipCategoryCounterpartsRepositoryInterface
from src.domain.models import RelationshipCategoryCounterparts
from src.domain.test import mock_relationship_category_counterparts
from src.domain.use_cases import FindRelationshipCategoryCounterpartsInterface


class FindRelationshipCategoryCounterpartsSpy(
    FindRelationshipCategoryCounterpartsInterface
):
    """Class to define use case: Select RelationshipCategoryCounterpart Spy"""

    def __init__(
        self,
        relationship_category_counterparts_repository: Type[
            RelationshipCategoryCounterpartsRepositoryInterface
        ],
    ):
        self.relationship_category_counterparts_repository = (
            relationship_category_counterparts_repository
        )
        self.by_id_param = {}
        self.by_category_param = {}
        self.by_counterpart_param = {}

    def by_id(self, id: int) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Select Relationship Category Counterpart by id spy"""

        self.by_id_param["id"] = id
        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = [mock_relationship_category_counterparts()]

        return {"Success": validate_entry, "Data": response}

    def by_category(
        self, category_id: int
    ) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Select Relationship Category Counterpart by is id category"""

        self.by_category_param["category_id"] = category_id
        response = None
        validate_entry = isinstance(category_id, int)

        if validate_entry:
            response = [mock_relationship_category_counterparts()]

        return {"Success": validate_entry, "Data": response}

    def by_counterpart(
        self, counterpart_id: int
    ) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Select Relationship Category Counterpart by is id counterpart"""

        self.by_counterpart_param["counterpart_id"] = counterpart_id
        response = None
        validate_entry = isinstance(counterpart_id, int)

        if validate_entry:
            response = [mock_relationship_category_counterparts()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Select all Relationship Category Counterpart spy"""

        response = [mock_relationship_category_counterparts()]

        return {"Success": True, "Data": response}
