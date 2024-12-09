from abc import ABC, abstractmethod
from typing import List

from src.domain.models import CategoryCounterpart


class CategoryCounterpartRepositoryInterface(ABC):
    """Interface to Category Counterpart Repository"""

    @abstractmethod
    def insert_category_counterpart(
        self, nome: str, descricao: str, subcategoria_de_id: int
    ) -> CategoryCounterpart:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_category_counterpart(self) -> List[CategoryCounterpart]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_category_counterpart(
        self, category_counterpart_id: int = None, subcategoria_de_id: int = None
    ) -> List[CategoryCounterpart]:
        """abstractmethod"""
        raise Exception("Method not implemented")
