from typing import Dict, Type

from src.data.interface import ProposalMilestoneRepositoryInterface
from src.domain.models import ProposalMilestone
from src.domain.test import mock_proposal_milestone
from src.domain.use_cases import RegisterProposalMilestoneInterface


class RegisterProposalMilestoneSpy(RegisterProposalMilestoneInterface):
    "Class te define use case: Register ProposalMilestone"

    def __init__(
        self, proposal_milestone_repository: Type[ProposalMilestoneRepositoryInterface]
    ):
        self._proposal_milestone_repository = proposal_milestone_repository
        self.register_param = {}

    def register(
        self, description: str, execution_date: str, proposal_id: str
    ) -> Dict[bool, ProposalMilestone]:
        """Register proposal milestone use case
        :param  -   description: milestone description
                -   execution_date: milestone execution date
                -   proposal_id: foreign key to proposal
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(description, str)
            and isinstance(execution_date, str)
            and isinstance(proposal_id, str)
            and len(description) <= 500
            and len(execution_date) <= 10  # Assuming date format YYYY-MM-DD
        )

        if validate_entry:
            self.register_param["description"] = description
            self.register_param["execution_date"] = execution_date
            self.register_param["proposal_id"] = proposal_id

            response = mock_proposal_milestone()

        return {"Success": validate_entry, "Data": response}
