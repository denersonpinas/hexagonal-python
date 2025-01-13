from src.data.register_proposal_milestone import RegisterProposalMilestone
from src.infra.repo import ProposalMilestoneRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalMilestoneController


def register_proposal_milestone_composer() -> RouteInterface:
    """Composing Register ProposalMilestone Route
    :param  -   None
    :return -   Object with Register ProposalMilestone Route
    """

    repository = ProposalMilestoneRepository()
    use_case = RegisterProposalMilestone(repository)
    register_proposal_milestone_route = RegisterProposalMilestoneController(use_case)

    return register_proposal_milestone_route
