from src.data.register_counterpart import RegisterCounterpart
from src.infra.repo import CounterpartRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterCounterpartController


def register_counterpart_composer() -> RouteInterface:
    """Composing Register Counterpart Route
    :param  -   None
    :return -   Object with Register Counterpart Route
    """

    repository = CounterpartRepository()
    use_case = RegisterCounterpart(repository)
    register_counterpart_route = RegisterCounterpartController(use_case)

    return register_counterpart_route
