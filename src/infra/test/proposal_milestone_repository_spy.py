from src.data.interface import ProposalMilestoneRepositoryInterface
from src.domain.models import ProposalMilestone
from src.domain.test import mock_proposal_milestone


class ProposalMilestoneRepositorySpy(ProposalMilestoneRepositoryInterface):
    """Spy to ProposalMilestone Repository"""

    def __init__(self):
        self.insert_proposal_milestone_params = {}

    def insert_proposal_milestone(
        self, description: str, execution_date: str, proposal_id: str
    ) -> ProposalMilestone:
        """Spy to all the attributes"""

        self.insert_proposal_milestone_params["description"] = description
        self.insert_proposal_milestone_params["execution_date"] = execution_date
        self.insert_proposal_milestone_params["proposal_id"] = proposal_id

        return mock_proposal_milestone()
