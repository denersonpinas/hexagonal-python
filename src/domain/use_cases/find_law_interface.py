from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Law


class FindLawInterface(ABC):
    """Interface to Find Law use case"""

    @abstractmethod
    def all(self) -> Dict[bool, List[Law]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
