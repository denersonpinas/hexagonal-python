from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import Thematic


class FindThematicInterface(ABC):
    """Interface to Find Thematic use case"""

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[Thematic]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def all(self) -> Dict[bool, List[Thematic]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
