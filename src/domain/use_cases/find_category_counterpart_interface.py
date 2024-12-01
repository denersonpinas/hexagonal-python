from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import CategoryCounterpart


class FindCategoryCounterpartInterface(ABC):
    """Interface to Find Category Counterpart use case"""

    @abstractmethod
    def by_id(
        cls, category_counterpart_id: int
    ) -> Dict[bool, List[CategoryCounterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_subcategory(
        cls, subcategory_id: int
    ) -> Dict[bool, List[CategoryCounterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: by_subcategory")

    @abstractmethod
    def all(cls) -> Dict[bool, List[CategoryCounterpart]]:
        """Specific Case"""

        raise Exception("Should implement method: all")
