from src.data.interface import SupplyHistoryRepositoryInterface
from src.domain.models import SupplyHistory
from src.domain.test import mock_supply_history


class SupplyHistoryRepositorySpy(SupplyHistoryRepositoryInterface):
    """Spy to SupplyHistory Repository"""

    def __init__(self):
        self.insert_supply_history_params = {}

    def insert_supply_history(
        self, service_provided: str, hiring_manager: str, proposal_id: str
    ) -> SupplyHistory:
        """Spy to all the attributes"""

        self.insert_supply_history_params["service_provided"] = service_provided
        self.insert_supply_history_params["hiring_manager"] = hiring_manager
        self.insert_supply_history_params["proposal_id"] = proposal_id

        return mock_supply_history()
