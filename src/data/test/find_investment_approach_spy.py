from typing import Dict, List, Type
from src.data.interface import InvestmentApproachRepositoryInterface
from src.domain.models import InvestmentApproach
from src.domain.test import mock_investment_appr
from src.domain.use_cases import FindInvestmentApproachInterface


class FindInvestmentApproachSpy(FindInvestmentApproachInterface):
    """Class to define use case: Select InvestmentApproach Spy"""

    def __init__(
        self, investment_appr_repository: Type[InvestmentApproachRepositoryInterface]
    ):
        self.investment_appr_repository = investment_appr_repository

    def all(self) -> Dict[bool, List[InvestmentApproach]]:
        """Select InvestmentApproach spy"""

        response = [mock_investment_appr()]

        return {"Success": True, "Data": response}
