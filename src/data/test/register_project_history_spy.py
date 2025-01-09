from typing import Dict, Type
import uuid

from sqlalchemy import UUID

from src.data.interface import ProjectHistoryRepositoryInterface
from src.domain.models import ProjectHistory
from src.domain.test import mock_project_history
from src.domain.use_cases import RegisterLawInterface


class RegisterProjectHistorySpy(RegisterLawInterface):
    "Class te define use case: Register ProjectHistory"

    def __init__(
        self, project_history_repository: Type[ProjectHistoryRepositoryInterface]
    ):
        self._project_history_repository = project_history_repository
        self.register_param = {}

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
            self.register_param["investment_year"] = investment_year
            self.register_param["title"] = title
            self.register_param["investment_type"] = investment_type
            self.register_param["proposal_id"] = proposal_id

            response = mock_project_history()

        return {"Success": validate_entry, "Data": response}
