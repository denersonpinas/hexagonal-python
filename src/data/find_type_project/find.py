from typing import Dict, List, Type
from src.data.interface import TypeProjectRepositoryInterface
from src.domain.use_cases import FindTypeProjectInterface
from src.domain.models import TypeProject


class FindTypeProject(FindTypeProjectInterface):
    """Class to define use case Find TypeProject"""

    def __init__(self, type_project_repository: Type[TypeProjectRepositoryInterface]):
        self._type_project_repository = type_project_repository

    def all(self) -> Dict[bool, List[TypeProject]]:
        """Select TypeProject
        :param  -   is None
        :return -   Dictionary with informations od the process
        """
        response = self._type_project_repository.select_all_type_project()

        return {"Success": True, "Data": response}
