from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.data.interface import PropostaMetaRepositoryInterface
from src.domain.models import ProposalMeta
from src.domain.test import mock_proposal_meta
from src.domain.use_cases import RegisterProposalMetaInterface


class RegisterProposalMetaSpy(RegisterProposalMetaInterface):
    "Class te define use case: Register ProposalMeta"

    def __init__(self, proposal_meta_repository: Type[PropostaMetaRepositoryInterface]):
        self._proposal_meta_repository = proposal_meta_repository
        self.register_param = {}

    def register(
        self, order: int, goal: str, quantity: int, proposal_id: UUID
    ) -> Dict[bool, ProposalMeta]:
        """Register proposal meta use case
        :param  -   order: order of the proposal meta
                -   goal: description of the goal
                -   quantity: quantity of the goal
                -   proposal_id: UUID of the associated proposal
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(order, int)
            and isinstance(goal, str)
            and isinstance(quantity, int)
            and isinstance(proposal_id, uuid.UUID)
            and order > 0
            and len(goal) <= 500
            and quantity > 0
        )

        if validate_entry:
            self.register_param["order"] = order
            self.register_param["goal"] = goal
            self.register_param["quantity"] = quantity
            self.register_param["proposal_id"] = proposal_id

            response = mock_proposal_meta()

        return {"Success": validate_entry, "Data": response}
