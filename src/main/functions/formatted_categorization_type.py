from typing import Dict, List, Type

from src.domain.models import BenefitCategorizationType


def formatted_categorization_type(
    data: Type[List[BenefitCategorizationType]],
) -> List[Dict]:
    """Formated List BenefitCategorizationType Object in Dict
    :param      -   data: List Object of the BenefitCategorizationType
    :return     -   Dict with BenefitCategorizationType formatted
    """

    categorization_type = []

    for item in data:
        categorization_type.append(
            {"id": item.id, "info": item.info, "descricao": item.descricao}
        )

    return categorization_type
