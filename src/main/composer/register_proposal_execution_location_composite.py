from src.data.register_proposal_execution_location import (
    RegisterProposalExecutionLocation,
)
from src.infra.repo import ProposalExecutionLocationRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalExecutionLocationController


def register_proposal_execution_location_composer() -> RouteInterface:
    """Composing Register ProposalExecutionLocation Route
    :param  -   None
    :return -   Object with Register ProposalExecutionLocation Route
    """

    repository = ProposalExecutionLocationRepository()
    use_case = RegisterProposalExecutionLocation(repository)
    register_proposal_execution_location_route = (
        RegisterProposalExecutionLocationController(use_case)
    )

    return register_proposal_execution_location_route
