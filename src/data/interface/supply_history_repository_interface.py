from abc import ABC, abstractmethod

from src.domain.models import SupplyHistory


class SupplyHistoryRepositoryInterface(ABC):
    """Interface to SupplyHistory Repository"""

    @abstractmethod
    def insert_supply_history(
        cls, service_provided: str, hiring_manager: str, proposal_id: str
    ) -> SupplyHistory:
        """abstractmethod"""
        raise Exception("Method not implemented")
