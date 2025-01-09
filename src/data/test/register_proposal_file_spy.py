from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.data.interface import ProposalFileRepositoryInterface
from src.domain.models import ProposalFile
from src.domain.test import mock_proposal_file
from src.domain.use_cases import RegisterProposalFileInterface


class RegisterProposalFileSpy(RegisterProposalFileInterface):
    "Class te define use case: Register ProposalFile"

    def __init__(self, proposal_file_repository: Type[ProposalFileRepositoryInterface]):
        self._proposal_file_repository = proposal_file_repository
        self.register_param = {}

    def register(
        self,
        name: str,
        extension: str,
        size: int,
        uri: str,
        proposal_id: UUID,
        type_id: str,
    ) -> Dict[bool, ProposalFile]:
        """Register proposal file use case
        :param  -   id: file unique identifier
                -   name: file name
                -   extension: file extension
                -   size: file size in bytes
                -   uri: file location uri
                -   proposal_id: foreign key to proposal
                -   type_id: foreign key to file type
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(extension, str)
            and isinstance(size, int)
            and isinstance(uri, str)
            and isinstance(proposal_id, uuid.UUID)
            and isinstance(type_id, str)
            and len(name) <= 100
            and len(extension) <= 10
            and size > 0
            and len(uri) <= 500
        )

        if validate_entry:
            self.register_param["name"] = name
            self.register_param["extension"] = extension
            self.register_param["size"] = size
            self.register_param["uri"] = uri
            self.register_param["proposal_id"] = proposal_id
            self.register_param["type_id"] = type_id

            response = mock_proposal_file()

        return {"Success": validate_entry, "Data": response}
