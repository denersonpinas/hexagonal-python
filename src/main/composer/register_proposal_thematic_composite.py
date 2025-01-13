from src.data.register_proposal_thematic import RegisterProposalThematic
from src.infra.repo import ProposalThematicRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalThematicController


def register_proposal_thematic_composer() -> RouteInterface:
    """Composing Register ProposalThematic Route
    :param  -   None
    :return -   Object with Register ProposalThematic Route
    """

    repository = ProposalThematicRepository()
    use_case = RegisterProposalThematic(repository)
    register_proposal_thematic_route = RegisterProposalThematicController(use_case)

    return register_proposal_thematic_route
