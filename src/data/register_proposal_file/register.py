from typing import Dict, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.proposal_file_repository_interface import (
    ProposalFileRepositoryInterface,
)
from src.domain.use_cases.register_proposal_file_interface import (
    RegisterProposalFileInterface,
)
from src.domain.models import ProposalFile


class RegisterProposalFile(RegisterProposalFileInterface):
    """Class to define proposal file case: Register Proposal File"""

    def __init__(self, proposal_file_repository: Type[ProposalFileRepositoryInterface]):
        self._proposal_file_repository = proposal_file_repository

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
            response = self._proposal_file_repository.insert_proposal_file(
                id=uuid.uuid4().hex,
                name=name,
                extension=extension,
                size=size,
                uri=uri,
                proposal_id=proposal_id,
                type_id=type_id,
            )

        return {"Success": validate_entry, "Data": response}
