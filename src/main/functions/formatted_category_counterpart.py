from typing import Dict, List, Type

from src.domain.models import CategoryCounterpart


def formatted_category_counterpart(
    data: Type[List[CategoryCounterpart]],
) -> List[Dict]:
    """Formated List CategoryCounterpart Object in Dict
    :param      -   data: List Object of the CategoryCounterpart
    :return     -   Dict with CategoryCounterpart formatted
    """

    category_counterpart = []

    for item in data:
        category_counterpart.append(
            {
                "id": item.id,
                "subcategoria_de": item.subcategoria_de_id,
                "nome": item.nome,
                "descricao": item.descricao,
            }
        )

    return category_counterpart
