from typing import Dict, Optional, Type
import uuid
from sqlalchemy import UUID
from src.data.interface.proposal_counterpart_repository_interface import (
    ProposalCounterpartRepositoryInterface,
)
from src.domain.use_cases.register_proposal_counterpart_interface import (
    RegisterProposalCounterpartInterface,
)
from src.domain.models import ProposalCounterpart


class RegisterProposalCounterpart(RegisterProposalCounterpartInterface):
    """Class to define proposal counterpart case: Register Proposal Counterpart"""

    def __init__(
        self,
        proposal_counterpart_repository: Type[ProposalCounterpartRepositoryInterface],
    ):
        self._proposal_counterpart_repository = proposal_counterpart_repository

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
            response = self._proposal_counterpart_repository.insert_proposal_counterpart(
                id=uuid.uuid4().hex,
                description=description,
                quantity=quantity,
                investment_type_law_counterpart_id=investment_type_law_counterpart_id,
                proposal_investment_type_law_id=proposal_investment_type_law_id,
                expected=expected,
            )

        return {"Success": validate_entry, "Data": response}
