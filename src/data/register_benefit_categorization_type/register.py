# Implementation
from typing import Dict, Type
from src.data.interface import BenefitCategorizationTypeRepositoryInterface
from src.domain.models import BenefitCategorizationType
from src.domain.use_cases import RegisterBenefitCategorizationTypeInterface


class RegisterBenefitCategorizationType(RegisterBenefitCategorizationTypeInterface):
    """Class to define use case: Register Benefit Categorization Type"""

    def __init__(
        self,
        categorization_type_repo: Type[BenefitCategorizationTypeRepositoryInterface],
    ):
        self._categorization_type_repo = categorization_type_repo

    def register(
        self, description: str, info: str
    ) -> Dict[bool, BenefitCategorizationType]:
        """Register Benefit Categorization Type use case
        :param  -   description: Description of the categorization type
                    info: Additional information
        :return -   Dictionary with information of the process
        """
        response = None
        validate_entry = (
            isinstance(description, str)
            and isinstance(info, str)
            and len(description) <= 50
            and len(info) <= 150
        )

        if validate_entry:
            response = self._categorization_type_repo.insert_categorization_type(
                descricao=description, info=info
            )

        return {"Success": validate_entry, "Data": response}
