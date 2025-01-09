from sqlalchemy import UUID
from src.data.interface import ProposalInvestmentTypeLawRepositoryInterface
from src.domain.models import ProposalInvestmentTypeLaw
from src.domain.test import mock_proposal_investment_type_law


class ProposalInvestmentTypeLawRepositorySpy(
    ProposalInvestmentTypeLawRepositoryInterface
):
    """Spy to ProposalInvestmentTypeLaw Repository"""

    def __init__(self):
        self.insert_proposal_investment_type_law_params = {}

    def insert_proposal_investment_type_law(
        self, id: UUID, investment_type_law_id: int, proposal_id: UUID
    ) -> ProposalInvestmentTypeLaw:
        """Spy to all the attributes"""

        self.insert_proposal_investment_type_law_params["id"] = id
        self.insert_proposal_investment_type_law_params["investment_type_law_id"] = (
            investment_type_law_id
        )
        self.insert_proposal_investment_type_law_params["proposal_id"] = proposal_id

        return mock_proposal_investment_type_law()
