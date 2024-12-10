from typing import Dict, List, Type
from src.data.interface import AbginvestTpprojLeiContrpartRepositoryInterface
from src.domain.models import AbginvestTpprojLeiContrpart
from src.domain.test import mock_abginvest_tpproj_lei_contrpart
from src.domain.use_cases import FindAbginvestTpprojLeiContrpartInterface


class FindAbginvestTpprojLeiContrpartSpy(FindAbginvestTpprojLeiContrpartInterface):
    """Class to define use case: Select AbginvestTpprojLeiContrpart Spy"""

    def __init__(
        self,
        abginvest_tpproj_lei_contrpart_repository: Type[
            AbginvestTpprojLeiContrpartRepositoryInterface
        ],
    ):
        self.abginvest_tpproj_lei_contrpart_repository = (
            abginvest_tpproj_lei_contrpart_repository
        )
        self.by_id_param = {}
        self.by_abginvest_tpproj_lei_param = {}

    def by_id(self, id: int) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Select AbginvestTpprojLeiContrpart by id spy"""

        self.by_id_param["id"] = id
        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = [mock_abginvest_tpproj_lei_contrpart()]

        return {"Success": validate_entry, "Data": response}

    def by_abginvest_tpproj_lei(
        self,
        abginvest_tpproj_lei_id: int,
    ) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Select AbginvestTpprojLeiContrpart by abginvest_tpproj_lei_id"""

        self.by_abginvest_tpproj_lei_param["abginvest_tpproj_lei_id"] = (
            abginvest_tpproj_lei_id
        )
        response = None
        validate_entry = isinstance(abginvest_tpproj_lei_id, int)

        if validate_entry:
            response = [mock_abginvest_tpproj_lei_contrpart()]

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Select all AbginvestTpprojLeiContrpart spy"""

        response = [mock_abginvest_tpproj_lei_contrpart()]

        return {"Success": True, "Data": response}
