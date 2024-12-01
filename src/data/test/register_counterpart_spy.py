from typing import Dict, Type

from src.data.interface import CounterpartRepositoryInterface
from src.domain.models import Counterpart
from src.domain.test import mock_counterpart
from src.domain.use_cases import RegisterCounterpartInterface


class RegisterCounterpartSpy(RegisterCounterpartInterface):
    "Class te define use case: Register Counterpart"

    def __init__(self, counterpart_repository: Type[CounterpartRepositoryInterface]):
        self.__counterpart_repository = counterpart_repository
        self.registry_param = {}

    def registry(
        self, descricao: str, exemplo_aplicabilidade: str, obrigatoria: bool
    ) -> Dict[bool, Counterpart]:
        """Register counterpart use case"""

        response = None
        validate_entry = (
            isinstance(descricao, str)
            and isinstance(exemplo_aplicabilidade, str)
            and isinstance(obrigatoria, bool)
            and len(exemplo_aplicabilidade) <= 500
            and len(descricao) <= 500
        )

        if validate_entry:
            self.registry_param["descricao"] = descricao
            self.registry_param["exemplo_aplicabilidade"] = exemplo_aplicabilidade
            self.registry_param["obrigatoria"] = obrigatoria

            response = mock_counterpart()

        return {"Success": validate_entry, "Data": response}
