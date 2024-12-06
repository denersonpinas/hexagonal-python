# Interface
from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import BenefitCategorization


class RegisterBenefitCategorizationInterface(ABC):
    """Interface to Register Benefit Categorization use case"""

    @abstractmethod
    def register(self, value: str, type_id: str) -> Dict[bool, BenefitCategorization]:
        """Use Case"""
        raise Exception("Should implement method: register")
