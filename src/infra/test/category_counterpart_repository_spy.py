from typing import List
from src.data.interface import CategoryCounterpartRepositoryInterface
from src.domain.models import Counterpart
from src.domain.test import mock_category_counterpart


class CategoryCounterpartRepositorySpy(CategoryCounterpartRepositoryInterface):
    """Spy to Category Counterpart Repository"""

    def __init__(self):
        self.insert_category_counterpart_params = {}
        self.select_category_counterpart_params = {}

    def insert_category_counterpart(
        self, nome, descricao, subcategoria_de_id
    ) -> Counterpart:
        """Spy to all the attributes"""

        self.insert_category_counterpart_params["nome"] = nome
        self.insert_category_counterpart_params["descricao"] = descricao
        self.insert_category_counterpart_params["subcategoria_de_id"] = (
            subcategoria_de_id
        )

        return mock_category_counterpart()

    def select_category_counterpart(
        self, category_counterpart_id=None, subcategoria_de_id=None
    ) -> List[Counterpart]:
        """Spy to all the attributes"""

        self.select_category_counterpart_params["category_counterpart_id"] = (
            category_counterpart_id
        )
        self.select_category_counterpart_params["subcategoria_de_id"] = (
            subcategoria_de_id
        )

        return [mock_category_counterpart()]

    def select_all_category_counterpart(self) -> List[Counterpart]:
        """Spy to all the attributes"""

        return [mock_category_counterpart()]
