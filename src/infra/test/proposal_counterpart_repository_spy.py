from typing import Optional

from sqlalchemy import UUID
from src.data.interface import ProposalCounterpartRepositoryInterface
from src.domain.models import ProposalCounterpart
from src.domain.test import mock_proposal_counterpart


class ProposalCounterpartRepositorySpy(ProposalCounterpartRepositoryInterface):
    """Spy to ProposalCounterpart Repository"""

    def __init__(self):
        self.insert_proposal_counterpart_params = {}

    def insert_proposal_counterpart(
        self,
        id: UUID,
        description: str,
        quantity: int,
        investment_type_law_counterpart_id: int,
        proposal_investment_type_law_id: UUID,
        expected: Optional[int] = None,
    ) -> ProposalCounterpart:
        """Spy to all the attributes"""

        self.insert_proposal_counterpart_params["id"] = id
        self.insert_proposal_counterpart_params["description"] = description
        self.insert_proposal_counterpart_params["quantity"] = quantity
        self.insert_proposal_counterpart_params[
            "investment_type_law_counterpart_id"
        ] = investment_type_law_counterpart_id
        self.insert_proposal_counterpart_params["proposal_investment_type_law_id"] = (
            proposal_investment_type_law_id
        )
        self.insert_proposal_counterpart_params["expected"] = expected

        return mock_proposal_counterpart()
