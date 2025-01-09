from typing import Dict, Type

from src.data.interface import SupplyHistoryRepositoryInterface
from src.domain.models import SupplyHistory
from src.domain.test import mock_supply_history
from src.domain.use_cases import RegisterSupplyHistoryInterface


class RegisterSupplyHistorySpy(RegisterSupplyHistoryInterface):
    "Class te define use case: Register SupplyHistory"

    def __init__(
        self, supply_history_repository: Type[SupplyHistoryRepositoryInterface]
    ):
        self._supply_history_repository = supply_history_repository
        self.register_param = {}

    def register(
        self, service_provided: str, hiring_manager: str, proposal_id: str
    ) -> Dict[bool, SupplyHistory]:
        """Register supply history use case
        :param  -   service_provided: service provided description
                -   hiring_manager: hiring manager name
                -   proposal_id: foreign key to proposal
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(service_provided, str)
            and isinstance(hiring_manager, str)
            and isinstance(proposal_id, str)
            and len(service_provided) <= 500
            and len(hiring_manager) <= 100
        )

        if validate_entry:
            self.register_param["service_provided"] = service_provided
            self.register_param["hiring_manager"] = hiring_manager
            self.register_param["proposal_id"] = proposal_id

            response = mock_supply_history()

        return {"Success": validate_entry, "Data": response}
