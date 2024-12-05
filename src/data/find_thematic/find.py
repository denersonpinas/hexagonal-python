from typing import Dict, List, Type
from src.data.interface import ThematicRepositoryInterface
from src.domain.models import Thematic
from src.domain.use_cases import FindThematicInterface


class FindThematic(FindThematicInterface):
    """Class to define use case Find Thematic"""

    def __init__(self, thematic_repo: Type[ThematicRepositoryInterface]):
        self.thematic_repo = thematic_repo

    def by_id(self, id: int) -> Dict[bool, List[Thematic]]:
        """Select Thematic by id
        :param  -   id: id of the register
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = self.thematic_repo.select_thematic(id=id)

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[Thematic]]:
        """Select all Thematic
        :param  -   is None
        :return -   Dictionary with informations od the process
        """

        response = self.thematic_repo.select_all_thematic()

        return {"Success": True, "Data": response}
