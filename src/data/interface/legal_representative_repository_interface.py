from abc import ABC, abstractmethod
from typing import Optional

from src.domain.models import LegalRepresentative


class LegalRepresentativeRepositoryInterface(ABC):
    """Interface to LegalRepresentative Repository"""

    @abstractmethod
    def insert_legal_representative(
        cls,
        name: str,
        cpf: str,
        email: str,
        position: str,
        proposal_id: str,
        summary: Optional[str] = None,
    ) -> LegalRepresentative:
        """abstractmethod"""
        raise Exception("Method not implemented")
