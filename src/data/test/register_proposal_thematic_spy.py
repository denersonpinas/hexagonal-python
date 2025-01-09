from typing import Dict, Type

from src.data.interface import ProposalThematicRepositoryInterface
from src.domain.models import ProposalThematic
from src.domain.test import mock_proposal_thematic
from src.domain.use_cases import RegisterProposalThematicInterface


class RegisterProposalThematicSpy(RegisterProposalThematicInterface):
    "Class te define use case: Register Law"

    def __init__(
        self, proposal_thematic_repository: Type[ProposalThematicRepositoryInterface]
    ):
        self._proposal_thematic_repository = proposal_thematic_repository
        self.register_param = {}

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
            self.register_param["proposal_id"] = proposal_id
            self.register_param["thematic_id"] = thematic_id

            response = mock_proposal_thematic()

        return {"Success": validate_entry, "Data": response}
