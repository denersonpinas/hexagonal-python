from src.data.find_relationship_category_counterparts import (
    FindRelationshipCategoryCounterparts,
)
from src.infra.repo import RelationshipCategoryCounterpartsRepository
from src.presenters.controllers import FindRelationshipCategoryCounterpartsController


def find_relationship_category_counterparts_composer() -> (
    FindRelationshipCategoryCounterpartsController
):
    """Composing Find RelationshipCategoryCounterparts Route
    :param  - None
    :return - Object with Find RelationshipCategoryCounterparts Route
    """

    repository = RelationshipCategoryCounterpartsRepository()
    use_case = FindRelationshipCategoryCounterparts(repository)
    find_RelationshipCategoryCounterparts_route = (
        FindRelationshipCategoryCounterpartsController(use_case)
    )

    return find_RelationshipCategoryCounterparts_route
