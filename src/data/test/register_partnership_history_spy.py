from typing import Dict, Optional, Type

from src.data.interface import PartnershipHistoryRepositoryInterface
from src.domain.models import PartnershipHistory
from src.domain.test import mock_partnership_history
from src.domain.use_cases import RegisterPartnershipHistoryInterface


class RegisterPartnershipHistorySpy(RegisterPartnershipHistoryInterface):
    "Class te define use case: Register PartnershipHistory"

    def __init__(
        self,
        partnership_history_repository: Type[PartnershipHistoryRepositoryInterface],
    ):
        self._partnership_history_repository = partnership_history_repository
        self.register_param = {}

    def register(
        self,
        sponsors_number: int,
        renewal_number: int,
        proposal_id: str,
        additional_info: Optional[str] = None,
    ) -> Dict[bool, PartnershipHistory]:
        """Register partnership history use case
        :param  -   sponsors_number: number of sponsors
                -   renewal_number: number of renewals
                -   proposal_id: foreign key to proposal
                -   additional_info: additional information
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(sponsors_number, int)
            and isinstance(renewal_number, int)
            and isinstance(proposal_id, str)
            and sponsors_number >= 0
            and renewal_number >= 0
            and (
                additional_info is None
                or (isinstance(additional_info, str) and len(additional_info) <= 500)
            )
        )

        if validate_entry:
            self.register_param["sponsors_number"] = sponsors_number
            self.register_param["renewal_number"] = renewal_number
            self.register_param["proposal_id"] = proposal_id
            self.register_param["additional_info"] = additional_info

            response = mock_partnership_history()

        return {"Success": validate_entry, "Data": response}
