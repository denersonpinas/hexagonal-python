from typing import Dict, List, Type
from src.data.interface import TypeProjectRepositoryInterface
from src.domain.models import TypeProject
from src.domain.test import mock_type_project
from src.domain.use_cases import FindTypeProjectInterface


class FindTypeProjectSpy(FindTypeProjectInterface):
    """Class to define use case: Select TypeProject Spy"""

    def __init__(self, type_project_repository: Type[TypeProjectRepositoryInterface]):
        self.type_project_repository = type_project_repository

    def all(self) -> Dict[bool, List[TypeProject]]:
        """Select TypeProject spy"""

        response = [mock_type_project()]

        return {"Success": True, "Data": response}
