from abc import ABC, abstractmethod
from typing import Dict, Optional

from src.domain.models import LegalRepresentative


class RegisterLegalRepresentativeInterface(ABC):
    """Interface to Register LegalRepresentative use case"""

    @abstractmethod
    def register(
        self,
        name: str,
        cpf: str,
        email: str,
        position: str,
        proposal_id: str,
        summary: Optional[str] = None,
    ) -> Dict[bool, LegalRepresentative]:
        """Use Case"""

        raise Exception("Should implement method: register")
