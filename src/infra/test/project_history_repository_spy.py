from sqlalchemy import UUID
from src.data.interface import ProjectHistoryRepositoryInterface
from src.domain.models import ProjectHistory
from src.domain.test import mock_project_history


class ProjectHistoryRepositorySpy(ProjectHistoryRepositoryInterface):
    """Spy to ProjectHistory Repository"""

    def __init__(self):
        self.insert_project_history_params = {}

    def insert_project_history(
        self, investment_year: int, title: str, investment_type: str, proposal_id: UUID
    ) -> ProjectHistory:
        """Spy to all the attributes"""

        self.insert_project_history_params["investment_year"] = investment_year
        self.insert_project_history_params["title"] = title
        self.insert_project_history_params["investment_type"] = investment_type
        self.insert_project_history_params["proposal_id"] = proposal_id

        return mock_project_history()
