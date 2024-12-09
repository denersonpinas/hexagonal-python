from src.data.find_benefit_categorization_type import FindBenefitCategorizationType
from src.infra.repo import BenefitCategorizationTypeRepository
from src.presenters.controllers import FindBenefitCategorizationTypeController


def find_categorization_type_composer() -> FindBenefitCategorizationTypeController:
    """Composing Find BenefitCategorizationType Route
    :param  - None
    :return - Object with Find BenefitCategorizationType Route
    """

    repository = BenefitCategorizationTypeRepository()
    use_case = FindBenefitCategorizationType(repository)
    find_categorization_type_route = FindBenefitCategorizationTypeController(use_case)

    return find_categorization_type_route
