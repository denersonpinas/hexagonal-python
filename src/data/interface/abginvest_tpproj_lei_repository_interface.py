from abc import ABC, abstractmethod
from typing import List

from src.domain.models import AbginvestTpprojLei


class AbginvestTpprojLeiRepositoryInterface(ABC):
    """Interface to Abginvest Tpproj Lei Repository"""

    @abstractmethod
    def insert_abginvest_tpproj_lei(
        self, abordagem_investimento_id: int, lei_id: int, tipo_projeto_id: int
    ) -> AbginvestTpprojLei:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_abginvest_tpproj_lei(
        id: int = None,
        abordagem_investimento_id: int = None,
        lei_id: int = None,
        tipo_projeto_id: int = None,
    ) -> List[AbginvestTpprojLei]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_abginvest_tpproj_lei(self) -> List[AbginvestTpprojLei]:
        """abstractmethod"""
        raise Exception("Method not implemented")
