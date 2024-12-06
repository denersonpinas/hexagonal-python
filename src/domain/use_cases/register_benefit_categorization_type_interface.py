# Interface
from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import BenefitCategorizationType


class RegisterBenefitCategorizationTypeInterface(ABC):
    """Interface to Register Benefit Categorization Type use case"""

    @abstractmethod
    def register(
        self, description: str, info: str
    ) -> Dict[bool, BenefitCategorizationType]:
        """Use Case"""
        raise Exception("Should implement method: register")
