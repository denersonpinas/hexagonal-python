from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.data.interface import ProposalExecutionLocationRepositoryInterface
from src.domain.models import ProposalExecutionLocation
from src.domain.test import mock_proposal_execution_location
from src.domain.use_cases import RegisterProposalExecutionLocationInterface


class RegisterProposalExecutionLocationSpy(RegisterProposalExecutionLocationInterface):
    "Class te define use case: Register ProposalExecutionLocation"

    def __init__(
        self,
        proposal_execution_location_repository: Type[
            ProposalExecutionLocationRepositoryInterface
        ],
    ):
        self._proposal_execution_location_repository = (
            proposal_execution_location_repository
        )
        self.register_param = {}

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
            self.register_param["city_id"] = city_id
            self.register_param["proposal_id"] = proposal_id

            response = mock_proposal_execution_location()

        return {"Success": validate_entry, "Data": response}
