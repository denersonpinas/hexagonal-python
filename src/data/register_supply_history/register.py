from typing import Dict, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.supply_history_repository_interface import (
    SupplyHistoryRepositoryInterface,
)
from src.domain.use_cases.register_supply_history_interface import (
    RegisterSupplyHistoryInterface,
)
from src.domain.models import SupplyHistory


class RegisterSupplyHistory(RegisterSupplyHistoryInterface):
    """Class to define supply history case: Register Supply History"""

    def __init__(
        self, supply_history_repository: Type[SupplyHistoryRepositoryInterface]
    ):
        self._supply_history_repository = supply_history_repository

    def register(
        self, service_provided: str, hiring_manager: str, proposal_id: UUID
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
            and isinstance(proposal_id, uuid.UUID)
            and len(service_provided) <= 500
            and len(hiring_manager) <= 100
        )

        if validate_entry:
            response = self._supply_history_repository.insert_supply_history(
                service_provided=service_provided,
                hiring_manager=hiring_manager,
                proposal_id=proposal_id,
            )

        return {"Success": validate_entry, "Data": response}
