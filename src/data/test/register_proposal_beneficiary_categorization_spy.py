from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.data.interface import ProposalBeneficiaryCategorizationRepositoryInterface
from src.domain.models import ProposalBeneficiaryCategorization
from src.domain.test import mock_proposal_beneficiary_categorization
from src.domain.use_cases import RegisterProposalBeneficiaryCategorizationInterface


class RegisterProposalBeneficiaryCategorizationSpy(
    RegisterProposalBeneficiaryCategorizationInterface
):
    "Class te define use case: Register ProposalBeneficiaryCategorization"

    def __init__(
        self,
        proposal_beneficiary_categorization_repository: Type[
            ProposalBeneficiaryCategorizationRepositoryInterface
        ],
    ):
        self._proposal_beneficiary_categorization_repository = (
            proposal_beneficiary_categorization_repository
        )
        self.register_param = {}

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
            self.register_param["categorizacao_id"] = categorizacao_id
            self.register_param["proposta_beneficiario_id"] = proposta_beneficiario_id

            response = mock_proposal_beneficiary_categorization()

        return {"Success": validate_entry, "Data": response}
