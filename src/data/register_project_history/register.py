from typing import Dict, Type
import uuid

from sqlalchemy import UUID
from src.data.interface.project_history_repository_interface import (
    ProjectHistoryRepositoryInterface,
)
from src.domain.use_cases.register_project_history_interface import (
    RegisterProjectHistoryInterface,
)
from src.domain.models import ProjectHistory


class RegisterProjectHistory(RegisterProjectHistoryInterface):
    """Class to define project history case: Register Project History"""

    def __init__(
        self, project_history_repository: Type[ProjectHistoryRepositoryInterface]
    ):
        self._project_history_repository = project_history_repository

    def register(
        self, investment_year: int, title: str, investment_type: str, proposal_id: UUID
    ) -> Dict[bool, ProjectHistory]:
        """Register project history use case
        :param  -   investment_year: year of investment
                -   title: project title
                -   investment_type: type of investment
                -   proposal_id: foreign key to proposal
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(investment_year, int)
            and isinstance(title, str)
            and isinstance(investment_type, str)
            and isinstance(proposal_id, uuid.UUID)
            and investment_year > 1900
            and len(title) <= 100
            and len(investment_type) <= 50
        )

        if validate_entry:
            response = self._project_history_repository.insert_project_history(
                investment_year=investment_year,
                title=title,
                investment_type=investment_type,
                proposal_id=proposal_id,
            )

        return {"Success": validate_entry, "Data": response}
