from sqlalchemy import UUID
from src.data.interface import ProposalFileRepositoryInterface
from src.domain.models import ProposalFile
from src.domain.test import mock_proposal_file


class ProposalFileRepositorySpy(ProposalFileRepositoryInterface):
    """Spy to ProposalFile Repository"""

    def __init__(self):
        self.insert_proposal_file_params = {}

    def insert_proposal_file(
        self,
        id: UUID,
        name: str,
        extension: str,
        size: int,
        uri: str,
        proposal_id: UUID,
        type_id: str,
    ) -> ProposalFile:
        """Spy to all the attributes"""

        self.insert_proposal_file_params["id"] = id
        self.insert_proposal_file_params["name"] = name
        self.insert_proposal_file_params["extension"] = extension
        self.insert_proposal_file_params["size"] = size
        self.insert_proposal_file_params["uri"] = uri
        self.insert_proposal_file_params["proposal_id"] = proposal_id
        self.insert_proposal_file_params["type_id"] = type_id

        return mock_proposal_file()
