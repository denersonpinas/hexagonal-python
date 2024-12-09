from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import InvestmentApproach


class RegisterInvestmentApproachInterface(ABC):
    """Interface to Register InvestmentApproach use case"""

    @abstractmethod
    def register(
        self, descricao: str, incentivado: bool
    ) -> Dict[bool, InvestmentApproach]:
        """Use Case"""

        raise Exception("Should implement method: register")
