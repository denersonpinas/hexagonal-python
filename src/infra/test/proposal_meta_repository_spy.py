from sqlalchemy import UUID
from src.data.interface import PropostaMetaRepositoryInterface
from src.domain.models import ProposalMeta
from src.domain.test import mock_proposal_meta


class ProposalMetaRepositorySpy(PropostaMetaRepositoryInterface):
    """Spy to ProposalMeta Repository"""

    def __init__(self):
        self.insert_proposal_meta_params = {}

    def insert_proposal_meta(
        self, order: int, goal: str, quantity: int, proposal_id: UUID
    ) -> ProposalMeta:
        """Spy to all the attributes"""

        self.insert_proposal_meta_params["order"] = order
        self.insert_proposal_meta_params["goal"] = goal
        self.insert_proposal_meta_params["quantity"] = quantity
        self.insert_proposal_meta_params["proposal_id"] = proposal_id

        return mock_proposal_meta()
