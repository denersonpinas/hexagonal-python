from abc import ABC, abstractmethod
from typing import List
from src.domain.models import BenefitCategorization


class BenefitCategorizationRepositoryInterface(ABC):
    """Interface to Benefit Categorization Repository"""

    @abstractmethod
    def insert_categorization(cls, valor: str, tipo_id: str) -> BenefitCategorization:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_categorization(
        cls, id: int = None, tipo_id: str = None
    ) -> List[BenefitCategorization]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_categorizations(cls) -> List[BenefitCategorization]:
        """abstractmethod"""
        raise Exception("Method not implemented")
