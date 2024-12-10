from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import AbginvestTpprojLeiContrpart


class FindAbginvestTpprojLeiContrpartInterface(ABC):
    """Interface to Find AbginvestTpprojLeiContrpart use case"""

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_abginvest_tpproj_lei(
        self,
        abginvest_tpproj_lei_id: int,
    ) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_abginvest_tpproj_lei")

    @abstractmethod
    def all(self) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
