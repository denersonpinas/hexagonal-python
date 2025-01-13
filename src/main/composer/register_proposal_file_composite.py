from src.data.register_proposal_file import RegisterProposalFile
from src.infra.repo import ProposalFileRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalFileController


def register_proposal_file_composer() -> RouteInterface:
    """Composing Register ProposalFile Route
    :param  -   None
    :return -   Object with Register ProposalFile Route
    """

    repository = ProposalFileRepository()
    use_case = RegisterProposalFile(repository)
    register_proposal_file_route = RegisterProposalFileController(use_case)

    return register_proposal_file_route
