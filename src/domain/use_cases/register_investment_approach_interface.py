from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import InvestmentApproach


class RegisterInvestmentApproachInterface(ABC):
    """Interface to Register InvestmentApproach use case"""

    @abstractmethod
    def registry(
        self, descricao: str, incetivado: bool
    ) -> Dict[bool, InvestmentApproach]:
        """Use Case"""

        raise Exception("Should implement method: register")
