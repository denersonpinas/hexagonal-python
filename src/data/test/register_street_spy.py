from typing import Dict, Type

from src.data.interface import StreetRepositoryInterface
from src.domain.models import Street
from src.domain.test import mock_street
from src.domain.use_cases import RegisterStreetInterface


class RegisterStreetSpy(RegisterStreetInterface):
    "Class te define use case: Register Street"

    def __init__(self, street_repository: Type[StreetRepositoryInterface]):
        self._street_repository = street_repository
        self.register_param = {}

    def register(self, name: str, neighborhood_id: int) -> Dict[bool, Street]:
        """Register street use case
        :param  -   name: street name
                -   neighborhood_id: foreign key to neighborhood
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(neighborhood_id, int)
            and len(name) <= 100
            and neighborhood_id > 0
        )

        if validate_entry:
            self.register_param["name"] = name
            self.register_param["neighborhood_id"] = neighborhood_id

            response = mock_street()

        return {"Success": validate_entry, "Data": response}
