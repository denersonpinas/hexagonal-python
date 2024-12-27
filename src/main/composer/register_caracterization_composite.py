from src.data.register_benefit_categorization import RegisterBenefitCategorization
from src.infra.repo import BenefitCategorizationRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterBenefitCategorizationController


def register_caracterization_composer() -> RouteInterface:
    """Composing Register BenefitCategorization Route
    :param  -   None
    :return -   Object with Register BenefitCategorization Route
    """

    repository = BenefitCategorizationRepository()
    use_case = RegisterBenefitCategorization(repository)
    register_caracterization_route = RegisterBenefitCategorizationController(use_case)

    return register_caracterization_route
