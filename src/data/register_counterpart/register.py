from typing import Dict, Type
from src.data.interface import CounterpartRepositoryInterface
from src.domain.models import Counterpart
from src.domain.use_cases.register_counterpart_interface import (
    RegisterCounterpartInterface,
)


class RegisterCounterpart(RegisterCounterpartInterface):
    """Class to define counterpart case: Register Counterpart"""

    def __init__(self, counterpart_repository: Type[CounterpartRepositoryInterface]):
        self.__counterpart_repository = counterpart_repository

    def registry(
        self, descricao: str, exemplo_aplicabilidade: str, obrigatoria: bool
    ) -> Dict[bool, Counterpart]:
        """Register counterpart use case
        :param  -   descricao: description of the counterpart
                -   exemplo_aplicabilidade: aplicability example of the counterpart
                -   obrigatoria: if counterpart is required
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(descricao, str)
            and isinstance(exemplo_aplicabilidade, str)
            and isinstance(obrigatoria, bool)
        )

        if validate_entry:
            response = self.__counterpart_repository.insert_counterpart(
                descricao=descricao,
                exemplo_aplicabilidade=exemplo_aplicabilidade,
                obrigatoria=obrigatoria,
            )

        return {"Success": validate_entry, "Data": response}
