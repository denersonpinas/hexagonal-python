from typing import Dict, List, Type
from src.data.interface import RelationshipCategoryCounterpartsRepositoryInterface
from src.domain.models import RelationshipCategoryCounterparts
from src.domain.use_cases import FindRelationshipCategoryCounterpartsInterface


class FindRelationshipCategoryCounterparts(
    FindRelationshipCategoryCounterpartsInterface
):
    """Class to define use case Find Relationship Category Counterpart"""

    def __init__(
        self,
        relationship_category_counterparts_repo: Type[
            RelationshipCategoryCounterpartsRepositoryInterface
        ],
    ):
        self.relationship_category_counterparts_repo = (
            relationship_category_counterparts_repo
        )

    def by_id(self, id: int) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Select Relationship Category Counterpart by id
        :param  -   id: id of the register
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = self.relationship_category_counterparts_repo.select_relationship_category_counterparts(
                id=id
            )

        return {"Success": validate_entry, "Data": response}

    def by_category(
        self, category_id: int
    ) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Select Relationship Category Counterpart by id
        :param  -   category_id: id category of the relationship category counterpart
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(category_id, int)

        if validate_entry:
            response = self.relationship_category_counterparts_repo.select_relationship_category_counterparts(
                categoria_id=category_id
            )

        return {"Success": validate_entry, "Data": response}

    def by_counterpart(
        self, counterpart_id: int
    ) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Select Relationship Category Counterpart by id
        :param  -   counterpart_id: id counterpart of the relationship category counterpart
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(counterpart_id, int)

        if validate_entry:
            response = self.relationship_category_counterparts_repo.select_relationship_category_counterparts(
                contrapartida_id=counterpart_id
            )

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[RelationshipCategoryCounterparts]]:
        """Select all Relationship Category Counterpart
        :param  -   is None
        :return -   Dictionary with informations od the process
        """

        response = (
            self.relationship_category_counterparts_repo.select_all_relationship_category_counterparts()
        )

        return {"Success": True, "Data": response}
