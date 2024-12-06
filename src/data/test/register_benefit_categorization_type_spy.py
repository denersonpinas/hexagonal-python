from typing import Dict, Type

from src.data.interface import BenefitCategorizationTypeRepositoryInterface
from src.domain.models import BenefitCategorizationType
from src.domain.test import mock_categorization_type
from src.domain.use_cases import RegisterBenefitCategorizationTypeInterface


class RegisterBenefitCategorizationTypeSpy(RegisterBenefitCategorizationTypeInterface):
    "Class te define use case: Register BenefitCategorizationType"

    def __init__(
        self,
        categorization_type_repo: Type[BenefitCategorizationTypeRepositoryInterface],
    ):
        self._categorization_type_repo = categorization_type_repo
        self.register_param = {}

    def register(
        self, description: str, info: str
    ) -> Dict[bool, BenefitCategorizationType]:
        """Register BenefitCategorizationType use case"""

        response = None
        validate_entry = (
            isinstance(description, str)
            and isinstance(info, str)
            and len(description) <= 50
            and len(info) <= 150
        )

        if validate_entry:
            self.register_param["description"] = description
            self.register_param["info"] = info

            response = mock_categorization_type()

        return {"Success": validate_entry, "Data": response}
