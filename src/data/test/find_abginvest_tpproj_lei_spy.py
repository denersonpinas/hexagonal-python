from typing import Dict, List, Type
from src.data.interface import AbginvestTpprojLeiRepositoryInterface
from src.domain.models import AbginvestTpprojLei
from src.domain.test import mock_abginvest_tpproj_lei
from src.domain.use_cases import FindAbginvestTpprojLeiInterface


class FindAbginvestTpprojLeiSpy(FindAbginvestTpprojLeiInterface):
    """Class to define use case: Select AbginvestTpprojLei Spy"""

    def __init__(
        self,
        abginvest_tpproj_lei_repository: Type[AbginvestTpprojLeiRepositoryInterface],
    ):
        self.abginvest_tpproj_lei_repository = abginvest_tpproj_lei_repository
        self.by_id_param = {}
        self.by_investment_approach_param = {}
        self.by_type_project_param = {}
        self.by_law_param = {}

    def by_id(self, id: int) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select AbginvestTpprojLei by id spy"""

        self.by_id_param["id"] = id
        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = [mock_abginvest_tpproj_lei()]

        return {"Success": validate_entry, "Data": response}

    def by_investment_approach(
        self, investment_approach_id: int
    ) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select AbginvestTpprojLei by is id investment approach"""

        self.by_investment_approach_param["investment_approach_id"] = (
            investment_approach_id
        )
        response = None
        validate_entry = isinstance(investment_approach_id, int)

        if validate_entry:
            response = [mock_abginvest_tpproj_lei()]

        return {"Success": validate_entry, "Data": response}

    def by_type_project(
        self, type_project_id: int
    ) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select AbginvestTpprojLei by is id type project"""

        self.by_type_project_param["type_project_id"] = type_project_id
        response = None
        validate_entry = isinstance(type_project_id, int)

        if validate_entry:
            response = [mock_abginvest_tpproj_lei()]

        return {"Success": validate_entry, "Data": response}

    def by_law(self, law_id: int) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select AbginvestTpprojLei by is id law"""

        self.by_law_param["law_id"] = law_id
        response = None
        validate_entry = isinstance(law_id, int)

        if validate_entry:
            response = [mock_abginvest_tpproj_lei()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select all AbginvestTpprojLei spy"""

        response = [mock_abginvest_tpproj_lei()]

        return {"Success": True, "Data": response}
