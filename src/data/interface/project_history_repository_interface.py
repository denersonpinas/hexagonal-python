from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.domain.models import ProjectHistory


class ProjectHistoryRepositoryInterface(ABC):
    """Interface to ProjectHistory Repository"""

    @abstractmethod
    def insert_project_history(
        cls, investment_year: int, title: str, investment_type: str, proposal_id: UUID
    ) -> ProjectHistory:
        """abstractmethod"""
        raise Exception("Method not implemented")
