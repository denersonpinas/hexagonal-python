from typing import List
from src.data.interface import AbginvestTpprojLeiRepositoryInterface
from src.domain.models import AbginvestTpprojLei
from src.domain.test import mock_abginvest_tpproj_lei


class AbginvestTpprojLeiRepositorySpy(AbginvestTpprojLeiRepositoryInterface):
    """Spy to AbginvestTpprojLei Repository"""

    def __init__(self):
        self.insert_abginvest_tpproj_lei_params = {}
        self.select_abginvest_tpproj_lei_params = {}

    def insert_abginvest_tpproj_lei(
        self, abordagem_investimento_id: int, lei_id: int, tipo_pojeto_id: int
    ) -> AbginvestTpprojLei:
        """Spy to all the attributes"""

        self.insert_abginvest_tpproj_lei_params["abordagem_investimento_id"] = (
            abordagem_investimento_id
        )
        self.insert_abginvest_tpproj_lei_params["lei_id"] = lei_id
        self.insert_abginvest_tpproj_lei_params["tipo_pojeto_id"] = tipo_pojeto_id

        return mock_abginvest_tpproj_lei()

    def select_abginvest_tpproj_lei(
        self,
        id: int = None,
        abordagem_investimento_id: int = None,
        lei_id: int = None,
        tipo_pojeto_id: int = None,
    ) -> List[AbginvestTpprojLei]:
        """Spy to all the attributes"""

        self.select_abginvest_tpproj_lei_params["id"] = id
        self.select_abginvest_tpproj_lei_params["abordagem_investimento_id"] = (
            abordagem_investimento_id
        )
        self.select_abginvest_tpproj_lei_params["lei_id"] = lei_id
        self.select_abginvest_tpproj_lei_params["tipo_pojeto_id"] = tipo_pojeto_id

        return [mock_abginvest_tpproj_lei()]

    def select_all_abginvest_tpproj_lei(self) -> List[AbginvestTpprojLei]:
        """Spy to all the attributes"""

        return [mock_abginvest_tpproj_lei()]
