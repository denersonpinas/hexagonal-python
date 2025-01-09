from sqlalchemy import UUID
from src.data.interface import ProjectContactPointRepositoryInterface
from src.domain.models import ProjectContactPoint
from src.domain.test import mock_project_contact


class ProjectContactPointRepositorySpy(ProjectContactPointRepositoryInterface):
    """Spy to ProjectContactPoint Repository"""

    def __init__(self):
        self.insert_project_contact_params = {}

    def insert_project_contact(
        self, name: str, email: str, position: str, proposal_id: UUID
    ) -> ProjectContactPoint:
        """Spy to all the attributes"""

        self.insert_project_contact_params["name"] = name
        self.insert_project_contact_params["email"] = email
        self.insert_project_contact_params["position"] = position
        self.insert_project_contact_params["proposal_id"] = proposal_id

        return mock_project_contact()
