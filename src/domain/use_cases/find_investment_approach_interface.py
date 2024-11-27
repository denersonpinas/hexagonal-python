from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import InvestmentApproach


class FindInvestmentApproachInterface(ABC):
    """Interface to Find InvestmentApproach use case"""

    @abstractmethod
    def all(self) -> Dict[bool, List[InvestmentApproach]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
