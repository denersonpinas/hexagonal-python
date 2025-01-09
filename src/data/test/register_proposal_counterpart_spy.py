from typing import Dict, Optional, Type
from uuid import UUID
import uuid

from src.data.interface import ProposalCounterpartRepositoryInterface
from src.domain.models import ProposalCounterpart
from src.domain.test import mock_proposal_counterpart
from src.domain.use_cases import RegisterProposalCounterpartInterface


class RegisterProposalCounterpartSpy(RegisterProposalCounterpartInterface):
    "Class te define use case: Register ProposalCounterpart"

    def __init__(
        self,
        proposal_counterpart_repository: Type[ProposalCounterpartRepositoryInterface],
    ):
        self._proposal_counterpart_repository = proposal_counterpart_repository
        self.register_param = {}

    def register(
        self,
        description: str,
        quantity: int,
        investment_type_law_counterpart_id: int,
        proposal_investment_type_law_id: UUID,
        expected: Optional[int] = None,
    ) -> Dict[bool, ProposalCounterpart]:
        """Register proposal counterpart use case
        :param  -   id: unique identifier
                -   description: counterpart description
                -   quantity: counterpart quantity
                -   investment_type_law_counterpart_id: foreign key to investment type law counterpart
                -   proposal_investment_type_law_id: foreign key to proposal investment type law
                -   expected: expected quantity
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(description, str)
            and isinstance(quantity, int)
            and isinstance(investment_type_law_counterpart_id, int)
            and isinstance(proposal_investment_type_law_id, uuid.UUID)
            and len(description) <= 500
            and quantity > 0
            and investment_type_law_counterpart_id > 0
            and (expected is None or (isinstance(expected, int) and expected > 0))
        )

        if validate_entry:
            self.register_param["description"] = description
            self.register_param["quantity"] = quantity
            self.register_param["investment_type_law_counterpart_id"] = (
                investment_type_law_counterpart_id
            )
            self.register_param["proposal_investment_type_law_id"] = (
                proposal_investment_type_law_id
            )
            self.register_param["expected"] = expected

            response = mock_proposal_counterpart()

        return {"Success": validate_entry, "Data": response}
