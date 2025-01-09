from abc import ABC, abstractmethod

from src.domain.models import City


class CityRepositoryInterface(ABC):
    """Interface to City Repository"""

    @abstractmethod
    def insert_city(cls, name: str, state: str) -> City:
        """abstractmethod"""
        raise Exception("Method not implemented")
