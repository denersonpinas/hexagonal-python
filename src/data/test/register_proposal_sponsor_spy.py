from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.data.interface import ProposalSponsorRepositoryInterface
from src.domain.models import ProposalSponsor
from src.domain.test import mock_proposal_sponsor
from src.domain.use_cases import RegisterProposalSponsorInterface


class RegisterProposalSponsorSpy(RegisterProposalSponsorInterface):
    "Class te define use case: Register ProposalSponsor"

    def __init__(
        self, proposal_sponsor_repository: Type[ProposalSponsorRepositoryInterface]
    ):
        self._proposal_sponsor_repository = proposal_sponsor_repository
        self.register_param = {}

    def register(
        self, nome: str, formato: str, valor: float, proposta_id: UUID
    ) -> Dict[bool, ProposalSponsor]:
        """Register proposal sponsor use case
        :param  -   nome: sponsor name
                -   formato: sponsor format
                -   valor: sponsor value
                -   proposta_id: proposal ID
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(nome, str)
            and isinstance(formato, str)
            and isinstance(valor, float)
            and isinstance(proposta_id, uuid.UUID)
            and len(nome) <= 100
            and len(formato) <= 50
            and valor > 0
        )

        if validate_entry:
            self.register_param["nome"] = nome
            self.register_param["formato"] = formato
            self.register_param["valor"] = valor
            self.register_param["proposta_id"] = proposta_id

            response = mock_proposal_sponsor()

        return {"Success": validate_entry, "Data": response}
