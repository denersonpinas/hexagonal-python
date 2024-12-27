from src.data.register_category_counterpart import RegisterCategoryCounterpart
from src.infra.repo import CategoryCounterpartRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterCategoryCounterpartController


def register_category_counterpart_composer() -> RouteInterface:
    """Composing Register CategoryCounterpart Route
    :param  -   None
    :return -   Object with Register CategoryCounterpart Route
    """

    repository = CategoryCounterpartRepository()
    use_case = RegisterCategoryCounterpart(repository)
    register_category_counterpart_route = RegisterCategoryCounterpartController(
        use_case
    )

    return register_category_counterpart_route
