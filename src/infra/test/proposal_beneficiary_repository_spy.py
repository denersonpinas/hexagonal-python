from sqlalchemy import UUID
from src.data.interface import ProposalBeneficiaryRepositoryInterface
from src.domain.models import ProposalBeneficiary
from src.domain.test import mock_proposal_beneficiary


class ProposalBeneficiaryRepositorySpy(ProposalBeneficiaryRepositoryInterface):
    """Spy to ProposalBeneficiary Repository"""

    def __init__(self):
        self.insert_proposal_beneficiary_params = {}

    def insert_proposal_beneficiary(
        self, id: UUID, quantidade: int, proposta_id: UUID
    ) -> ProposalBeneficiary:
        """Spy to all the attributes"""

        self.insert_proposal_beneficiary_params["id"] = id
        self.insert_proposal_beneficiary_params["quantidade"] = quantidade
        self.insert_proposal_beneficiary_params["proposta_id"] = proposta_id

        return mock_proposal_beneficiary()
