from typing import Dict, Type
from src.data.interface.street_repository_interface import StreetRepositoryInterface
from src.domain.use_cases.register_street_interface import RegisterStreetInterface
from src.domain.models import Street


class RegisterStreet(RegisterStreetInterface):
    """Class to define street case: Register Street"""

    def __init__(self, street_repository: Type[StreetRepositoryInterface]):
        self._street_repository = street_repository

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
            response = self._street_repository.insert_street(
                name=name, neighborhood_id=neighborhood_id
            )

        return {"Success": validate_entry, "Data": response}
