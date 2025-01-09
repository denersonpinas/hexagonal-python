from typing import Dict, Type
import uuid
from sqlalchemy import UUID
from src.data.interface.proposal_meta_repository_interface import (
    PropostaMetaRepositoryInterface,
)
from src.domain.use_cases.register_proposal_meta_interface import (
    RegisterProposalMetaInterface,
)
from src.domain.models import ProposalMeta


class RegisterProposalMeta(RegisterProposalMetaInterface):
    """Class to define proposal meta case: Register Proposal Meta"""

    def __init__(self, proposal_meta_repository: Type[PropostaMetaRepositoryInterface]):
        self._proposal_meta_repository = proposal_meta_repository

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
            response = self._proposal_meta_repository.insert_proposal_meta(
                order=order, goal=goal, quantity=quantity, proposal_id=proposal_id
            )

        return {"Success": validate_entry, "Data": response}
