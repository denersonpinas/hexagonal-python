from typing import Dict, List, Type
from src.data.interface import ThematicRepositoryInterface
from src.domain.models import Thematic
from src.domain.test import mock_thematic
from src.domain.use_cases import FindThematicInterface


class FindThematicSpy(FindThematicInterface):
    """Class to define use case: Select Thematic Spy"""

    def __init__(
        self,
        thematic_repository: Type[ThematicRepositoryInterface],
    ):
        self.thematic_repository = thematic_repository
        self.by_id_param = {}

    def by_id(self, id: int) -> Dict[bool, List[Thematic]]:
        """Select Thematic by id spy"""

        self.by_id_param["id"] = id
        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = [mock_thematic()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[Thematic]]:
        """Select all Thematic spy"""

        response = [mock_thematic()]

        return {"Success": True, "Data": response}
