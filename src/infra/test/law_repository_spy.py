from typing import List
from src.data.interface import LawRepositoryInterface
from src.domain.models import Law
from src.domain.test import mock_law


class LawRepositorySpy(LawRepositoryInterface):
    """Spy to Law Repository"""

    def __init__(self):
        self.insert_law_params = {}

    def insert_law(self, nome: str, descricao: str) -> Law:
        """Spy to all the attributes"""

        self.insert_law_params["nome"] = nome
        self.insert_law_params["descricao"] = descricao

        return mock_law()

    def select_all_law(self) -> List[Law]:
        """Spy to all the attributes"""

        return [mock_law()]
