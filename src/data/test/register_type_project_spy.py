from typing import Dict, Type

from src.data.interface import TypeProjectRepositoryInterface
from src.domain.models import TypeProject
from src.domain.test import mock_type_project
from src.domain.use_cases import RegisterTypeProjectInterface


class RegisterTypeProjectSpy(RegisterTypeProjectInterface):
    "Class te define use case: Register Type Project"

    def __init__(
        self,
        type_project_repository: Type[TypeProjectRepositoryInterface],
    ):
        self._type_project_repository = type_project_repository
        self.register_param = {}

    def register(self, nome: str, descricao: str) -> Dict[bool, TypeProject]:
        """Register TypeProject use case"""

        response = None
        validate_entry = (
            isinstance(descricao, str)
            and isinstance(nome, str)
            and len(descricao) <= 250
            and len(nome) <= 100
        )

        if validate_entry:
            self.register_param["nome"] = nome
            self.register_param["descricao"] = descricao

            response = mock_type_project()

        return {"Success": validate_entry, "Data": response}
