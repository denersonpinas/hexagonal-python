from typing import Dict, Type

from src.data.interface import InvestmentApproachRepositoryInterface
from src.domain.models import InvestmentApproach
from src.domain.test import mock_investment_appr
from src.domain.use_cases import RegisterInvestmentApproachInterface


class RegisterInvestmentApproachSpy(RegisterInvestmentApproachInterface):
    "Class te define use case: Register InvestmentApproach"

    def __init__(
        self,
        investment_approach_repository: Type[InvestmentApproachRepositoryInterface],
    ):
        self.__investment_approach_repository = investment_approach_repository
        self.registry_param = {}

    def registry(
        self, descricao: str, incetivado: str
    ) -> Dict[bool, InvestmentApproach]:
        """Register investmentApproach use case"""

        response = None
        validate_entry = isinstance(descricao, str) and isinstance(incetivado, bool)

        if validate_entry:
            self.registry_param["descricao"] = descricao
            self.registry_param["incetivado"] = incetivado

            response = mock_investment_appr()

        return {"Success": validate_entry, "Data": response}
