from abc import ABC, abstractmethod
from typing import List

from src.domain.models import TypeFile


class TypeFileRepositoryInterface(ABC):
    """Interface to TypeFile Repository"""

    @abstractmethod
    def insert_type_file(
        cls, id: str, contexto: str, descricao: str, info: str
    ) -> TypeFile:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_type_file(cls, id: int = None) -> List[TypeFile]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_type_file(cls) -> List[TypeFile]:
        """abstractmethod"""
        raise Exception("Method not implemented")
