from abc import ABC, abstractmethod
from typing import List

from src.domain.models import Counterpart


class CounterpartRepositoryInterface(ABC):
    """Interface to Counterpart Repository"""

    @abstractmethod
    def insert_counterpart(
        cls, descricao: str, exemplo_aplicabilidade: str, obrigatoria: bool
    ) -> Counterpart:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_counterpart(
        cls, counterpart_id: int = None, required: bool = None, default: bool = None
    ) -> List[Counterpart]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_counterpart(cls) -> List[Counterpart]:
        """abstractmethod"""
        raise Exception("Method not implemented")
