from typing import Dict, Type

from src.data.interface import AbginvestTpprojLeiRepositoryInterface
from src.domain.models import AbginvestTpprojLei
from src.domain.test import mock_abginvest_tpproj_lei
from src.domain.use_cases import RegisterAbginvestTpprojLeiInterface


class RegisterAbginvestTpprojLeiSpy(RegisterAbginvestTpprojLeiInterface):
    "Class te define use case: Register AbginvestTpprojLei"

    def __init__(
        self, abginvest_tpproj_lei_repo: Type[AbginvestTpprojLeiRepositoryInterface]
    ):
        self._abginvest_tpproj_lei_repo = abginvest_tpproj_lei_repo
        self.register_param = {}

    def register(
        self, investment_approach_id: int, type_project_id: int, law_id: int
    ) -> Dict[bool, AbginvestTpprojLei]:
        """Register AbginvestTpprojLei use case"""

        response = None
        validate_entry = (
            isinstance(investment_approach_id, int)
            and isinstance(type_project_id, int)
            and isinstance(law_id, int)
        )

        if validate_entry:
            self.register_param["investment_approach_id"] = investment_approach_id
            self.register_param["type_project_id"] = type_project_id
            self.register_param["law_id"] = law_id

            response = mock_abginvest_tpproj_lei()

        return {"Success": validate_entry, "Data": response}
