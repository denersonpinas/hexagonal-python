from typing import List
from src.data.interface import BenefitCategorizationRepositoryInterface
from src.domain.models import BenefitCategorization
from src.domain.test import mock_categorization


class BenefitCategorizationRepositorySpy(BenefitCategorizationRepositoryInterface):
    """Spy to BenefitCategorization Repository"""

    def __init__(self):
        self.insert_categorization_params = {}
        self.select_categorization_params = {}

    def insert_categorization(self, valor: str, tipo_id: str) -> BenefitCategorization:
        """Spy to all the attributes"""

        self.insert_categorization_params["valor"] = valor
        self.insert_categorization_params["tipo_id"] = tipo_id

        return mock_categorization()

    def select_categorization(
        self, id: int = None, tipo_id: str = None
    ) -> List[BenefitCategorization]:
        """Spy to all the attributes"""

        self.select_categorization_params["id"] = id
        self.select_categorization_params["tipo_id"] = tipo_id

        return [mock_categorization()]

    def select_all_categorizations(cls) -> List[BenefitCategorization]:
        """Spy to all the attributes"""

        return [mock_categorization()]
