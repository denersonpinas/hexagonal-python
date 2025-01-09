from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.domain.models import ProposalInvestmentTypeLaw


class ProposalInvestmentTypeLawRepositoryInterface(ABC):
    """Interface to ProposalInvestmentTypeLaw Repository"""

    @abstractmethod
    def insert_proposal_investment_type_law(
        cls, id: UUID, investment_type_law_id: int, proposal_id: UUID
    ) -> ProposalInvestmentTypeLaw:
        """abstractmethod"""
        raise Exception("Method not implemented")
