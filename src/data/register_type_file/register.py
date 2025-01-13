from typing import Dict, Type
from src.data.interface import TypeFileRepositoryInterface
from src.domain.models import TypeFile
from src.domain.use_cases import RegisterTypeFileInterface


class RegisterTypeFile(RegisterTypeFileInterface):
    """Class to define TypeFile case: Register TypeFile"""

    def __init__(self, type_file_repo: Type[TypeFileRepositoryInterface]):
        self._type_file_repo = type_file_repo

    def register(
        self, id: str, context: str, description: str, info: str
    ) -> Dict[bool, TypeFile]:
        """Register TypeFile use case
        :param  -   context: Context of the TypeFile
                -   description: Description of the TypeFile
                -   info: infor of the TypeFile
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(id, str)
            and isinstance(context, str)
            and isinstance(description, str)
            and isinstance(info, str)
            and len(context) <= 32
            and len(description) <= 120
            and len(info) <= 1000
        )

        if validate_entry:
            response = self._type_file_repo.insert_type_file(
                id=id,
                contexto=context,
                descricao=description,
                info=info,
            )

        return {"Success": validate_entry, "Data": response}
