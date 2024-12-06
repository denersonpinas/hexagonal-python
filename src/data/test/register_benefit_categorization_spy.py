from typing import Dict, Type

from src.data.interface import BenefitCategorizationRepositoryInterface
from src.domain.models import BenefitCategorization
from src.domain.test import mock_categorization
from src.domain.use_cases import RegisterBenefitCategorizationInterface


class RegisterBenefitCategorizationSpy(RegisterBenefitCategorizationInterface):
    "Class te define use case: Register BenefitCategorization"

    def __init__(
        self, categorization_repo: Type[BenefitCategorizationRepositoryInterface]
    ):
        self._categorization_repo = categorization_repo
        self.register_param = {}

    def register(self, value: str, type_id: str) -> Dict[bool, BenefitCategorization]:
        """Register BenefitCategorization use case"""

        response = None
        validate_entry = (
            isinstance(value, str)
            and isinstance(type_id, str)
            and len(value) <= 64
            and len(type_id) <= 32
        )

        if validate_entry:
            self.register_param["value"] = value
            self.register_param["type_id"] = type_id

            response = mock_categorization()

        return {"Success": validate_entry, "Data": response}
