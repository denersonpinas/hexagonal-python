from typing import Dict, List, Type
from src.data.interface import BenefitCategorizationTypeRepositoryInterface
from src.domain.models import BenefitCategorizationType
from src.domain.use_cases import FindBenefitCategorizationTypeInterface


class FindBenefitCategorizationType(FindBenefitCategorizationTypeInterface):
    """Class to define use case Find BenefitCategorizationType"""

    def __init__(
        self,
        categorization_type_repo: Type[BenefitCategorizationTypeRepositoryInterface],
    ):
        self.categorization_type_repo = categorization_type_repo

    def by_id(self, id: str) -> Dict[bool, List[BenefitCategorizationType]]:
        """Select BenefitCategorizationType by id
        :param  -   id: id of the register
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(id, str)

        if validate_entry:
            response = self.categorization_type_repo.select_categorization_type(id=id)

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[BenefitCategorizationType]]:
        """Select all BenefitCategorizationType
        :param  -   is None
        :return -   Dictionary with informations od the process
        """

        response = self.categorization_type_repo.select_all_categorization_types()

        return {"Success": True, "Data": response}
