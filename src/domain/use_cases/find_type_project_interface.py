from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import TypeProject


class FindTypeProjectInterface(ABC):
    """Interface to Find TypeProject use case"""

    @abstractmethod
    def all(self) -> Dict[bool, List[TypeProject]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
