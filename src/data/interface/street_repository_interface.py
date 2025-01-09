from abc import ABC, abstractmethod

from src.domain.models import Street


class StreetRepositoryInterface(ABC):
    """Interface to Street Repository"""

    @abstractmethod
    def insert_street(cls, name: str, neighborhood_id: int) -> Street:
        """abstractmethod"""
        raise Exception("Method not implemented")
