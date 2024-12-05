from typing import Dict, List, Type
from src.data.interface import TypeFileRepositoryInterface
from src.domain.use_cases import FindTypeFileInterface
from src.domain.models import TypeFile


class FindTypeFile(FindTypeFileInterface):
    """Class to define use case Find TypeFile"""

    def __init__(self, type_file_repository: Type[TypeFileRepositoryInterface]):
        self._type_file_repository = type_file_repository

    def by_id(self, id: int) -> Dict[bool, List[TypeFile]]:
        """Select TypeFile by id
        :param  -   id: id of the register
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = self._type_file_repository.select_type_file(id=id)

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[TypeFile]]:
        """Select TypeFile
        :param  -   is None
        :return -   Dictionary with informations od the process
        """
        response = self._type_file_repository.select_all_type_file()

        return {"Success": True, "Data": response}
