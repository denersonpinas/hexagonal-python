from typing import Dict, Type

from src.data.interface import TypeFileRepositoryInterface
from src.domain.models import TypeFile
from src.domain.test import mock_type_file
from src.domain.use_cases import RegisterTypeFileInterface


class RegisterTypeFileSpy(RegisterTypeFileInterface):
    "Class te define use case: Register TypeFile"

    def __init__(self, type_file_repo: Type[TypeFileRepositoryInterface]):
        self._type_file_repo = type_file_repo
        self.register_param = {}

    def register(
        self, id: str, context: str, description: str, info: str
    ) -> Dict[bool, TypeFile]:
        """Register TypeFile use case"""

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
            self.register_param["id"] = id
            self.register_param["context"] = context
            self.register_param["description"] = description
            self.register_param["info"] = info

            response = mock_type_file()

        return {"Success": validate_entry, "Data": response}
