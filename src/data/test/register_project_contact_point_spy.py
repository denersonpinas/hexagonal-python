from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.data.interface import ProjectContactPointRepositoryInterface
from src.domain.models import ProjectContactPoint
from src.domain.test import mock_project_contact
from src.domain.use_cases import RegisterProjectContactPointInterface


class RegisterProjectContactPointSpy(RegisterProjectContactPointInterface):
    "Class te define use case: Register ProjectContactPoint"

    def __init__(
        self,
        project_contact_point_repository: Type[ProjectContactPointRepositoryInterface],
    ):
        self._project_contact_point_repository = project_contact_point_repository
        self.register_param = {}

    def register(
        self, name: str, email: str, position: str, proposal_id: UUID
    ) -> Dict[bool, ProjectContactPoint]:
        """Register project contact point use case
        :param  -   name: contact person name
                -   email: contact email
                -   position: contact position
                -   proposal_id: foreign key to proposal
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(email, str)
            and isinstance(position, str)
            and isinstance(proposal_id, uuid.UUID)
            and len(name) <= 100
            and len(email) <= 100
            and len(position) <= 100
            and "@" in email
        )

        if validate_entry:
            self.register_param["name"] = name
            self.register_param["email"] = email
            self.register_param["position"] = position
            self.register_param["proposal_id"] = proposal_id

            response = mock_project_contact()

        return {"Success": validate_entry, "Data": response}
