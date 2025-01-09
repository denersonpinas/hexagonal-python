from typing import Dict, Type

from src.data.interface import NeighborhoodRepositoryInterface
from src.domain.models import Neighborhood
from src.domain.test import mock_neighborhood
from src.domain.use_cases import RegisterLawInterface


class RegisterNeighborhoodSpy(RegisterLawInterface):
    "Class te define use case: Register Neighborhood"

    def __init__(self, neighborhood_repository: Type[NeighborhoodRepositoryInterface]):
        self._neighborhood_repository = neighborhood_repository
        self.register_param = {}

    def register(self, name: str, city_id: int) -> Dict[bool, Neighborhood]:
        """Register neighborhood use case
        :param  -   name: neighborhood name
                -   city_id: foreign key to city
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(city_id, int)
            and len(name) <= 100
            and city_id > 0
        )

        if validate_entry:
            self.register_param["name"] = name
            self.register_param["city_id"] = city_id

            response = mock_neighborhood()

        return {"Success": validate_entry, "Data": response}
