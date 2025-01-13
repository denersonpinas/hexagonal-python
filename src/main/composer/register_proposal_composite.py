from src.data.register_proposal import RegisterProposal
from src.infra.repo import ProposalRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalController


def register_proposal_composer() -> RouteInterface:
    """Composing Register Proposal Route
    :param  -   None
    :return -   Object with Register Proposal Route
    """

    repository = ProposalRepository()
    use_case = RegisterProposal(repository)
    register_proposal_route = RegisterProposalController(use_case)

    return register_proposal_route
