from typing import Dict, List, Type
from src.data.interface import LawRepositoryInterface
from src.domain.use_cases import FindLawInterface
from src.domain.models import Law


class FindLaw(FindLawInterface):
    """Class to define use case Find Law"""

    def __init__(self, law_repository: Type[LawRepositoryInterface]):
        self._law_repository = law_repository

    def all(self) -> Dict[bool, List[Law]]:
        """Select Law
        :param  -   is None
        :return -   Dictionary with informations od the process
        """
        response = self._law_repository.select_all_law()

        return {"Success": True, "Data": response}
