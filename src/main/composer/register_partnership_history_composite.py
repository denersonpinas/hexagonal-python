from src.data.register_partnership_history import RegisterPartnershipHistory
from src.infra.repo import PartnershipHistoryRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterPartnershipHistoryController


def register_partnership_history_composer() -> RouteInterface:
    """Composing Register PartnershipHistory Route
    :param  -   None
    :return -   Object with Register PartnershipHistory Route
    """

    repository = PartnershipHistoryRepository()
    use_case = RegisterPartnershipHistory(repository)
    register_partnership_history_route = RegisterPartnershipHistoryController(use_case)

    return register_partnership_history_route
