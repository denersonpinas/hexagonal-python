from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import Counterpart


class FindCounterpartInterface(ABC):
    """Interface to Find Counterpart use case"""

    @abstractmethod
    def by_id(self, counterpart_id: int) -> Dict[bool, List[Counterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_required(self, required: bool) -> Dict[bool, List[Counterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_required")

    @abstractmethod
    def by_default(self, default: bool) -> Dict[bool, List[Counterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_default")

    @abstractmethod
    def by_id_and_required(
        self, counterpart_id: int, required: bool
    ) -> Dict[bool, List[Counterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id_and_required")

    @abstractmethod
    def by_id_and_default(
        self, counterpart_id: int, default: bool
    ) -> Dict[bool, List[Counterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id_and_default")

    @abstractmethod
    def by_required_and_default(
        self, required: bool, default: bool
    ) -> Dict[bool, List[Counterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_required_and_default")

    @abstractmethod
    def by_id_and_required_and_default(
        self, counterpart_id: int, required: bool, default: bool
    ) -> Dict[bool, List[Counterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id_and_required_and_default")

    @abstractmethod
    def all(self) -> Dict[bool, List[Counterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
