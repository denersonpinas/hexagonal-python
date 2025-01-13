from src.data.register_proposal_investment_type_law import (
    RegisterProposalInvestmentTypeLaw,
)
from src.infra.repo import ProposalInvestmentTypeLawRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterProposalInvestmentTypeLawController


def register_proposal_investment_type_law_composer() -> RouteInterface:
    """Composing Register ProposalInvestmentTypeLaw Route
    :param  -   None
    :return -   Object with Register ProposalInvestmentTypeLaw Route
    """

    repository = ProposalInvestmentTypeLawRepository()
    use_case = RegisterProposalInvestmentTypeLaw(repository)
    register_investment_type_law_route = RegisterProposalInvestmentTypeLawController(
        use_case
    )

    return register_investment_type_law_route
