from abc import ABC, abstractmethod
from typing import List
from src.domain.models import BenefitCategorizationType


class BenefitCategorizationTypeRepositoryInterface(ABC):
    """Interface to Benefit Categorization Type Repository"""

    @abstractmethod
    def insert_categorization_type(
        cls, id: str, descricao: str, info: str
    ) -> BenefitCategorizationType:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_categorization_type(
        cls, id: str = None
    ) -> List[BenefitCategorizationType]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_categorization_types(cls) -> List[BenefitCategorizationType]:
        """abstractmethod"""
        raise Exception("Method not implemented")
