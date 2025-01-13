from typing import Dict, List, Type

from src.domain.models import BenefitCategorization


def formatted_categorization(
    data: Type[List[BenefitCategorization]],
) -> List[Dict]:
    """Formated List BenefitCategorization Object in Dict
    :param      -   data: List Object of the BenefitCategorization
    :return     -   Dict with BenefitCategorization formatted
    """

    categorization = []

    for item in data:
        categorization.append(
            {"id": item.id, "valor": item.valor, "tipo": item.tipo_id}
        )

    return categorization
