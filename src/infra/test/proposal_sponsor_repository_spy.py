from sqlalchemy import UUID
from src.data.interface import ProposalSponsorRepositoryInterface
from src.domain.models import ProposalSponsor
from src.domain.test import mock_proposal_sponsor


class ProposalSponsorRepositorySpy(ProposalSponsorRepositoryInterface):
    """Spy to ProposalSponsor Repository"""

    def __init__(self):
        self.insert_proposal_sponsor_params = {}

    def insert_proposal_sponsor(
        self, nome: str, formato: str, valor: float, proposta_id: UUID
    ) -> ProposalSponsor:
        """Spy to all the attributes"""

        self.insert_proposal_sponsor_params["nome"] = nome
        self.insert_proposal_sponsor_params["formato"] = formato
        self.insert_proposal_sponsor_params["valor"] = valor
        self.insert_proposal_sponsor_params["proposta_id"] = proposta_id

        return mock_proposal_sponsor()
