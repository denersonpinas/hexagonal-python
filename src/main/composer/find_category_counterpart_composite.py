from src.data.find_category_counterpart import FindCategoryCounterpart
from src.infra.repo import CategoryCounterpartRepository
from src.presenters.controllers import FindCategoryCounterpartController


def find_category_counterpart_composer() -> FindCategoryCounterpartController:
    """Composing Find CategoryCounterpart Route
    :param  - None
    :return - Object with Find CategoryCounterpart Route
    """

    repository = CategoryCounterpartRepository()
    use_case = FindCategoryCounterpart(repository)
    find_category_counterpart_route = FindCategoryCounterpartController(use_case)

    return find_category_counterpart_route
