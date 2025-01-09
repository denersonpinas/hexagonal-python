from typing import Dict, Type
from src.data.interface.proposal_thematic_repository_interface import (
    ProposalThematicRepositoryInterface,
)
from src.domain.use_cases.register_proposal_thematic_interface import (
    RegisterProposalThematicInterface,
)
from src.domain.models import ProposalThematic


class RegisterProposalThematic(RegisterProposalThematicInterface):
    """Class to define proposal thematic case: Register Proposal Thematic"""

    def __init__(
        self, proposal_thematic_repository: Type[ProposalThematicRepositoryInterface]
    ):
        self._proposal_thematic_repository = proposal_thematic_repository

    def register(
        self, proposal_id: str, thematic_id: int
    ) -> Dict[bool, ProposalThematic]:
        """Register proposal thematic use case
        :param  -   proposal_id: foreign key to proposal
                -   thematic_id: foreign key to thematic
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(proposal_id, str)
            and isinstance(thematic_id, int)
            and thematic_id > 0
        )

        if validate_entry:
            response = self._proposal_thematic_repository.insert_proposal_thematic(
                proposal_id=proposal_id, thematic_id=thematic_id
            )

        return {"Success": validate_entry, "Data": response}
