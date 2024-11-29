from typing import Dict, List, Type
from src.data.interface import LawRepositoryInterface
from src.domain.models import Law
from src.domain.test import mock_law
from src.domain.use_cases import FindLawInterface


class FindLawSpy(FindLawInterface):
    """Class to define use case: Select Law Spy"""

    def __init__(self, law_repository: Type[LawRepositoryInterface]):
        self.law_repository = law_repository

    def all(self) -> Dict[bool, List[Law]]:
        """Select Law spy"""

        response = [mock_law()]

        return {"Success": True, "Data": response}
