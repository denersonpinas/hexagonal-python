from typing import List
from src.data.interface import ThematicRepositoryInterface
from src.domain.models import Thematic
from src.domain.test import mock_thematic


class ThematicRepositorySpy(ThematicRepositoryInterface):
    """Spy to Thematic Repository"""

    def __init__(self):
        self.insert_thematic_params = {}
        self.select_thematic_params = {}

    def insert_thematic(self, descricao: str) -> Thematic:
        """Spy to all the attributes"""

        self.insert_thematic_params["descricao"] = descricao

        return mock_thematic()

    def select_thematic(self, id: int = None) -> List[Thematic]:
        """Spy to all the attributes"""

        self.select_thematic_params["id"] = id

        return [mock_thematic()]

    def select_all_thematic(cls) -> List[Thematic]:
        """Spy to all the attributes"""

        return [mock_thematic()]
