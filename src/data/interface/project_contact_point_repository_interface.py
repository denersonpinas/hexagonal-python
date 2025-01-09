from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.domain.models import ProjectContactPoint


class ProjectContactPointRepositoryInterface(ABC):
    """Interface to ProjectContactPoint Repository"""

    @abstractmethod
    def insert_project_contact(
        cls, name: str, email: str, position: str, proposal_id: UUID
    ) -> ProjectContactPoint:
        """abstractmethod"""
        raise Exception("Method not implemented")
