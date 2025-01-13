from src.data.register_proposal_sponsor import RegisterProposalSponsor
from src.infra.repo import ProposalSponsorRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalSponsorController


def register_proposal_sponsor_composer() -> RouteInterface:
    """Composing Register ProposalSponsor Route
    :param  -   None
    :return -   Object with Register ProposalSponsor Route
    """

    repository = ProposalSponsorRepository()
    use_case = RegisterProposalSponsor(repository)
    register_proposal_sponsor_route = RegisterProposalSponsorController(use_case)

    return register_proposal_sponsor_route
