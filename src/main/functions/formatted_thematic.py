from typing import Dict, List, Type

from src.domain.models import Thematic


def formatted_thematic(
    data: Type[List[Thematic]],
) -> List[Dict]:
    """Formated List Thematic Object in Dict
    :param      -   data: List Object of the Thematic
    :return     -   Dict with Thematic formatted
    """

    thematic = []

    for item in data:
        thematic.append({"id": item.id, "descricao": item.descricao})

    return thematic
