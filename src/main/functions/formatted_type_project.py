from typing import Dict, List, Type

from src.domain.models import TypeProject


def formatted_type_project(
    data: Type[List[TypeProject]],
) -> List[Dict]:
    """Formated List TypeProject Object in Dict
    :param      -   data: List Object of the TypeProject
    :return     -   Dict with TypeProject formatted
    """

    type_project = []

    for item in data:
        type_project.append(
            {"id": item.id, "nome": item.nome, "descricao": item.descricao}
        )

    return type_project
