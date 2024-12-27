from src.data.register_relationship_category_counterparts import (
    RegisterRelationshipCategoryCounterparts,
)
from src.infra.repo import RelationshipCategoryCounterpartsRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import (
    RegisterRelationshipCategoryCounterpartsController,
)


def register_relationship_category_counterpart_composer() -> RouteInterface:
    """Composing Register RelationshipCategoryCounterparts Route
    :param  -   None
    :return -   Object with Register RelationshipCategoryCounterparts Route
    """

    repository = RelationshipCategoryCounterpartsRepository()
    use_case = RegisterRelationshipCategoryCounterparts(repository)
    register_relationship_category_counterpart_route = (
        RegisterRelationshipCategoryCounterpartsController(use_case)
    )

    return register_relationship_category_counterpart_route
