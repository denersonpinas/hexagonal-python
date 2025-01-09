from typing import Optional
from src.data.interface import PartnershipHistoryRepositoryInterface
from src.domain.models import PartnershipHistory
from src.domain.test import mock_partnership_history


class PartnershipHistoryRepositorySpy(PartnershipHistoryRepositoryInterface):
    """Spy to PartnershipHistory Repository"""

    def __init__(self):
        self.insert_partnership_history_params = {}

    def insert_partnership_history(
        self,
        sponsors_number: int,
        renewal_number: int,
        proposal_id: str,
        additional_info: Optional[str] = None,
    ) -> PartnershipHistory:
        """Spy to all the attributes"""

        self.insert_partnership_history_params["sponsors_number"] = sponsors_number
        self.insert_partnership_history_params["renewal_number"] = renewal_number
        self.insert_partnership_history_params["proposal_id"] = proposal_id
        self.insert_partnership_history_params["additional_info"] = additional_info

        return mock_partnership_history()
