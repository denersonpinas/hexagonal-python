from typing import Dict, Type
from src.data.interface.neighborhood_repository_interface import (
    NeighborhoodRepositoryInterface,
)
from src.domain.use_cases.register_neighborhood_interface import (
    RegisterNeighborhoodInterface,
)
from src.domain.models import Neighborhood


class RegisterNeighborhood(RegisterNeighborhoodInterface):
    """Class to define neighborhood case: Register Neighborhood"""

    def __init__(self, neighborhood_repository: Type[NeighborhoodRepositoryInterface]):
        self._neighborhood_repository = neighborhood_repository

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
            response = self._neighborhood_repository.insert_neighborhood(
                name=name, city_id=city_id
            )

        return {"Success": validate_entry, "Data": response}
