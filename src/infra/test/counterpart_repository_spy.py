from typing import List
from src.data.interface import CounterpartRepositoryInterface
from src.domain.models import Counterpart
from src.domain.test import mock_counterpart


class CounterpartRepositorySpy(CounterpartRepositoryInterface):
    """Spy to Counterpart Repository"""

    def __init__(self):
        self.insert_counterpart_params = {}
        self.select_counterpart_params = {}

    def insert_counterpart(
        self, descricao, exemplo_aplicabilidade, obrigatoria
    ) -> Counterpart:
        """Spy to all the attributes"""

        self.insert_counterpart_params["descricao"] = descricao
        self.insert_counterpart_params["exemplo_aplicabilidade"] = (
            exemplo_aplicabilidade
        )
        self.insert_counterpart_params["obrigatoria"] = obrigatoria

        return mock_counterpart()

    def select_counterpart(
        self, counterpart_id=None, required=None, default=None
    ) -> List[Counterpart]:
        """Spy to all the attributes"""

        self.select_counterpart_params["counterpart_id"] = counterpart_id
        self.select_counterpart_params["required"] = required
        self.select_counterpart_params["default"] = default

        return [mock_counterpart()]

    def select_all_counterpart(self) -> List[Counterpart]:
        """Spy to all the attributes"""

        return [mock_counterpart()]
