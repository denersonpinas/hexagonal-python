from src.data.register_proposal_beneficiary import RegisterProposalBeneficiary
from src.infra.repo import ProposalBeneficiaryRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalBeneficiaryController


def register_proposal_beneficiary_composer() -> RouteInterface:
    """Composing Register ProposalBeneficiary Route
    :param  -   None
    :return -   Object with Register ProposalBeneficiary Route
    """

    repository = ProposalBeneficiaryRepository()
    use_case = RegisterProposalBeneficiary(repository)
    register_proposal_beneficiary_route = RegisterProposalBeneficiaryController(
        use_case
    )

    return register_proposal_beneficiary_route
