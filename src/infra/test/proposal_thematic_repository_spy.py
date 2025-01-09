from src.data.interface import ProposalThematicRepositoryInterface
from src.domain.models import ProposalThematic
from src.domain.test import mock_proposal_thematic


class ProposalThematicRepositorySpy(ProposalThematicRepositoryInterface):
    """Spy to ProposalThematic Repository"""

    def __init__(self):
        self.insert_proposal_thematic_params = {}

    def insert_proposal_thematic(
        self, proposal_id: str, thematic_id: int
    ) -> ProposalThematic:
        """Spy to all the attributes"""

        self.insert_proposal_thematic_params["proposal_id"] = proposal_id
        self.insert_proposal_thematic_params["thematic_id"] = thematic_id

        return mock_proposal_thematic()
