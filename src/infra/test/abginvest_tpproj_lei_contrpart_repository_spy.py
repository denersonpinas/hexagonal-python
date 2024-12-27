from typing import List
from src.data.interface import AbginvestTpprojLeiContrpartRepositoryInterface
from src.domain.models import AbginvestTpprojLeiContrpart
from src.domain.test import mock_abginvest_tpproj_lei_contrpart


class AbginvestTpprojLeiContrpartRepositorySpy(
    AbginvestTpprojLeiContrpartRepositoryInterface
):
    """Spy to AbginvestTpprojLeiContrpart Repository"""

    def __init__(self):
        self.insert_abginvest_tpproj_lei_contrpart_params = {}
        self.select_abginvest_tpproj_lei_contrpart_params = {}

    def insert_abginvest_tpproj_lei_contrpart(
        self,
        ordem: int,
        id_relacao_contrapartida_categoria: int,
        id_abginvest_tpproj_lei: int,
    ) -> AbginvestTpprojLeiContrpart:
        """Spy to all the attributes"""

        self.insert_abginvest_tpproj_lei_contrpart_params["ordem"] = ordem
        self.insert_abginvest_tpproj_lei_contrpart_params[
            "id_relacao_contrapartida_categoria"
        ] = id_relacao_contrapartida_categoria
        self.insert_abginvest_tpproj_lei_contrpart_params["id_abginvest_tpproj_lei"] = (
            id_abginvest_tpproj_lei
        )

        return mock_abginvest_tpproj_lei_contrpart()

    def select_abginvest_tpproj_lei_contrpart(
        self, id: int = None, id_abginvest_tpproj_lei: int = None
    ) -> List[AbginvestTpprojLeiContrpart]:
        """Spy to all the attributes"""

        self.select_abginvest_tpproj_lei_contrpart_params["id"] = id
        self.select_abginvest_tpproj_lei_contrpart_params["id_abginvest_tpproj_lei"] = (
            id_abginvest_tpproj_lei
        )

        return [mock_abginvest_tpproj_lei_contrpart()]

    def select_all_abginvest_tpproj_lei_contrpart(
        cls,
    ) -> List[AbginvestTpprojLeiContrpart]:
        """Spy to all the attributes"""

        return [mock_abginvest_tpproj_lei_contrpart()]
