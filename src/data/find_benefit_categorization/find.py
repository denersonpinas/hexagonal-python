from typing import Dict, List, Type
from src.data.interface import BenefitCategorizationRepositoryInterface
from src.domain.models import BenefitCategorization
from src.domain.use_cases import FindBenefitCategorizationInterface


class FindBenefitCategorization(FindBenefitCategorizationInterface):
    """Class to define use case Find BenefitCategorization"""

    def __init__(
        self, categorization_repo: Type[BenefitCategorizationRepositoryInterface]
    ):
        self.categorization_repo = categorization_repo

    def by_id(self, id: int) -> Dict[bool, List[BenefitCategorization]]:
        """Select BenefitCategorization by id
        :param  -   id: id of the register
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = self.categorization_repo.select_categorization(id=id)

        return {"Success": validate_entry, "Data": response}

    def by_type(self, type_id: str) -> Dict[bool, List[BenefitCategorization]]:
        """Select BenefitCategorization by id
        :param  -   type_id: id of the relationship register
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(type_id, str)

        if validate_entry:
            response = self.categorization_repo.select_categorization(tipo_id=type_id)

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[BenefitCategorization]]:
        """Select all BenefitCategorization
        :param  -   is None
        :return -   Dictionary with informations od the process
        """

        response = self.categorization_repo.select_all_categorizations()

        return {"Success": True, "Data": response}
