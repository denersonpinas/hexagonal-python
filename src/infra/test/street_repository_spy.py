from src.data.interface import StreetRepositoryInterface
from src.domain.models import Street
from src.domain.test import mock_street


class StreetRepositorySpy(StreetRepositoryInterface):
    """Spy to Street Repository"""

    def __init__(self):
        self.insert_street_params = {}

    def insert_street(self, name: str, neighborhood_id: int) -> Street:
        """Spy to all the attributes"""

        self.insert_street_params["name"] = name
        self.insert_street_params["neighborhood_id"] = neighborhood_id

        return mock_street()
