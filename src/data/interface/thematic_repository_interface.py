from abc import ABC, abstractmethod
from typing import List

from src.domain.models import Thematic


class ThematicRepositoryInterface(ABC):
    """Interface to Thematic Repository"""

    @abstractmethod
    def insert_thematic(cls, descricao: str) -> Thematic:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_thematic(cls, id: int = None) -> List[Thematic]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_thematic(cls) -> List[Thematic]:
        """abstractmethod"""
        raise Exception("Method not implemented")
