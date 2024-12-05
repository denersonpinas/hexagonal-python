from typing import Dict, List, Type
from src.data.interface import TypeFileRepositoryInterface
from src.domain.models import TypeFile
from src.domain.test import mock_type_file
from src.domain.use_cases import FindTypeFileInterface


class FindTypeFileSpy(FindTypeFileInterface):
    """Class to define use case: Select TypeFile Spy"""

    def __init__(
        self,
        type_file_repository: Type[TypeFileRepositoryInterface],
    ):
        self.type_file_repository = type_file_repository
        self.by_id_param = {}

    def by_id(self, id: int) -> Dict[bool, List[TypeFile]]:
        """Select TypeFile by id spy"""

        self.by_id_param["id"] = id
        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = [mock_type_file()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[TypeFile]]:
        """Select all TypeFile spy"""

        response = [mock_type_file()]

        return {"Success": True, "Data": response}
