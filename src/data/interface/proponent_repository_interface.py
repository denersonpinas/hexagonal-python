from abc import ABC, abstractmethod
from typing import Optional

from src.domain.models import Proponent


class ProponentRepositoryInterface(ABC):
    """Interface to Proponent Repository"""

    @abstractmethod
    def insert_proponent(
        cls,
        cnpj: str,
        proposal_id: str,
        company_name: str,
        trade_name: Optional[str] = None,
        zip_code: Optional[str] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        neighborhood: Optional[str] = None,
        street: Optional[str] = None,
        number: Optional[int] = None,
        complement: Optional[str] = None,
        website: Optional[str] = None,
        social_media: Optional[str] = None,
        curriculum_summary: Optional[str] = None,
    ) -> Proponent:
        """abstractmethod"""
        raise Exception("Method not implemented")
