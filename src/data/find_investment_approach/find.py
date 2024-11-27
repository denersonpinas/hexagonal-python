from typing import Dict, List, Type
from src.data.interface import InvestmentApproachRepositoryInterface
from src.domain.use_cases import FindInvestmentApproachInterface
from src.domain.models import InvestmentApproach


class FindInvestmentApproach(FindInvestmentApproachInterface):
    """Class to define use case Find InvestmentApproach"""

    def __init__(
        self, investment_appr_repository: Type[InvestmentApproachRepositoryInterface]
    ):
        self.investment_appr_repository = investment_appr_repository

    def all(self) -> Dict[bool, List[InvestmentApproach]]:
        """Select InvestmentApproach
        :param  -   is None
        :return -   Dictionary with informations od the process
        """
        response = self.investment_appr_repository.select_all_investment_approach()

        return {"Success": True, "Data": response}
