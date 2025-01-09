from typing import Dict, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.project_contact_point_repository_interface import (
    ProjectContactPointRepositoryInterface,
)
from src.domain.use_cases.register_project_contact_point_interface import (
    RegisterProjectContactPointInterface,
)
from src.domain.models import ProjectContactPoint


class RegisterProjectContactPoint(RegisterProjectContactPointInterface):
    """Class to define project contact point case: Register Project Contact Point"""

    def __init__(
        self,
        project_contact_point_repository: Type[ProjectContactPointRepositoryInterface],
    ):
        self._project_contact_point_repository = project_contact_point_repository

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
            response = self._project_contact_point_repository.insert_project_contact(
                name=name, email=email, position=position, proposal_id=proposal_id
            )

        return {"Success": validate_entry, "Data": response}
