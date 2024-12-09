from typing import Dict, List, Type
from src.data.interface import CategoryCounterpartRepositoryInterface
from src.domain.models import CategoryCounterpart
from src.domain.use_cases import FindCategoryCounterpartInterface


class FindCategoryCounterpart(FindCategoryCounterpartInterface):
    """Class to define use case Find Category Counterpart"""

    def __init__(
        self, category_counterpart_repo: Type[CategoryCounterpartRepositoryInterface]
    ):
        self.category_counterpart_repo = category_counterpart_repo

    def by_id(
        self, category_counterpart_id: int
    ) -> Dict[bool, List[CategoryCounterpart]]:
        """Select Category Counterpart by id
        :param  -   category_counterpart_id: id of the category counterpart
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(category_counterpart_id, int)

        if validate_entry:
            response = self.category_counterpart_repo.select_category_counterpart(
                category_counterpart_id=category_counterpart_id
            )

        return {"Success": validate_entry, "Data": response}

    def by_subcategory(
        self, subcategory_id: int
    ) -> Dict[bool, List[CategoryCounterpart]]:
        """Select Category Counterpart by id
        :param  -   subcategory_id: id subcategory of the category counterpart
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(subcategory_id, int)

        if validate_entry:
            response = self.category_counterpart_repo.select_category_counterpart(
                subcategoria_de_id=subcategory_id
            )

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[CategoryCounterpart]]:
        """Select all Category Counterpart
        :param  -   is None
        :return -   Dictionary with informations od the process
        """

        response = self.category_counterpart_repo.select_all_category_counterpart()

        return {"Success": True, "Data": response}
