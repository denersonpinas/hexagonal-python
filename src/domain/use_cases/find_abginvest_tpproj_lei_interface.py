from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import AbginvestTpprojLei


class FindAbginvestTpprojLeiInterface(ABC):
    """Interface to Find AbginvestTpprojLei use case"""

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_investment_approach(
        self, investment_approach_id: int
    ) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Specific Case"""

        raise Exception("Should implement method: by_investment_approach")

    @abstractmethod
    def by_type_project(
        self, type_project_id: int
    ) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Specific Case"""

        raise Exception("Should implement method: by_type_project")

    @abstractmethod
    def by_law(self, law_id: int) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Specific Case"""

        raise Exception("Should implement method: by_law")

    @abstractmethod
    def all(self) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
