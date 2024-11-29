from abc import ABC, abstractmethod
from typing import List

from src.domain.models import TypeProject


class TypeProjectRepositoryInterface(ABC):
    """Interface to TypeProject Repository"""

    @abstractmethod
    def insert_type_project(self, nome: str, descricao: str) -> TypeProject:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_type_project(self) -> List[TypeProject]:
        """abstractmethod"""
        raise Exception("Method not implemented")
