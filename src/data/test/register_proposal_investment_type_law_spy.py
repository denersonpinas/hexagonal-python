from typing import Dict, Type
from uuid import UUID
import uuid

from src.data.interface import ProposalInvestmentTypeLawRepositoryInterface
from src.domain.models import ProposalInvestmentTypeLaw
from src.domain.test import mock_proposal_investment_type_law
from src.domain.use_cases import RegisterProposalInvestmentTypeLawInterface


class RegisterProposalInvestmentTypeLawSpy(RegisterProposalInvestmentTypeLawInterface):
    "Class te define use case: Register ProposalInvestmentTypeLaw"

    def __init__(
        self,
        proposal_investment_type_law_repository: Type[
            ProposalInvestmentTypeLawRepositoryInterface
        ],
    ):
        self._proposal_investment_type_law_repository = (
            proposal_investment_type_law_repository
        )
        self.register_param = {}

    def register(
        self, investment_type_law_id: int, proposal_id: UUID
    ) -> Dict[bool, ProposalInvestmentTypeLaw]:
        """Register proposal investment type law use case
        :param  -   id: unique identifier
                -   investment_type_law_id: foreign key to investment type law
                -   proposal_id: foreign key to proposal
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(investment_type_law_id, int)
            and isinstance(proposal_id, uuid.UUID)
            and investment_type_law_id > 0
        )

        if validate_entry:
            self.register_param["investment_type_law_id"] = investment_type_law_id
            self.register_param["proposal_id"] = proposal_id

            response = mock_proposal_investment_type_law()

        return {"Success": validate_entry, "Data": response}
