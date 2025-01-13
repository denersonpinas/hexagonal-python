from src.data.register_proposal_counterpart import RegisterProposalCounterpart
from src.infra.repo import ProposalCounterpartRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalCounterpartController


def register_proposal_counterpart_composer() -> RouteInterface:
    """Composing Register ProposalCounterpart Route
    :param  -   None
    :return -   Object with Register ProposalCounterpart Route
    """

    repository = ProposalCounterpartRepository()
    use_case = RegisterProposalCounterpart(repository)
    register_proposal_counterpart_route = RegisterProposalCounterpartController(
        use_case
    )

    return register_proposal_counterpart_route
