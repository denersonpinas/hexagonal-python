from typing import Dict, Type

from src.data.interface import CityRepositoryInterface
from src.domain.models import City
from src.domain.test import mock_city
from src.domain.use_cases import RegisterCityInterface


class RegisterCitySpy(RegisterCityInterface):
    "Class te define use case: Register City"

    def __init__(self, city_repository: Type[CityRepositoryInterface]):
        self._city_repository = city_repository
        self.register_param = {}

    def register(self, name: str, state: str) -> Dict[bool, City]:
        """Register city use case
        :param  -   name: city name
                -   state: state abbreviation
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(state, str)
            and len(name) <= 100
            and len(state) == 2
        )

        if validate_entry:
            self.register_param["name"] = name
            self.register_param["state"] = state

            response = mock_city()

        return {"Success": validate_entry, "Data": response}
