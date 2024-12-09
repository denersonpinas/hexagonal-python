from typing import Dict, List, Type
from src.data.interface import AbginvestTpprojLeiRepositoryInterface
from src.domain.models import AbginvestTpprojLei
from src.domain.use_cases import FindAbginvestTpprojLeiInterface


class FindAbginvestTpprojLei(FindAbginvestTpprojLeiInterface):
    """Class to define use case Find AbginvestTpprojLei"""

    def __init__(
        self, abginvest_tpproj_lei_repo: Type[AbginvestTpprojLeiRepositoryInterface]
    ):
        self.abginvest_tpproj_lei_repo = abginvest_tpproj_lei_repo

    def by_id(self, id: int) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select AbginvestTpprojLei by id
        :param  -   id: id of the register
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(id, int)

        if validate_entry:
            response = self.abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(id=id)

        return {"Success": validate_entry, "Data": response}

    def by_investment_approach(
        self, investment_approach_id: int
    ) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select AbginvestTpprojLei by id
        :param  -   investment_approach_id: id of the investment aproach of the relationship AbginvestmentTpprojLei
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(investment_approach_id, int)

        if validate_entry:
            response = self.abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
                abordagem_investimento_id=investment_approach_id
            )

        return {"Success": validate_entry, "Data": response}

    def by_type_project(
        self, type_project_id: int
    ) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select AbginvestTpprojLei by id
        :param  -   type_project_id: id of the type project of the relationship AbginvestmentTpprojLei
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(type_project_id, int)

        if validate_entry:
            response = self.abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
                tipo_pojeto_id=type_project_id
            )

        return {"Success": validate_entry, "Data": response}

    def by_law(self, law_id: int) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select AbginvestTpprojLei by id
        :param  -   law_id: id of the law of the relationship AbginvestmentTpprojLei
        :return -   Dictionary with informations od the process
        """

        response = None
        validate_entry = isinstance(law_id, int)

        if validate_entry:
            response = self.abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
                lei_id=law_id
            )

        return {"Success": validate_entry, "Data": response}

    def all(self) -> Dict[bool, List[AbginvestTpprojLei]]:
        """Select all AbginvestTpprojLei
        :param  -   is None
        :return -   Dictionary with informations od the process
        """

        response = self.abginvest_tpproj_lei_repo.select_all_abginvest_tpproj_lei()

        return {"Success": True, "Data": response}
