from typing import Optional
from src.data.interface import LegalRepresentativeRepositoryInterface
from src.domain.models import LegalRepresentative
from src.domain.test import mock_legal_representative


class LegalRepresentativeRepositorySpy(LegalRepresentativeRepositoryInterface):
    """Spy to LegalRepresentative Repository"""

    def __init__(self):
        self.insert_legal_representative_params = {}

    def insert_legal_representative(
        self,
        name: str,
        cpf: str,
        email: str,
        position: str,
        proposal_id: str,
        summary: Optional[str] = None,
    ) -> LegalRepresentative:
        """Spy to all the attributes"""

        self.insert_legal_representative_params["name"] = name
        self.insert_legal_representative_params["cpf"] = cpf
        self.insert_legal_representative_params["email"] = email
        self.insert_legal_representative_params["position"] = position
        self.insert_legal_representative_params["proposal_id"] = proposal_id
        self.insert_legal_representative_params["summary"] = summary

        return mock_legal_representative()
