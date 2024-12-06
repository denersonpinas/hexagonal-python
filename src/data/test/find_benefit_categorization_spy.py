from typing import Dict, List, Type
from src.data.interface import BenefitCategorizationRepositoryInterface
from src.domain.models import BenefitCategorization
from src.domain.test import mock_categorization
from src.domain.use_cases import FindBenefitCategorizationInterface


class FindBenefitCategorizationSpy(FindBenefitCategorizationInterface):
    """Class to define use case: Select BenefitCategorization Spy"""

    def __init__(
        self,
        categorization_repository: Type[BenefitCategorizationRepositoryInterface],
    ):
        self.categorization_repository = categorization_repository
        self.by_id_param = {}
        self.by_type_param = {}

    def by_id(self, id: int) -> Dict[bool, List[BenefitCategorization]]:
        """Select BenefitCategorization by id spy"""

        self.by_id_param["id"] = id
        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = [mock_categorization()]

        return {"Success": validate_entry, "Data": response}

    def by_type(self, type_id: str) -> Dict[bool, List[BenefitCategorization]]:
        """Select BenefitCategorization by type_id"""

        self.by_type_param["type_id"] = type_id
        response = None
        validate_entry = isinstance(type_id, str)

        if validate_entry:
            response = [mock_categorization()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[BenefitCategorization]]:
        """Select all BenefitCategorization spy"""

        response = [mock_categorization()]

        return {"Success": True, "Data": response}
