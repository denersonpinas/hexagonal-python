from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import TypeFile


class FindTypeFileInterface(ABC):
    """Interface to Find TypeFile use case"""

    @abstractmethod
    def by_id(self, id: int) -> Dict[bool, List[TypeFile]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def all(self) -> Dict[bool, List[TypeFile]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
