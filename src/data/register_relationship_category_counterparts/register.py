from typing import Dict, Type
from src.data.interface import RelationshipCategoryCounterpartsRepositoryInterface
from src.domain.models import RelationshipCategoryCounterparts
from src.domain.use_cases import RegisterRelationshipCategoryCounterpartsInterface


class RegisterRelationshipCategoryCounterparts(
    RegisterRelationshipCategoryCounterpartsInterface
):
    """Class to define relationship category counterparts case: Register Relationship Category Counterparts"""

    def __init__(
        self,
        relationship_category_counterparts_repo: Type[
            RelationshipCategoryCounterpartsRepositoryInterface
        ],
    ):
        self._relationship_category_counterparts_repo = (
            relationship_category_counterparts_repo
        )

    def register(
        self, categoria_id: int, contrapartida_id: int
    ) -> Dict[bool, RelationshipCategoryCounterparts]:
        """Register relationship category counterpart use case
        :param  -   categoria_id: id category of the relationship category counterpart
                -   contrapartida_id: id counterpart of the relationship category counterpart
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(categoria_id, int) and isinstance(
            contrapartida_id, int
        )

        if validate_entry:
            response = self._relationship_category_counterparts_repo.insert_relationship_category_counterparts(
                categoria_id=categoria_id, contrapartida_id=contrapartida_id
            )

        return {"Success": validate_entry, "Data": response}
