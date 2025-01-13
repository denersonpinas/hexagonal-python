from src.data.register_proposal_beneficiary_categorization import (
    RegisterProposalBeneficiaryCategorization,
)
from src.infra.repo import ProposalBeneficiaryCategorizationRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import (
    RegisterProposalBeneficinaryCategorizationController,
)


def register_proposal_beneficiary_categorization_composer() -> RouteInterface:
    """Composing Register ProposalBeneficiaryCategorization Route
    :param  -   None
    :return -   Object with Register ProposalBeneficiaryCategorization Route
    """

    repository = ProposalBeneficiaryCategorizationRepository()
    use_case = RegisterProposalBeneficiaryCategorization(repository)
    register_proposal_beneficiary_categorization_route = (
        RegisterProposalBeneficinaryCategorizationController(use_case)
    )

    return register_proposal_beneficiary_categorization_route
