from typing import Dict, Type
from src.data.interface.city_repository_interface import CityRepositoryInterface
from src.domain.use_cases.register_city_interface import RegisterCityInterface
from src.domain.models import City


class RegisterCity(RegisterCityInterface):
    """Class to define city case: Register City"""

    def __init__(self, city_repository: Type[CityRepositoryInterface]):
        self._city_repository = city_repository

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
            response = self._city_repository.insert_city(name=name, state=state)

        return {"Success": validate_entry, "Data": response}
