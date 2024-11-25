from src.data.find_counterpart import FindCounterpart
from src.infra.repo import CounterpartRepository
from src.presenters.controllers import FindCounterpartController


def find_counterpart_composer() -> FindCounterpartController:
    """Composing Find Counterpart Route
    :param  - None
    :return - Object with Find Counterpart Route
    """

    repository = CounterpartRepository()
    use_case = FindCounterpart(repository)
    find_counterpart_route = FindCounterpartController(use_case)

    return find_counterpart_route
