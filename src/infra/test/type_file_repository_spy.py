from typing import List
from src.data.interface import TypeFileRepositoryInterface
from src.domain.models import TypeFile
from src.domain.test import mock_type_file


class TypeFileRepositorySpy(TypeFileRepositoryInterface):
    """Spy to TypeFile Repository"""

    def __init__(self):
        self.insert_type_file_params = {}
        self.select_type_file_params = {}

    def insert_type_file(
        self, id: str, contexto: str, descricao: str, info: str
    ) -> TypeFile:
        """Spy to all the attributes"""

        self.insert_type_file_params["id"] = id
        self.insert_type_file_params["contexto"] = contexto
        self.insert_type_file_params["descricao"] = descricao
        self.insert_type_file_params["info"] = info

        return mock_type_file()

    def select_type_file(self, id: int = None) -> List[TypeFile]:
        """Spy to all the attributes"""

        self.select_type_file_params["id"] = id

        return [mock_type_file()]

    @classmethod
    def select_all_type_file(cls) -> List[TypeFile]:
        """Spy to all the attributes"""

        return [mock_type_file()]
