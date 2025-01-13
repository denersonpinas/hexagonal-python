from src.data.register_supply_history import RegisterSupplyHistory
from src.infra.repo import SupplyHistoryRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterSupplyHistoryController


def register_supply_history_composer() -> RouteInterface:
    """Composing Register SupplyHistory Route
    :param  -   None
    :return -   Object with Register SupplyHistory Route
    """

    repository = SupplyHistoryRepository()
    use_case = RegisterSupplyHistory(repository)
    register_supply_history_route = RegisterSupplyHistoryController(use_case)

    return register_supply_history_route
