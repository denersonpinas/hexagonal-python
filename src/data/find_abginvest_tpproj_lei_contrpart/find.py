from typing import Dict, List, Type
from src.data.interface import AbginvestTpprojLeiContrpartRepositoryInterface
from src.domain.models import AbginvestTpprojLeiContrpart
from src.domain.use_cases import FindAbginvestTpprojLeiContrpartInterface


class FindAbginvestTpprojLeiContrpart(FindAbginvestTpprojLeiContrpartInterface):
    """Class to define use case Find AbginvestTpprojLeiContrpart"""

    def __init__(
        self,
        abginvest_tpproj_lei_contrpart_repo: Type[
            AbginvestTpprojLeiContrpartRepositoryInterface
        ],
    ):
        self.abginvest_tpproj_lei_contrpart_repo = abginvest_tpproj_lei_contrpart_repo

    def by_id(self, id: int) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Select AbginvestTpprojLeiContrpart by id
        :param  -   id: id of the register
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = self.abginvest_tpproj_lei_contrpart_repo.select_abginvest_tpproj_lei_contrpart(
                id=id
            )

        return {"Success": validate_entry, "Data": response}

    def by_abginvest_tpproj_lei(
        self,
        abginvest_tpproj_lei_id: int,
    ) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Select AbginvestTpprojLeiContrpart by id
        :param  -   abginvest_tpproj_lei_id: id of the relationship AbginvestmentTpprojLei
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(abginvest_tpproj_lei_id, int)

        if validate_entry:
            response = self.abginvest_tpproj_lei_contrpart_repo.select_abginvest_tpproj_lei_contrpart(
                id_abginvest_tpproj_lei=abginvest_tpproj_lei_id
            )

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[AbginvestTpprojLeiContrpart]]:
        """Select all AbginvestTpprojLeiContrpart
        :param  -   is None
        :return -   Dictionary with informations od the process
        """

        response = (
            self.abginvest_tpproj_lei_contrpart_repo.select_all_abginvest_tpproj_lei_contrpart()
        )

        return {"Success": True, "Data": response}
