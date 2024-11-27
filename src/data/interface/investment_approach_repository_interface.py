from abc import ABC, abstractmethod
from typing import List
from src.domain.models import InvestmentApproach


class InvestmentApproachRepositoryInterface(ABC):
    """Interface to Investment Approach Repository"""

    @abstractmethod
    def insert_investment_approach(
        self, descricao: str, incetivado: bool
    ) -> InvestmentApproach:
        """abstractmethod"""
        raise Exception("Method insert_investment_approach not implemented")

    @abstractmethod
    def select_all_investment_approach(self) -> List[InvestmentApproach]:
        """abstractmethod"""
        raise Exception("Method select_all_investment_approach not implemented")
