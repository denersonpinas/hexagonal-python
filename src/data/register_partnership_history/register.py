from typing import Dict, Optional, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.partnership_history_repository_interface import (
    PartnershipHistoryRepositoryInterface,
)
from src.domain.use_cases.register_partnership_history_interface import (
    RegisterPartnershipHistoryInterface,
)
from src.domain.models import PartnershipHistory


class RegisterPartnershipHistory(RegisterPartnershipHistoryInterface):
    """Class to define partnership history case: Register Partnership History"""

    def __init__(
        self,
        partnership_history_repository: Type[PartnershipHistoryRepositoryInterface],
    ):
        self._partnership_history_repository = partnership_history_repository

    def register(
        self,
        sponsors_number: int,
        renewal_number: int,
        proposal_id: UUID,
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
            and isinstance(proposal_id, uuid.UUID)
            and sponsors_number >= 0
            and renewal_number >= 0
            and (
                additional_info is None
                or (isinstance(additional_info, str) and len(additional_info) <= 500)
            )
        )

        if validate_entry:
            response = self._partnership_history_repository.insert_partnership_history(
                sponsors_number=sponsors_number,
                renewal_number=renewal_number,
                proposal_id=proposal_id,
                additional_info=additional_info,
            )

        return {"Success": validate_entry, "Data": response}
