from typing import List
from src.data.interface import BenefitCategorizationTypeRepositoryInterface
from src.domain.models import BenefitCategorizationType
from src.domain.test import mock_categorization_type


class BenefitCategorizationTypeRepositorySpy(
    BenefitCategorizationTypeRepositoryInterface
):
    """Spy to BenefitCategorizationType Repository"""

    def __init__(self):
        self.insert_categorization_type_params = {}
        self.select_categorization_type_params = {}

    def insert_categorization_type(
        self, id: str, descricao: str, info: str
    ) -> BenefitCategorizationType:
        """Spy to all the attributes"""

        self.insert_categorization_type_params["id"] = id
        self.insert_categorization_type_params["descricao"] = descricao
        self.insert_categorization_type_params["info"] = info

        return mock_categorization_type()

    def select_categorization_type(
        self, id: str = None
    ) -> List[BenefitCategorizationType]:
        """Spy to all the attributes"""

        self.select_categorization_type_params["id"] = id

        return [mock_categorization_type()]

    def select_all_categorization_types(cls) -> List[BenefitCategorizationType]:
        """Spy to all the attributes"""

        return [mock_categorization_type()]
