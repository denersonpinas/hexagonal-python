from typing import Dict, List, Type

from src.domain.models import Counterpart


def formatted_counterpart(
    data: Type[List[Counterpart]],
) -> List[Dict]:
    """Formated List Counterpart Object in Dict
    :param      -   data: List Object of the Counterpart
    :return     -   Dict with Counterpart formatted
    """

    counterpart = []

    for item in data:
        counterpart.append(
            {
                "id": item.id,
                "descricao": item.descricao,
                "obrigatoria": item.obrigatoria,
                "exemplo_aplicabilidade": item.exemplo_aplicabilidade,
            }
        )

    return counterpart
