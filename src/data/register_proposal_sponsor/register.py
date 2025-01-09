from typing import Dict, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.proposal_sponsor_repository_interface import (
    ProposalSponsorRepositoryInterface,
)
from src.domain.use_cases.register_proposal_sponsor_interface import (
    RegisterProposalSponsorInterface,
)
from src.domain.models import ProposalSponsor


class RegisterProposalSponsor(RegisterProposalSponsorInterface):
    """Class to define proposal sponsor case: Register Proposal Sponsor"""

    def __init__(
        self, proposal_sponsor_repository: Type[ProposalSponsorRepositoryInterface]
    ):
        self._proposal_sponsor_repository = proposal_sponsor_repository

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
            response = self._proposal_sponsor_repository.insert_proposal_sponsor(
                nome=nome, formato=formato, valor=valor, proposta_id=proposta_id
            )

        return {"Success": validate_entry, "Data": response}
