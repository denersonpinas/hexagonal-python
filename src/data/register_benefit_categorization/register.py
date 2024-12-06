# Implementation
from typing import Dict, Type
from src.data.interface import BenefitCategorizationRepositoryInterface
from src.domain.models import BenefitCategorization
from src.domain.use_cases import RegisterBenefitCategorizationInterface


class RegisterBenefitCategorization(RegisterBenefitCategorizationInterface):
    """Class to define use case: Register Benefit Categorization"""

    def __init__(
        self,
        categorization_repo: Type[BenefitCategorizationRepositoryInterface],
    ):
        self.categorization_repo = categorization_repo

    def register(self, value: str, type_id: str) -> Dict[bool, BenefitCategorization]:
        """Register Benefit Categorization Type use case
        :param  -   valor: Value of the categorization
                -   tipo_id: ID of the categorization type
        :return -   Dictionary with information of the process
        """
        response = None
        validate_entry = (
            isinstance(value, str)
            and isinstance(type_id, str)
            and len(value) <= 64
            and len(type_id) <= 32
        )

        if validate_entry:
            response = self.categorization_repo.insert_categorization(
                valor=value, tipo_id=type_id
            )

        return {"Success": validate_entry, "Data": response}
