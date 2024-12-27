from abc import ABC, abstractmethod
from typing import List

from src.domain.models import AbginvestTpprojLeiContrpart


class AbginvestTpprojLeiContrpartRepositoryInterface(ABC):
    """Interface to AbginvestTpprojLeiContrpart Repository"""

    @abstractmethod
    def insert_abginvest_tpproj_lei_contrpart(
        cls,
        ordem: int,
        id_relacao_contrapartida_categoria: int,
        id_abginvest_tpproj_lei: int,
    ) -> AbginvestTpprojLeiContrpart:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_abginvest_tpproj_lei_contrpart(
        cls, id: int = None, id_abginvest_tpproj_lei: int = None
    ) -> List[AbginvestTpprojLeiContrpart]:
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_all_abginvest_tpproj_lei_contrpart(
        cls,
    ) -> List[AbginvestTpprojLeiContrpart]:
        """abstractmethod"""
        raise Exception("Method not implemented")
