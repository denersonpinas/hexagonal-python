from typing import Dict, Type

from src.data.interface import ThematicRepositoryInterface
from src.domain.models import Thematic
from src.domain.test import mock_thematic
from src.domain.use_cases import RegisterThematicInterface


class RegisterThematicSpy(RegisterThematicInterface):
    "Class te define use case: Register Thematic"

    def __init__(self, thematic_repo: Type[ThematicRepositoryInterface]):
        self._thematic_repo = thematic_repo
        self.register_param = {}

    def register(self, description: str) -> Dict[bool, Thematic]:
        """Register Thematic use case"""

        response = None
        validate_entry = isinstance(description, str) and len(description) <= 50

        if validate_entry:
            self.register_param["description"] = description

            response = mock_thematic()

        return {"Success": validate_entry, "Data": response}
