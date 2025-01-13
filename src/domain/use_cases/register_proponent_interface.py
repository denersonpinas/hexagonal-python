from abc import ABC, abstractmethod
from typing import Dict, Optional

from sqlalchemy import UUID

from src.domain.models import Proponent


class RegisterProponentInterface(ABC):
    """Interface to Register Proponent use case"""

    @abstractmethod
    def register(
        self,
        cnpj: str,
        proposal_id: UUID,
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
    ) -> Dict[bool, Proponent]:
        """Use Case"""

        raise Exception("Should implement method: register")
