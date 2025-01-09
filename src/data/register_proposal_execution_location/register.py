from typing import Dict, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.proposal_execution_location_repository_interface import (
    ProposalExecutionLocationRepositoryInterface,
)
from src.domain.use_cases.register_proposal_execution_location_interface import (
    RegisterProposalExecutionLocationInterface,
)
from src.domain.models import ProposalExecutionLocation


class RegisterProposalExecutionLocation(RegisterProposalExecutionLocationInterface):
    """Class to define proposal execution location case: Register Proposal Execution Location"""

    def __init__(
        self,
        proposal_execution_location_repository: Type[
            ProposalExecutionLocationRepositoryInterface
        ],
    ):
        self._proposal_execution_location_repository = (
            proposal_execution_location_repository
        )

    def register(
        self, city_id: int, proposal_id: UUID
    ) -> Dict[bool, ProposalExecutionLocation]:
        """Register proposal execution location use case
        :param  -   city_id: foreign key to city
                -   proposal_id: foreign key to proposal
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(city_id, int)
            and isinstance(proposal_id, uuid.UUID)
            and city_id > 0
        )

        if validate_entry:
            response = self._proposal_execution_location_repository.insert_proposal_execution_location(
                city_id=city_id, proposal_id=proposal_id
            )

        return {"Success": validate_entry, "Data": response}
