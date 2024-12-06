from typing import Dict, List, Type
from src.data.interface import BenefitCategorizationTypeRepositoryInterface
from src.domain.models import BenefitCategorizationType
from src.domain.test import mock_categorization_type
from src.domain.use_cases import FindBenefitCategorizationTypeInterface


class FindBenefitCategorizationTypeSpy(FindBenefitCategorizationTypeInterface):
    """Class to define use case: Select BenefitCategorizationType Spy"""

    def __init__(
        self,
        categorization_type_repository: Type[
            BenefitCategorizationTypeRepositoryInterface
        ],
    ):
        self.categorization_type_repository = categorization_type_repository
        self.by_id_param = {}

    def by_id(self, id: str) -> Dict[bool, List[BenefitCategorizationType]]:
        """Select BenefitCategorizationType by id spy"""

        self.by_id_param["id"] = id
        response = None
        validate_entry = isinstance(id, str)

        if validate_entry:
            response = [mock_categorization_type()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[BenefitCategorizationType]]:
        """Select all BenefitCategorizationType spy"""

        response = [mock_categorization_type()]

        return {"Success": True, "Data": response}
