from sqlalchemy import UUID
from src.data.interface import ProposalBeneficiaryCategorizationRepositoryInterface
from src.domain.models import ProposalBeneficiaryCategorization
from src.domain.test import mock_proposal_beneficiary_categorization


class ProposalBeneficiaryCategorizationRepositorySpy(
    ProposalBeneficiaryCategorizationRepositoryInterface
):
    """Spy to ProposalBeneficiaryCategorization Repository"""

    def __init__(self):
        self.insert_proposal_beneficiary_categorization_params = {}

    def insert_proposal_beneficiary_categorization(
        self, categorizacao_id: int, proposta_beneficiario_id: UUID
    ) -> ProposalBeneficiaryCategorization:
        """Spy to all the attributes"""

        self.insert_proposal_beneficiary_categorization_params["categorizacao_id"] = (
            categorizacao_id
        )
        self.insert_proposal_beneficiary_categorization_params[
            "proposta_beneficiario_id"
        ] = proposta_beneficiario_id

        return mock_proposal_beneficiary_categorization()
