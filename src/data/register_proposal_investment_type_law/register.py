from typing import Dict, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.proposal_investment_type_law_repository_interface import (
    ProposalInvestmentTypeLawRepositoryInterface,
)
from src.domain.use_cases.register_proposal_investment_type_law_interface import (
    RegisterProposalInvestmentTypeLawInterface,
)
from src.domain.models import ProposalInvestmentTypeLaw


class RegisterProposalInvestmentTypeLaw(RegisterProposalInvestmentTypeLawInterface):
    """Class to define proposal investment type law case: Register Proposal Investment Type Law"""

    def __init__(
        self,
        proposal_investment_type_law_repository: Type[
            ProposalInvestmentTypeLawRepositoryInterface
        ],
    ):
        self._proposal_investment_type_law_repository = (
            proposal_investment_type_law_repository
        )

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
            response = self._proposal_investment_type_law_repository.insert_proposal_investment_type_law(
                id=uuid.uuid4().hex,
                investment_type_law_id=investment_type_law_id,
                proposal_id=proposal_id,
            )

        return {"Success": validate_entry, "Data": response}
