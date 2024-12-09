from typing import Dict, List, Type

from src.domain.models import Law


def formatted_law(
    data: Type[List[Law]],
) -> List[Dict]:
    """Formated List Law Object in Dict
    :param      -   data: List Object of the Law
    :return     -   Dict with Law formatted
    """

    law = []

    for item in data:
        law.append({"id": item.id, "nome": item.nome, "descricao": item.descricao})

    return law
