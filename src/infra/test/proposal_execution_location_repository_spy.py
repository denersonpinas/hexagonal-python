from sqlalchemy import UUID
from src.data.interface import ProposalExecutionLocationRepositoryInterface
from src.domain.models import ProposalExecutionLocation
from src.domain.test import mock_proposal_execution_location


class ProposalExecutionLocationRepositorySpy(
    ProposalExecutionLocationRepositoryInterface
):
    """Spy to ProposalExecutionLocation Repository"""

    def __init__(self):
        self.insert_proposal_execution_location_params = {}

    def insert_proposal_execution_location(
        self, city_id: int, proposal_id: UUID
    ) -> ProposalExecutionLocation:
        """Spy to all the attributes"""

        self.insert_proposal_execution_location_params["city_id"] = city_id
        self.insert_proposal_execution_location_params["proposal_id"] = proposal_id

        return mock_proposal_execution_location()
