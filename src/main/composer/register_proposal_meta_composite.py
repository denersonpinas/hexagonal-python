from src.data.register_proposal_meta import RegisterProposalMeta
from src.infra.repo import ProposalMetaRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalMetaController


def register_proposal_meta_composer() -> RouteInterface:
    """Composing Register ProposalMeta Route
    :param  -   None
    :return -   Object with Register ProposalMeta Route
    """

    repository = ProposalMetaRepository()
    use_case = RegisterProposalMeta(repository)
    register_proposal_meta_route = RegisterProposalMetaController(use_case)

    return register_proposal_meta_route
