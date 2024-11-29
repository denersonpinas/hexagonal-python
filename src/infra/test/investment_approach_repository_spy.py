from typing import List
from src.data.interface import (
    InvestmentApproachRepositoryInterface,
)
from src.domain.models import InvestmentApproach
from src.domain.test import mock_investment_appr


class InvestmentApproachRepositorySpy(InvestmentApproachRepositoryInterface):
    """Spy to InvestmentApproach Repository"""

    def __init__(self):
        self.insert_investment_appr_params = {}

    def insert_investment_approach(
        self, descricao: str, incetivado: bool
    ) -> InvestmentApproach:
        """Spy to all the attributes"""

        self.insert_investment_appr_params["descricao"] = descricao
        self.insert_investment_appr_params["incetivado"] = incetivado

        return mock_investment_appr()

    def select_all_investment_approach(self) -> List[InvestmentApproach]:
        """Spy to all the attributes"""

        return [mock_investment_appr()]
