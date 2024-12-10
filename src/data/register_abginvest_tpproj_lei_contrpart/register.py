from typing import Dict, Type
from src.data.interface import AbginvestTpprojLeiContrpartRepositoryInterface
from src.domain.models import AbginvestTpprojLeiContrpart
from src.domain.use_cases import RegisterAbginvestTpprojLeiContrpartInterface


class RegisterAbginvestTpprojLeiContrpart(RegisterAbginvestTpprojLeiContrpartInterface):
    """Class to define AbginvestTpprojLeiContrpart case: Register AbginvestTpprojLeiContrpart"""

    def __init__(
        self,
        abginvest_tpproj_lei_contrpart_repo: Type[
            AbginvestTpprojLeiContrpartRepositoryInterface
        ],
    ):
        self._abginvest_tpproj_lei_contrpart_repo = abginvest_tpproj_lei_contrpart_repo

    def register(
        self, ordem: int, id_relacao_contrapartida: int, id_abginvest_tpproj_lei: int
    ) -> Dict[bool, AbginvestTpprojLeiContrpart]:
        """Register AbginvestTpprojLeiContrpart use case
        :param  -   ordem: order of the create AbginvestTpprjLeiContrpart
                -   id_relacao_contrapartida: id of the relationship
                counterpart relation with AbginvestTpprjLeiContrpart
                -   id_abginvest_tpproj_lei: id of the relationship
                AbginvestTpprjLei with AbginvestTpprjLeiContrpart
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(ordem, int)
            and isinstance(id_relacao_contrapartida, int)
            and isinstance(id_abginvest_tpproj_lei, int)
        )

        if validate_entry:
            response = self._abginvest_tpproj_lei_contrpart_repo.insert_abginvest_tpproj_lei_contrpart(
                ordem=ordem,
                id_relacao_contrapartida=id_relacao_contrapartida,
                id_abginvest_tpproj_lei=id_abginvest_tpproj_lei,
            )

        return {"Success": validate_entry, "Data": response}
