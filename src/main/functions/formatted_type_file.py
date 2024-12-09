from typing import Dict, List, Type

from src.domain.models import TypeFile


def formatted_type_file(
    data: Type[List[TypeFile]],
) -> List[Dict]:
    """Formated List TypeFile Object in Dict
    :param      -   data: List Object of the TypeFile
    :return     -   Dict with TypeFile formatted
    """

    type_file = []

    for item in data:
        type_file.append(
            {
                "id": item.id,
                "contexto": item.contexto,
                "descricao": item.descricao,
                "info": item.info,
            }
        )

    return type_file
