from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.domain.models import ProposalExecutionLocation


class ProposalExecutionLocationRepositoryInterface(ABC):
    """Interface to ProposalExecutionLocation Repository"""

    @abstractmethod
    def insert_proposal_execution_location(
        cls, city_id: int, proposal_id: UUID
    ) -> ProposalExecutionLocation:
        """abstractmethod"""
        raise Exception("Method not implemented")
