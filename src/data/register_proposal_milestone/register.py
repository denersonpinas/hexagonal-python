from typing import Dict, Type
from src.data.interface.proposal_milestone_repository_interface import (
    ProposalMilestoneRepositoryInterface,
)
from src.domain.use_cases.register_proposal_milestone_interface import (
    RegisterProposalMilestoneInterface,
)
from src.domain.models import ProposalMilestone


class RegisterProposalMilestone(RegisterProposalMilestoneInterface):
    """Class to define proposal milestone case: Register Proposal Milestone"""

    def __init__(
        self, proposal_milestone_repository: Type[ProposalMilestoneRepositoryInterface]
    ):
        self._proposal_milestone_repository = proposal_milestone_repository

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
            response = self._proposal_milestone_repository.insert_proposal_milestone(
                description=description,
                execution_date=execution_date,
                proposal_id=proposal_id,
            )

        return {"Success": validate_entry, "Data": response}
