from typing import Dict, Optional, Type

from src.data.interface import LegalRepresentativeRepositoryInterface
from src.domain.models import LegalRepresentative
from src.domain.test import mock_legal_representative
from src.domain.use_cases import RegisterLegalRepresentativeInterface


class RegisterLegalRepresentativeSpy(RegisterLegalRepresentativeInterface):
    "Class te define use case: Register LegalRepresentative"

    def __init__(
        self,
        legal_representative_repository: Type[LegalRepresentativeRepositoryInterface],
    ):
        self._legal_representative_repository = legal_representative_repository
        self.register_param = {}

    def register(
        self,
        name: str,
        cpf: str,
        email: str,
        position: str,
        proposal_id: str,
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
            and isinstance(proposal_id, str)
            and len(name) <= 100
            and len(cpf) == 11
            and len(email) <= 100
            and len(position) <= 100
            and "@" in email
            and (summary is None or (isinstance(summary, str) and len(summary) <= 500))
        )

        if validate_entry:
            self.register_param["name"] = name
            self.register_param["cpf"] = cpf
            self.register_param["email"] = email
            self.register_param["position"] = position
            self.register_param["proposal_id"] = proposal_id
            self.register_param["summary"] = summary

            response = mock_legal_representative()

        return {"Success": validate_entry, "Data": response}
