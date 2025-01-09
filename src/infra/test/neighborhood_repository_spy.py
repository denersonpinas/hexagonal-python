from src.data.interface import NeighborhoodRepositoryInterface
from src.domain.models import Neighborhood
from src.domain.test import mock_neighborhood


class NeighborhoodRepositorySpy(NeighborhoodRepositoryInterface):
    """Spy to Neighborhood Repository"""

    def __init__(self):
        self.insert_neighborhood_params = {}

    def insert_neighborhood(self, name: str, city_id: int) -> Neighborhood:
        """Spy to all the attributes"""

        self.insert_neighborhood_params["name"] = name
        self.insert_neighborhood_params["city_id"] = city_id

        return mock_neighborhood()
