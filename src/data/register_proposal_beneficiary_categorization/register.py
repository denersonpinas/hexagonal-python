from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.domain.models import ProposalBeneficiaryCategorization
from src.data.interface.proposal_beneficiary_categorization_repository_interface import (
    ProposalBeneficiaryCategorizationRepositoryInterface,
)
from src.domain.use_cases.register_proposal_beneficiary_categorization_interface import (
    RegisterProposalBeneficiaryCategorizationInterface,
)


class RegisterProposalBeneficiaryCategorization(
    RegisterProposalBeneficiaryCategorizationInterface
):
    """Class to define proposal beneficiary categorization case: Register Proposal Beneficiary Categorization"""

    def __init__(
        self,
        proposal_beneficiary_categorization_repository: Type[
            ProposalBeneficiaryCategorizationRepositoryInterface
        ],
    ):
        self._proposal_beneficiary_categorization_repository = (
            proposal_beneficiary_categorization_repository
        )

    def register(
        self, categorizacao_id: int, proposta_beneficiario_id: UUID
    ) -> Dict[bool, ProposalBeneficiaryCategorization]:
        """Register proposal beneficiary categorization use case
        :param  -   categorizacao_id: categorization ID
                -   proposta_beneficiario_id: proposal beneficiary ID
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(categorizacao_id, int)
            and isinstance(proposta_beneficiario_id, uuid.UUID)
            and categorizacao_id > 0
        )

        if validate_entry:
            response = self._proposal_beneficiary_categorization_repository.insert_proposal_beneficiary_categorization(
                categorizacao_id=categorizacao_id,
                proposta_beneficiario_id=proposta_beneficiario_id,
            )

        return {"Success": validate_entry, "Data": response}
