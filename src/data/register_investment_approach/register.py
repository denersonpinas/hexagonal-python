from typing import Type
from src.domain.use_cases.register_investment_approach_interface import (
    RegisterInvestmentApproachInterface,
)
from src.infra.repo.investment_approach_repository import InvestmentApproachRepository


class RegisterInvestmentApproach(RegisterInvestmentApproachInterface):
    """Class to define investment approach case: Register InvestmentApproach"""

    def __init__(self, investment_appr_repository: Type[InvestmentApproachRepository]):
        self._investment_appr_repository = investment_appr_repository

    def register(self, descricao: str, incentivado: bool):
        """Register investment approach use case
        :param  -   descricao: description of the investment approach
                -   incentivado: if investment approach is incentivized or not
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(descricao, str)
            and isinstance(incentivado, bool)
            and len(descricao) <= 80
        )

        if validate_entry:
            response = self._investment_appr_repository.insert_investment_approach(
                descricao=descricao, incentivado=incentivado
            )

        return {"Success": validate_entry, "Data": response}
