from typing import Dict, Type

from src.data.interface import LawRepositoryInterface
from src.domain.models import Law
from src.domain.test import mock_law
from src.domain.use_cases import RegisterLawInterface


class RegisterLawSpy(RegisterLawInterface):
    "Class te define use case: Register Law"

    def __init__(
        self,
        law_repository: Type[LawRepositoryInterface],
    ):
        self.__law_repository = law_repository
        self.registry_param = {}

    def registry(self, nome: str, descricao: str) -> Dict[bool, Law]:
        """Register Law use case"""

        response = None
        validate_entry = (
            isinstance(descricao, str)
            and isinstance(nome, str)
            and len(descricao) <= 250
            and len(nome) <= 100
        )

        if validate_entry:
            self.registry_param["nome"] = nome
            self.registry_param["descricao"] = descricao

            response = mock_law()

        return {"Success": validate_entry, "Data": response}
