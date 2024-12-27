from src.data.register_benefit_categorization_type import (
    RegisterBenefitCategorizationType,
)
from src.infra.repo import BenefitCategorizationTypeRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterBenefitCategorizationTypeController


def register_caracterization_type_composer() -> RouteInterface:
    """Composing Register BenefitCategorizationType Route
    :param  -   None
    :return -   Object with Register BenefitCategorizationType Route
    """

    repository = BenefitCategorizationTypeRepository()
    use_case = RegisterBenefitCategorizationType(repository)
    register_caracterization_type_route = RegisterBenefitCategorizationTypeController(
        use_case
    )

    return register_caracterization_type_route
