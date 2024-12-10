from typing import Dict, Type

from src.data.interface import AbginvestTpprojLeiContrpartRepositoryInterface
from src.domain.models import AbginvestTpprojLeiContrpart
from src.domain.test import mock_abginvest_tpproj_lei_contrpart
from src.domain.use_cases import RegisterAbginvestTpprojLeiContrpartInterface


class RegisterAbginvestTpprojLeiContrpartSpy(
    RegisterAbginvestTpprojLeiContrpartInterface
):
    "Class te define use case: Register AbginvestTpprojLeiContrpart"

    def __init__(
        self,
        abginvest_tpproj_lei_contrpart_repo: Type[
            AbginvestTpprojLeiContrpartRepositoryInterface
        ],
    ):
        self._abginvest_tpproj_lei_contrpart_repo = abginvest_tpproj_lei_contrpart_repo
        self.register_param = {}

    def register(
        self, ordem: int, id_relacao_contrapartida: int, id_abginvest_tpproj_lei: int
    ) -> Dict[bool, AbginvestTpprojLeiContrpart]:
        """Register AbginvestTpprojLeiContrpart use case"""

        response = None
        validate_entry = (
            isinstance(ordem, int)
            and isinstance(id_relacao_contrapartida, int)
            and isinstance(id_abginvest_tpproj_lei, int)
        )

        if validate_entry:
            self.register_param["ordem"] = ordem
            self.register_param["id_relacao_contrapartida"] = id_relacao_contrapartida
            self.register_param["id_abginvest_tpproj_lei"] = id_abginvest_tpproj_lei

            response = mock_abginvest_tpproj_lei_contrpart()

        return {"Success": validate_entry, "Data": response}
