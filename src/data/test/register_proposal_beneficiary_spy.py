from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.data.interface import ProposalBeneficiaryRepositoryInterface
from src.domain.models import ProposalBeneficiary
from src.domain.test import mock_proposal_beneficiary
from src.domain.use_cases import RegisterProposalBeneficiaryInterface


class RegisterProposalBeneficiarySpy(RegisterProposalBeneficiaryInterface):
    "Class te define use case: Register ProposalBeneficiary"

    def __init__(
        self,
        proposal_beneficiary_repository: Type[ProposalBeneficiaryRepositoryInterface],
    ):
        self._proposal_beneficiary_repository = proposal_beneficiary_repository
        self.register_param = {}

    def register(
        self, quantidade: int, proposta_id: UUID
    ) -> Dict[bool, ProposalBeneficiary]:
        """Register proposal beneficiary use case
        :param  -   id: beneficiary id
                -   quantidade: beneficiary quantity
                -   proposta_id: proposal ID
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(quantidade, int)
            and isinstance(proposta_id, uuid.UUID)
            and quantidade > 0
        )

        if validate_entry:
            self.register_param["quantidade"] = quantidade
            self.register_param["proposta_id"] = proposta_id

            response = mock_proposal_beneficiary()

        return {"Success": validate_entry, "Data": response}
