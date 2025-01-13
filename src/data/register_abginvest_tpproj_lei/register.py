from typing import Dict, Type
from src.data.interface import AbginvestTpprojLeiRepositoryInterface
from src.domain.models import AbginvestTpprojLei
from src.domain.use_cases import RegisterAbginvestTpprojLeiInterface


class RegisterAbginvestTpprojLei(RegisterAbginvestTpprojLeiInterface):
    """Class to define AbginvestTpprojLei case: Register AbginvestTpprojLei"""

    def __init__(
        self, abginvest_tpproj_lei_repo: Type[AbginvestTpprojLeiRepositoryInterface]
    ):
        self._abginvest_tpproj_lei_repo = abginvest_tpproj_lei_repo

    def register(
        self, investment_approach_id: int, type_project_id: int, law_id: int
    ) -> Dict[bool, AbginvestTpprojLei]:
        """Register AbginvestTpprojLei use case
        :param  -   investment_approach_id: id investment approach of the relationship abginvest tpprj lei
                -   law_id: id law of the relationship abginvest tpprj lei
                -   type_project_id: id type project of the relationship abginvest tpprj lei
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(investment_approach_id, int)
            and isinstance(type_project_id, int)
            and (law_id is None or isinstance(law_id, int))
        )

        if validate_entry:
            response = self._abginvest_tpproj_lei_repo.insert_abginvest_tpproj_lei(
                abordagem_investimento_id=investment_approach_id,
                lei_id=law_id,
                tipo_pojeto_id=type_project_id,
            )

        return {"Success": validate_entry, "Data": response}
