from typing import Dict, Optional, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.legal_representative_repository_interface import (
    LegalRepresentativeRepositoryInterface,
)
from src.domain.use_cases.register_legal_representative_interface import (
    RegisterLegalRepresentativeInterface,
)
from src.domain.models import LegalRepresentative


class RegisterLegalRepresentative(RegisterLegalRepresentativeInterface):
    """Class to define legal representative case: Register Legal Representative"""

    def __init__(
        self,
        legal_representative_repository: Type[LegalRepresentativeRepositoryInterface],
    ):
        self._legal_representative_repository = legal_representative_repository

    def register(
        self,
        name: str,
        cpf: str,
        email: str,
        position: str,
        proposal_id: UUID,
        summary: Optional[str] = None,
    ) -> Dict[bool, LegalRepresentative]:
        """Register legal representative use case
        :param  -   name: representative name
                -   cpf: representative document number
                -   email: representative email
                -   position: representative position
                -   proposal_id: foreign key to proposal
                -   summary: representative summary
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(cpf, str)
            and isinstance(email, str)
            and isinstance(position, str)
            and isinstance(proposal_id, uuid.UUID)
            and len(name) <= 100
            and len(cpf) == 11
            and len(email) <= 100
            and len(position) <= 100
            and "@" in email
            and (summary is None or (isinstance(summary, str) and len(summary) <= 500))
        )

        if validate_entry:
            response = (
                self._legal_representative_repository.insert_legal_representative(
                    name=name,
                    cpf=cpf,
                    email=email,
                    position=position,
                    proposal_id=proposal_id,
                    summary=summary,
                )
            )

        return {"Success": validate_entry, "Data": response}
