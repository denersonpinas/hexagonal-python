from abc import ABC, abstractmethod
from typing import List

from src.domain.models import Law


class LawRepositoryInterface(ABC):
    """Interface to Law Repository"""

    @abstractmethod
    def insert_law(self, nome: str, descricao: str) -> Law:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_law(self) -> List[Law]:
        """abstractmethod"""
        raise Exception("Method not implemented")
