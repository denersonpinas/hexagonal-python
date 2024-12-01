from typing import Dict, List, Type
from src.data.interface import CategoryCounterpartRepositoryInterface
from src.domain.models import CategoryCounterpart
from src.domain.test import mock_category_counterpart
from src.domain.use_cases import FindCategoryCounterpartInterface


class FindCategoryCounterpartSpy(FindCategoryCounterpartInterface):
    """Class to define use case: Select Counterpart Spy"""

    def __init__(
        self,
        category_counterpart_repository: Type[CategoryCounterpartRepositoryInterface],
    ):
        self.category_counterpart_repository = category_counterpart_repository
        self.by_id_param = {}
        self.by_subcategory_param = {}

    def by_id(
        self, category_counterpart_id: int
    ) -> Dict[bool, List[CategoryCounterpart]]:
        """Select Category Counterpart by id spy"""

        self.by_id_param["category_counterpart_id"] = category_counterpart_id
        response = None
        validate_entry = isinstance(category_counterpart_id, int)

        if validate_entry:
            response = [mock_category_counterpart()]

        return {"Success": validate_entry, "Data": response}

    def by_subcategory(
        self, subcategory_id: int
    ) -> Dict[bool, List[CategoryCounterpart]]:
        """Select Category Counterpart by is id subcategory"""

        self.by_subcategory_param["subcategory_id"] = subcategory_id
        response = None
        validate_entry = isinstance(subcategory_id, int)

        if validate_entry:
            response = [mock_category_counterpart()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[CategoryCounterpart]]:
        """Select all Category Counterpart spy"""

        response = [mock_category_counterpart()]

        return {"Success": True, "Data": response}
