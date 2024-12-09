from typing import Dict, List, Type

from src.domain.models import InvestmentApproach


def formatted_investment_approach(
    data: Type[List[InvestmentApproach]],
) -> List[Dict]:
    """Formated List InvestmentApproach Object in Dict
    :param      -   data: List Object of the InvestmentApproach
    :return     -   Dict with InvestmentApproach formatted
    """

    investment_appr = []

    for item in data:
        investment_appr.append(
            {
                "id": item.id,
                "descricao": item.descricao,
                "incentivado": item.incentivado,
            }
        )

    return investment_appr
