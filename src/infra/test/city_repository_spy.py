from src.data.interface import CityRepositoryInterface
from src.domain.models import City
from src.domain.test import mock_city


class CityRepositorySpy(CityRepositoryInterface):
    """Spy to City Repository"""

    def __init__(self):
        self.insert_city_params = {}

    def insert_city(self, name: str, state: str) -> City:
        """Spy to all the attributes"""

        self.insert_city_params["name"] = name
        self.insert_city_params["state"] = state

        return mock_city()
