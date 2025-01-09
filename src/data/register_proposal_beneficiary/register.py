from typing import Dict, Type
import uuid
from sqlalchemy import UUID

from src.domain.use_cases.register_proposal_beneficiary_interface import (
    RegisterProposalBeneficiaryInterface,
)
from src.infra.repo.proposal_beneficiary_repository import ProposalBeneficiaryRepository
from src.domain.models import ProposalBeneficiary


class RegisterProposalBeneficiary(RegisterProposalBeneficiaryInterface):
    """Class to define proposal beneficiary case: Register Proposal Beneficiary"""

    def __init__(
        self, proposal_beneficiary_repository: Type[ProposalBeneficiaryRepository]
    ):
        self._proposal_beneficiary_repository = proposal_beneficiary_repository

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
            response = (
                self._proposal_beneficiary_repository.insert_proposal_beneficiary(
                    id=uuid.uuid4().hex, quantidade=quantidade, proposta_id=proposta_id
                )
            )

        return {"Success": validate_entry, "Data": response}
