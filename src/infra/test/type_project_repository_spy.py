from typing import List
from src.data.interface import TypeProjectRepositoryInterface
from src.domain.models import TypeProject
from src.domain.test import mock_type_project


class TypeProjectRepositorySpy(TypeProjectRepositoryInterface):
    """Spy to TypeProject Repository"""

    def __init__(self):
        self.insert_type_project_params = {}

    def insert_type_project(self, nome: str, descricao: str) -> TypeProject:
        """Spy to all the attributes"""

        self.insert_type_project_params["nome"] = nome
        self.insert_type_project_params["descricao"] = descricao

        return mock_type_project()

    def select_all_type_project(self) -> List[TypeProject]:
        """Spy to all the attributes"""

        return [mock_type_project()]
