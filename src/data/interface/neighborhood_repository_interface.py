from abc import ABC, abstractmethod

from src.domain.models import Neighborhood


class NeighborhoodRepositoryInterface(ABC):
    """Interface to Neighborhood Repository"""

    @abstractmethod
    def insert_neighborhood(cls, name: str, city_id: int) -> Neighborhood:
        """abstractmethod"""
        raise Exception("Method not implemented")
