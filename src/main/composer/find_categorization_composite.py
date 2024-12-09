from src.data.find_benefit_categorization import FindBenefitCategorization
from src.infra.repo import BenefitCategorizationRepository
from src.presenters.controllers import FindBenefitCategorizationController


def find_categorization_composer() -> FindBenefitCategorizationController:
    """Composing Find BenefitCategorizationType Route
    :param  - None
    :return - Object with Find BenefitCategorizationType Route
    """

    repository = BenefitCategorizationRepository()
    use_case = FindBenefitCategorization(repository)
    find_categorization_route = FindBenefitCategorizationController(use_case)

    return find_categorization_route
