from typing import Dict, Type
from src.data.interface import ThematicRepositoryInterface
from src.domain.models import Thematic
from src.domain.use_cases import RegisterThematicInterface


class RegisterThematic(RegisterThematicInterface):
    """Class to define Thematic case: Register Thematic"""

    def __init__(self, thematic_repo: Type[ThematicRepositoryInterface]):
        self._thematic_repo = thematic_repo

    def register(self, description: str) -> Dict[bool, Thematic]:
        """Register Thematic use case
        :param  -   descricao: Description of the Thematic
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(description, str) and len(description) <= 50

        if validate_entry:
            response = self._thematic_repo.insert_thematic(descricao=description)

        return {"Success": validate_entry, "Data": response}
